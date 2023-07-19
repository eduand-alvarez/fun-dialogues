from datasets import load_dataset
import pandas as pd

def dialoader(dataset):
    """ facilitates the loading of available fictitous dialogues from hugging face hub as pandas dataframes

    Parameters
    ----------
    dataset : str
        dataset identifier from hugging face dataset hub ex: "FunDialogues/academia-physics-office-hours"

    Returns
    -------
    pd.DataFrame
        returns pandas dataframe with columns = ['id', 'description', 'dialogue']
    """
    
    dataset = load_dataset(dataset)
    dialogues = dataset['train']

    # Create a pandas dataframe
    df = pd.DataFrame(dialogues, columns=['id', 'description', 'dialogue'])

    return df
