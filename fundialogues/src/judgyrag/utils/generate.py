import torch
import time

def prompt_template(chunk_value):

    """
    Generates a prompt template for question generation based on provided chunk information.

    Parameters
    ----------
    chunk_value : str
        The text chunk for which a question is to be generated, forming the context for the question.

    Returns
    -------
    str
        A formatted string (prompt) that includes instructions for question generation along with the provided chunk value.

    Notes
    -----
    The prompt is designed for use with models trained to generate multiple choice questions based on a given context.
    It includes both instructions and the context (chunk_value) within a specified template.
    """

    prompt = f"""
    <s>[INST] <<SYS>>
    You are an expert at creating multiple choice questions. You will be provided information and you will use only this information
    to create a multiple choice question composed of four options a, b, c, and d. Only provide the correct letter option for the correct answer.
    You must provide your response in exactly the following format:

    question text/ option a / option b/ option c/ optiond/ correct answer

    <</SYS>>

    {chunk_value} [/INST]
    """
    return prompt


def qa_gen(model, tokenizer, max_length, input):
    """
    Generates a question and answer pair using a specified model and tokenizer, based on given input text.

    Parameters
    ----------
    model : transformers.PreTrainedModel
        The pre-trained model used for question generation.
    tokenizer : transformers.PreTrainedTokenizer
        The tokenizer corresponding to the pre-trained model, used for encoding input text and decoding output tokens.
    max_length : int
        The maximum length of the generated text (in tokens).
    input : str
        The input text for which the question and answer pair is to be generated.

    Returns
    -------
    tuple
        A tuple containing two elements:
        - The generated question and answer pair as a string.
        - The latency (in seconds) of the generation process.

    Notes
    -----
    The function encodes the input text using the provided tokenizer, generates output tokens with the model, and then decodes these tokens back to text.
    It measures the time taken for the generation process and returns both the generated text and the latency.

    Raises
    ------
    Exception
        If an error occurs during the token generation or decoding process.
    """

    print("Starting to generate synthetic Q&A Dataset")

    # Generate predicted tokens
    with torch.inference_mode():
            engineered_prompt = prompt_template(input)
            input_ids = tokenizer.encode(engineered_prompt, return_tensors="pt").to('xpu')

            # start inference
            st = time.time()
            output = model.generate(input_ids,
                                    max_new_tokens=max_length,
                                    use_cache=True)
            torch.xpu.synchronize()
            end = time.time()
            output = output.cpu()
            output_str = tokenizer.decode(output[0], skip_special_tokens=True)
            generation_latency = end-st

    print("JudgyRAG Dataset Generation Complete!")
    return output_str, generation_latency

