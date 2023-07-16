from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import HuggingFaceEmbeddings

from datasets import load_dataset
from pathlib import Path
from tqdm import tqdm

import requests
import pandas as pd
import os

class QuickBot():
    
    def __init__(self, data, model_path):
        self.data = data
        self.model_path = model_path
        
        pass
    def data_proc(self):
         
        if not os.path.isfile(self.data): 
            # Download the medical_dialog dataset from Hugging Face
            dataset = load_dataset('medical_dialog', 'processed.en')

            # Convert the dataset to a pandas dataframe
            df = pd.DataFrame(dataset['train'])

            # Print the first 5 rows of the dataframe
            df.head()

            dialog = []
            # make each sentence on a seperate row
            patient, doctor = zip(*df['utterances'])
            for i in range(len(patient)):
              dialog.append(patient[i])
              dialog.append(doctor[i])

            dialog_df = pd.DataFrame({"dialog": dialog})
            # save the data to txt file
            dialog_df.to_csv(self.data, sep=' ', index=False)
        else:
            print('data already exists in path.')

    def pull_model(self):
        
        if not os.path.isfile(self.model_path): 
            local_path = self.model_path
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)

            # download the commertial gpt4all-j model
            url = "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"
            # send a GET request to the URL to download the file. Stream since it's large
            response = requests.get(url, stream=True)

            # open the file in binary mode and write the contents of the response to it in chunks
            # This is a large file, so be prepared to wait.
            with open(local_path, 'wb') as f:
                for chunk in tqdm(response.iter_content(chunk_size=8192)):
                    if chunk:
                        f.write(chunk)
        else:
            print('model already exists in path.')

    def create_assets(self, chunk_size: int = 500, overlap: int = 25, n_threads: int=4, max_tokens: int=50, repeat_penalty: float = 1.20):
        # add the path to the CV as a PDF
        loader = TextLoader(self.data)
        # Text Splitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        # Embed the document and store into chroma DB
        self.index = VectorstoreIndexCreator(embedding= HuggingFaceEmbeddings(), text_splitter=text_splitter).from_loaders([loader])
        #init gpt4all
        # specify the path to the .bin downloaded file
        local_path = self.model_path  # replace with your desired local file path
        # Callbacks support token-wise streaming
        callbacks = [StreamingStdOutCallbackHandler()]
        # Verbose is required to pass to the callback manager
        self.llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True, backend='gptj', n_threads=n_threads, n_predict=max_tokens, repeat_penalty=repeat_penalty)

    def inference(self, user_input: str, context_verbosity: bool = False, top_k: int=2):

        # perform similarity search and retrieve the context from our documents
        results = self.index.vectorstore.similarity_search(user_input, k=top_k)
        # join all context information (top 4) into one string 
        context = "\n".join([document.page_content for document in results])
        if context_verbosity:
            print(f"Retrieving information related to your question...")
            print(f"Found this content which is most similar to your question: {context}")

        template = """
        Please use the following health related information to answer the patient's question. 
        Context: {context}
        ---
        This is the patient's question: {question}
        Answer: This is what our health professionals suggest."""

        prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)

        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        print("Processing the information with gpt4all...\n")
        response = llm_chain.run(user_input)
        return response