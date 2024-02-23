import pandas as pd
import re

def process_qa(qa, knowledge_chunk):
    """
    Processes a question and answer (QA) string to extract structured information and populates a DataFrame.

    Parameters
    ----------
    qa : str
        The QA string containing the question, options (a, b, c, d), and the correct answer.
    knowledge_chunk : str
        The knowledge content associated with the QA that will be used as context or reference.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the following columns:
        - 'Knowledge Chunk': The provided knowledge chunk as context.
        - 'QA Text': A structured text combining the question and all options.
        - 'Correct Answer': The letter (a, b, c, or d) indicating the correct option.

    Notes
    -----
    The function attempts to clean the QA string by removing instructional text, splits the content into 
    components (question, options, and correct answer), and validates the extracted answer key. If any step 
    fails or the answer key is not valid, the corresponding fields in the returned DataFrame are set to None.

    Raises
    ------
    Exception
        If an error occurs during the processing, an error message is printed, and a DataFrame with null values 
        is returned instead of raising an exception.
    """

    # Initializing a DataFrame with null values
    df = pd.DataFrame({
        'Knowledge Chunk': [knowledge_chunk],
        'QA Text': [None],
        'Correct Answer': [None]
    })
    
    # Removing the instructional text
    qa_cleaned = re.sub(r'\[INST\].*?\[/INST\]', '', qa, flags=re.DOTALL).strip()
    
    try:
        # Splitting the cleaned text based on the structured format
        parts = re.split(r'\na\) |\nb\) |\nc\) |\nd\) |\nCorrect answer: ', qa_cleaned)
        question = parts[0].replace('question: ', '').strip()
        options_a = parts[1].strip()
        options_b = parts[2].strip()
        options_c = parts[3].strip()
        options_d = parts[4].strip()
        answer_key = parts[5].strip().split(' ')[0]  # Extracting the last word, assuming it's the answer key
        answer_key = answer_key[0]

        # Validating the answer_key
        if answer_key not in ['a', 'b', 'c', 'd']:
            answer_key = None  # Setting to None if not valid

        # Formatting the QA text to include question and options
        qa_text = f"{question} Options: a) {options_a}, b) {options_b}, c) {options_c}, d) {options_d}"
        
        # Updating the DataFrame with extracted or validated values
        df.at[0, 'QA Text'] = qa_text
        df.at[0, 'Correct Answer'] = answer_key
    except (IndexError, AttributeError):
        # If extraction or validation fails, the function will return the DataFrame with null values as initialized
        print("QA extraction or validation failed. Please Review Output File and Log.")
    
    return df