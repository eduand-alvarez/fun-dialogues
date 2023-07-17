import json
import pandas as pd

def load_dialogue(category, dialogue):
    """ facilitates the loading of available fictitous dialogues as pandas dataframes

    Parameters
    ----------
    category : str
        dialogue category, currently support 'academia', 'customer_service', 'healthcare', and 'sports'
    dialogue : str
        dialogue name from category

    Returns
    -------
    pd.DataFrame
        returns pandas dataframe with columns = ['id', 'description', 'dialogue']
    """
    with open(f'../dialogues/{category}/{dialogue}.json') as file:
        data = json.load(file)

    dialogues = data[f'{dialogue}']

    # Create a pandas dataframe
    df = pd.DataFrame(dialogues, columns=['id', 'description', 'dialogue'])

    return df