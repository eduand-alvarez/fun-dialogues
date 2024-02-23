import pandas as pd 
import os, sys

from judgyrag.utils.generate import qa_gen
from judgyrag.utils.postproc import process_qa
from bigdl.llm.transformers import AutoModelForCausalLM
from transformers import LlamaTokenizer

# make sure to run >> call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat"
# to initialize the oneapi environment before running this

def benchgen(chunked_data: str, output_path: str, llama_size:int = 7, 
             debug: bool = False, use_cache: bool = True, max_length: int = 300):
    """
    Generate a synthetic benchmark dataset using a specified LLaMA model.

    Parameters
    ----------
    chunked_data : str
        The file path to the CSV containing chunked data to be used as input for question generation.
    output_path : str
        The directory path where the output CSV file containing generated questions will be saved.
    llama_size : int, optional
        The size of the LLaMA model to be used for question generation. Supported sizes are 7 (for LLaMA-7B) 
        and 13 (for LLaMA-13B). Default is 7.
    debug : bool, optional
        If True, additional debug information will be saved to a separate file. Default is False.
    use_cache : bool, optional
        Indicates whether to use cached model weights. Default is True.
    max_length : int, optional
        The maximum length of the generated text. Default is 300.

    Notes
    -----
    The function attempts to load the specified LLaMA model and generate questions based on the content 
    of the chunked data. Generated questions, along with the input chunked data, are saved in a CSV file.

    Raises
    ------
    Exception
        If there is an issue with model loading or question generation.

    """
    
    # data loading block
    df = pd.read_csv(chunked_data)
    num_rows = len(df)

    # prep output file properties
    output_path = os.path.join(output_path,'judgyrag_q.csv')
    print('target file path for judgyrag synthetic benchmark', output_path)
    if debug:
        debug_log = pd.DataFrame()
        debug_path = os.path.join(output_path,'debug.csv')
        print('target debug file path for judgyrag synthetic benchmark', output_path)

    # create data
    bench_df = pd.DataFrame()

    # model loading block
    if llama_size == 7:
        hf_model ="meta-llama/Llama-2-7b-chat-hf"
    elif llama_size == 13:
        hf_model = "meta-llama/Llama-2-13b-chat-hf"
    else:
        print('Invalid Llama v2 model size selected, only meta-llama/Llama-2-7b-chat-hf and meta-llama/Llama-2-13b-chat-hf are supported')
    
    try:
        model = AutoModelForCausalLM.from_pretrained(hf_model,
                                                 load_in_4bit=True,
                                                 optimize_model=True,
                                                 trust_remote_code=True,
                                                 use_cache=use_cache,
                                                 cpu_embedding=False)
        model = model.to('xpu')
        # Load tokenizer
        tokenizer = LlamaTokenizer.from_pretrained(hf_model, trust_remote_code=True)

        latency_total = 0

        for ind in df.index:
            knowledge_chunk = df['Chunk Content'][ind]
            qa, latency = qa_gen(model, tokenizer,max_length=max_length,input=knowledge_chunk)
            new_bench_qa = process_qa(qa=qa, knowledge_chunk=knowledge_chunk)
            bench_df = pd.concat([bench_df, new_bench_qa], ignore_index=True)
            print(f"benchmark question {ind+1}/{num_rows} completed in {latency} seconds...")

            latency_total = latency_total + latency

            if debug:
                ind_log = pd.DataFrame({'ind':[ind],'qa':[qa],'latency':[latency],'knowledge_chunk':[knowledge_chunk],'bench_qa':[new_bench_qa]})
                debug_log = pd.concat([debug_log, ind_log], ignore_index=True)    
                if ind == num_rows - 1:
                    debug_log.to_csv(debug_path)

        print(f'Benchmark Generated in {latency_total} seconds or {latency_total/60} minutes')

        bench_df.to_csv(output_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()

def exit_program():
    """
    Exits the program with a standard system exit call.

    This function is called in case of a critical error where continuing execution is not possible or desired.
    
    """
    print("Exiting the program...")
    sys.exit(0)