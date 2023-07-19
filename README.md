# fun dialogues
A library of fictitious dialogues that can be used to train language models or augment prompts for prototyping and educational purposes. Fun dialogues currently come in json and csv format for easy ingestion or conversion to popular data structures. Dialogues span various topics such as sports, retail, academia, healthcare, and more. The library also includes basic tooling for loading dialogues and will include quick chatbot prototyping functionality in the future.

![fun_dialogues](https://github.com/eduand-alvarez/fun-dialogues/assets/57263404/b4a29056-5220-4299-9a15-50beca4bdc1c)

# Available Dialogues
- Customer Service
  - Grocery Cashier: 100 fictitious examples of dialogues between a customer at a grocery store and the cashier.
- Academia
  - Physics Office Hours: 100 fictitious examples of dialogues between a physics professor and a student during office hours. 
- Healthcare
  - Minor Consultation: 100 fictitious examples of dialogues between a doctor and a patient during a minor medical consultation.
- Sports
  - Basketball Coach: 100 fictitious examples of dialogues between a basketball coach and the players on the court during a game.
 
# How to Load Dialogues
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

## How to Contribute
If you want to contribute to this project and make it better, your help is very welcome. Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### Contributing your own Lifecycle Solution
If you want to contribute to an existing dialogue or add a new dialogue, please open an issue and I will follow up with you ASAP!

### Implementing Patches and Bug Fixes

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called origin.
- Add the original repository as a remote called upstream.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from develop if it exists, else from master.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the component has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's interactive rebase. Create a new branch if necessary.
- Push your branch to your fork on Github, the remote origin.
- From your fork open a pull request in the correct branch. Target the project's develop branch if there is one, else go for master!

If the maintainer requests further changes just push them to your branch. The PR will be updated automatically.
Once the pull request is approved and merged you can pull the changes from upstream to your local repo and delete your extra branch(es).
And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.

# Disclaimer

The dialogues contained in this repository are provided for experimental purposes only. It is important to note that these dialogues are assumed to be original work by a human and are entirely fictitious, despite the possibility of some examples including factually correct information. The primary intention behind these dialogues is to serve as a tool for language modeling experimentation and should not be used for designing real-world products beyond non-production prototyping.

Please be aware that the utilization of fictitious data in these datasets may increase the likelihood of language model artifacts, such as hallucinations or unrealistic responses. Therefore, it is essential to exercise caution and discretion when employing these datasets for any purpose.

It is crucial to emphasize that none of the scenarios described in the fun dialogues dataset should be relied upon to provide advice or guidance to humans. These scenarios are purely fictitious and are intended solely for demonstration purposes. Any resemblance to real-world situations or individuals is entirely coincidental.

The responsibility for the usage and application of these datasets rests solely with the individual or entity employing them. By accessing and utilizing these dialogues and all contents of the repository, you acknowledge that you have read and understood this disclaimer, and you agree to use them at your own discretion and risk.
