# fun dialogues
A library of datasets, LLM tooling, and open source models that can be used for training and inference for prototyping purposes. The project began as a collection of fictitious dialogues that can be used to train language models or augment prompts for prototyping and educational purposes. It has now grown to include tooling for LLM application development purposes and open source models. 

![fun_dialogues_logo2](https://github.com/eduand-alvarez/fun-dialogues/assets/57263404/1d8ce401-b595-442f-980c-8ae06ed9d4b2)

# Benchmark Datasets

## Coming soon!

# Models

## GeoFalcon: coming soon!

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
 
## How to Load Dialogues
Loading dialogues can be accomplished using the fun dialogues library or Hugging Face datasets library. 

## Load using fun dialogues

1. Install fun dialogues package
`pip install fundialogues`

2. Use loader utility to load dataset as pandas dataframe. Further processing might be required for use.
```
from fundialogues import dialoader

# load as pandas dataframe
physics_office_hours = dialoader("FunDialogues/academia-physics-office-hours")
```

## Loading using Hugging Face datasets

1. Install datasets package

2. Load using datasets
```
from datasets import load_dataset

physics_office_hours = load_dataset("FunDialogues/academia-physics-office-hours")
```

# Disclaimer

The dialogues contained in this repository are provided for experimental purposes only. It is important to note that these dialogues are assumed to be original work by a human and are entirely fictitious, despite the possibility of some examples including factually correct information. The primary intention behind these dialogues is to serve as a tool for language modeling experimentation and should not be used for designing real-world products beyond non-production prototyping.

Please be aware that the utilization of fictitious data in these datasets may increase the likelihood of language model artifacts, such as hallucinations or unrealistic responses. Therefore, it is essential to exercise caution and discretion when employing these datasets for any purpose.

It is crucial to emphasize that none of the scenarios described in the fun dialogues dataset should be relied upon to provide advice or guidance to humans. These scenarios are purely fictitious and are intended solely for demonstration purposes. Any resemblance to real-world situations or individuals is entirely coincidental.

The responsibility for the usage and application of these datasets rests solely with the individual or entity employing them. By accessing and utilizing these dialogues and all contents of the repository, you acknowledge that you have read and understood this disclaimer, and you agree to use them at your own discretion and risk.

# Disclaimer

The dialogues contained in this repository are provided for experimental purposes only. It is important to note that these dialogues are assumed to be original work by a human and are entirely fictitious, despite the possibility of some examples including factually correct information. The primary intention behind these dialogues is to serve as a tool for language modeling experimentation and should not be used for designing real-world products beyond non-production prototyping.

Please be aware that the utilization of fictitious data in these datasets may increase the likelihood of language model artifacts, such as hallucinations or unrealistic responses. Therefore, it is essential to exercise caution and discretion when employing these datasets for any purpose.

It is crucial to emphasize that none of the scenarios described in the fun dialogues dataset should be relied upon to provide advice or guidance to humans. These scenarios are purely fictitious and are intended solely for demonstration purposes. Any resemblance to real-world situations or individuals is entirely coincidental.

The responsibility for the usage and application of these datasets rests solely with the individual or entity employing them. By accessing and utilizing these dialogues and all contents of the repository, you acknowledge that you have read and understood this disclaimer, and you agree to use them at your own discretion and risk.
