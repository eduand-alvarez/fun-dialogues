import os
import csv
from PyPDF2 import PdfReader

def extract_data_from_pdfs(folder_path: str):
    """
    Extract text data from all PDF files located in a specified folder.

    Parameters
    ----------
    folder_path : str
        The path to the folder containing PDF files to be processed.

    Returns
    -------
    dict
        A dictionary where each key is the filename of a PDF file and the corresponding value is the extracted text content of that file.

    """
    data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            reader = PdfReader(file_path)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + ' '  # Assuming space as delimiter between pages
            data[filename] = text
    return data

def clean_and_structure_data(data: dict):
    """
    Clean and structure the extracted data from PDF files.

    This function replaces newline characters with spaces and strips leading and trailing spaces.

    Parameters
    ----------
    data : dict
        A dictionary where each key is a filename and each value is the raw text extracted from the corresponding PDF file.

    Returns
    -------
    dict
        A dictionary with the same keys as the input but with cleaned and structured text as values.

    """
    cleaned_data = {filename: text.replace('\n', ' ').strip() for filename, text in data.items()}
    return cleaned_data

def generate_output_files(data: str, output_directory: str, output_type:str ='txt', chunk_size: int = 1000, chunk_distance: int = 0):
    """
    Generate output files from the structured data, including a comprehensive data file,
    a data start tracker file, and chunked data files with an additional column for the source PDF.

    Parameters
    ----------
    data : dict
        The structured data to be written to output files, where each key is a filename and each value is the cleaned text.
    output_directory : str
        The directory where output files will be saved.
    output_type : str, optional
        The type of the comprehensive data file to generate ('txt' or 'csv'). Default is 'txt'.
    chunk_size : int, optional
        The number of characters each chunk should contain. Default is 1000.
    chunk_distance : int, optional
        The distance between chunks. A negative value creates overlap; a positive value creates gaps. Default is 0.

    """

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    comprehensive_data_filename = os.path.join(output_directory, 'comprehensive_data.' + output_type)
    start_tracker_filename = os.path.join(output_directory, 'data_start_tracker.csv')
    chunk_data_filename = os.path.join(output_directory, 'chunked_data.csv')

    with open(comprehensive_data_filename, 'w', encoding='utf-8') as comp_file, \
         open(start_tracker_filename, 'w', newline='', encoding='utf-8') as start_file, \
         open(chunk_data_filename, 'w', newline='', encoding='utf-8') as chunk_file:

        start_writer = csv.writer(start_file)
        start_writer.writerow(['Filename', 'Start Line'])

        chunk_writer = csv.writer(chunk_file)
        chunk_writer.writerow(['Chunk ID', 'Chunk Content', 'Source PDF'])  # Add 'Source PDF' column

        line_counter = 1
        chunk_id = 1

        for filename, text in data.items():
            comp_file.write(text + '\n')
            start_writer.writerow([filename, line_counter])
            line_counter += text.count('\n') + 1

            # Chunking logic
            i = 0
            while i < len(text):
                chunk_end = i + chunk_size
                if chunk_distance < 0:  # Overlap
                    chunk_end += chunk_distance
                chunk = text[i:chunk_end].strip()
                chunk_writer.writerow([chunk_id, chunk, filename])  # Include filename in the row
                i += chunk_size - abs(chunk_distance) if chunk_distance < 0 else chunk_size
                chunk_id += 1

# Full Execution
def judgypdf(folder_path: str, output_directory: str, output_type:str ='csv', chunk_size:int = 1000, chunk_distance: int =0):
    """
    The main function to process PDF files from a folder, clean and structure the data, and generate output files.

    Parameters
    ----------
    folder_path : str
        The path to the folder containing the PDF files to process.
    output_directory : str
        The directory where the output files will be saved.
    output_type : str, optional
        The format of the comprehensive data file ('txt' or 'csv'). Default is 'csv'.
    chunk_size : int, optional
        The number of characters each data chunk should contain. Default is 1000.
    chunk_distance : int, optional
        The distance between data chunks. Negative for overlap, positive for gaps. Default is 0.

    """

    print("Starting PDF Processing")
    data = extract_data_from_pdfs(folder_path)
    cleaned_data = clean_and_structure_data(data)
    generate_output_files(cleaned_data, output_directory, output_type, chunk_size, chunk_distance)
    print("PDF Processing Complete!")

