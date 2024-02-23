# fun dialogues
A library of datasets, LLM tooling, and open source models that can be used for training and inference for prototyping purposes. The project began as a collection of fictitious dialogues that can be used to train language models or augment prompts for prototyping and educational purposes. It has now grown to include tooling for LLM application development purposes and open source models. 

### Key components of fun dialogues:
- **JudgyRAG**: RAG eval tool
- **Benchmark Datasets**: custom benchmark datasets
- **Dialogues**: fictitious dialogue datasets for fun, experimentation, and testing. 

You can install fun dialogues using pip: `pip install fundialogues`

<div align="center">
    <img src="https://github.com/eduand-alvarez/fun-dialogues/assets/57263404/1d8ce401-b595-442f-980c-8ae06ed9d4b2" alt="Fun Dialogues Logo" width="750"/>
</div>

# JudgyRAG
JudgyRAG is a component of the FunDialogues Python library focused on evaluating the performance of Retrieval-Augmented Generation (RAG) systems. It facilitates this by creating synthetic datasets based on custom datasets, enabling a unique assessment of a RAG system's question-answering capabilities in a zero-shot Q&A context. Initially, JudgyRAG's primary functionality is the automatic generation of custom multiple-choice Q&A datasets. Future iterations will introduce further automation to seamlessly integrate with popular frameworks, enhancing testing and benchmarking processes.

### Workflow

The workflow for JudgyRAG includes:

1. **Scraping PDFs**: Information is extracted from PDFs into structured text formats.
2. **Chunking Data**: Extracted data is chunked similarly to vector database embeddings for RAG, simulating data breakdown and storage.
3. **Question Generation**: Each chunk acts as a knowledge base, with custom prompts instructing supported models (currently LLaMA 7B and 13B chat) to generate multiple-choice questions.
4. **Iterative Parsing**: Chunks are processed iteratively, generating a multiple-choice question for each.
5. **Quality Checks**: Poor-quality chunks leading to failed question generation are flagged for user review.
6. **Benchmark Compilation**: The final document includes multiple-choice questions, correct answers, and source knowledge chunks.
7. **RAG System Evaluation**: The synthetic benchmark dataset can be used to assess a RAG system, with automation for this process planned for future updates.

### Environment Setup

Follow these steps to set up your environment for JudgyRAG:

#### Step 1
Install Visual Studio 2022 Community Edition with the “Desktop development with C++” workload.

#### Step 2
Update to the latest GPU driver.

#### Step 3
Install the Intel® oneAPI Base Toolkit 2024.0.

#### Step 4
Download the necessary wheels:

```bash
wget https://intel-extension-for-pytorch.s3.amazonaws.com/ipex_stable/xpu/torch-2.1.0a0%2Bcxx11.abi-cp39-cp39-win_amd64.whl
wget https://intel-extension-for-pytorch.s3.amazonaws.com/ipex_stable/xpu/torchvision-0.16.0a0%2Bcxx11.abi-cp39-cp39-win_amd64.whl
wget https://intel-extension-for-pytorch.s3.amazonaws.com/ipex_stable/xpu/intel_extension_for_pytorch-2.1.10%2Bxpu-cp39-cp39-win_amd64.whl
```

#### Step 5

Install the downloaded packages and BigDL LLM:

```bash
pip install torch-2.1.0a0+cxx11.abi-cp39-cp39-win_amd64.whl
pip install torchvision-0.16.0a0+cxx11.abi-cp39-cp39-win_amd64.whl
pip install intel_extension_for_pytorch-2.1.10+xpu-cp39-cp39-win_amd64.whl
pip install --pre --upgrade bigdl-llm[xpu]
conda install libuv
```

#### Step 6
Activate the Intel oneAPI environment:

```bash
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat"
```

For the latest setup instructions for BigDL LLM inference, visit [BigDL Documentation](https://bigdl.readthedocs.io/en/latest/doc/LLM/Overview/install_gpu.html)

### Example Usage of JudgyRAG

```python
from fundialogues import benchgen, judgypdf

folder_path = ""
output_directory = ""
chunk_file = ""
benchmark_output_directory = ""

judgypdf(folder_path, output_directory)
benchgen(chunk_file, benchmark_output_directory)
```
# Benchmark Datasets

### opengeoquery-v1
OpenGeoQuery-v1 is the first edition of a benchmark dataset composed of statements associated with the geosciences. The content of the dataset touches on topics like geophysics, petrology, minerology, seismology, geomorphology, etc. The purpose of this dataset is to use as a benchmark and for fine-tuning small geoscience LLMs (coming soon).

# Dialogues
- Customer Service
  - Grocery Cashier: 100 fictitious examples of dialogues between a customer at a grocery store and the cashier.
  - Robot Maintenance: 100 fictitious examples of dialogues between a robot arm technician and a customer.
  - Apple Picker Maintenance: 100 fictitious examples of dialogues between a apple harvesting equipment technician and a customer.
- Academia
  - Physics Office Hours: 100 fictitious examples of dialogues between a physics professor and a student during office hours. 
- Healthcare
  - Minor Consultation: 100 fictitious examples of dialogues between a doctor and a patient during a minor medical consultation.
- Sports
  - Basketball Coach: 100 fictitious examples of dialogues between a basketball coach and the players on the court during a game.
 
### How to Load Dialogues
Loading dialogues can be accomplished using the fun dialogues library or Hugging Face datasets library. 

### Load using fun dialogues

Assuming you've already installed fundialogues.

Use loader utility to load dataset as pandas dataframe. Further processing might be required for use.
```
from fundialogues import dialoader

# load as pandas dataframe
physics_office_hours = dialoader("FunDialogues/academia-physics-office-hours")
```

### Loading using Hugging Face datasets

1. Install datasets package `pip install datasets`

2. Load using datasets
```
from datasets import load_dataset

physics_office_hours = load_dataset("FunDialogues/academia-physics-office-hours")
```

# Disclaimer

The dialogues contained in this repository are provided for experimental purposes only. It is important to note that these dialogues are assumed to be original work by a human and are entirely fictitious, despite the possibility of some examples including factually correct information. The primary intention behind these dialogues is to serve as a tool for language modeling experimentation and should not be used for designing real-world products beyond non-production prototyping.

Please be aware that the utilization of fictitious data in these datasets may increase the likelihood of language model artifacts, such as hallucinations or unrealistic responses. Therefore, it is essential to exercise caution and discretion when employing these datasets for any purpose.

It is crucial to emphasize that none of the scenarios described in the fun dialogues dataset should be relied upon to provide advice or guidance to humans. These scenarios are purely fictitious and are intended solely for demonstration purposes. Any resemblance to real-world situations or individuals is entirely coincidental.

The responsibility for the usage and application of these datasets, tools, and codes rests solely with the individual or entity employing them. By accessing and utilizing these assets and all contents of the repository, you acknowledge that you have read and understood this disclaimer, and you agree to use them at your own discretion and risk.
