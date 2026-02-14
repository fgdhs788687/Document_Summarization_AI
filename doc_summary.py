from ollama import chat, ChatResponse
import requests 
import PyPDF2
import pandas as pd
from bs4 import BeautifulSoup
import os 

# function to read the web page and extract the text from it. It will return the text of the page as a string.
def read_web(link):
    page = requests.get(link).text 
    soup = BeautifulSoup(page, 'html.parser')
    paragraphs = soup.find_all('p')
    page_text = ''
    for line in paragraphs:
        page_text += line.text 
    return page_text

# function to read the pdf file and extract the text from it.
def read_pdf(link):
    text = ''
    with open(link, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text        

# function to read the txt file and extract the text from it.
def read_txt(link):
    with open(link, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# function to read the csv file and extract the text from it. It will return the text of the file as a string.
def read_csv(link):
    df = pd.read_csv(link)
    text = df.to_string()
    return text

# function to summarize the text using the AI model. It will return the summary of the text as a string.
def summarize(text):
    query = f'''
    Summarize the following text in 200 words or less:

    {text}
    '''
    response: ChatResponse = chat(model='gemma3:1b', messages=[
        {'role': 'user', 'content': query}
    ])
    return response.message.content.strip()

# This is the main function that will run the program. 
def main():
    print('AI Document Summarization')
    print('Supported formats: PDF, TXT, CSV, HTML or web URL')
    print('Make sure the file paths are not within the quotes and are correct')
    print('Type exit() to quit')

    while True:
        link = input('URL/File Path: ').strip('"') # This will remove any leading or trailing quotes from the input.
        if link.lower() == 'exit()':
            print('Exiting...')
            os.system('cls') # Clear the console or terminal in windows. 
            with open('History.html', 'w', encoding='utf-8') as file:
                file.write("") # This will clear the content of the History.html file.
            quit()

        try:
            if link.startswith('http'):
                text = read_web(link)  
            elif link.endswith('pdf'):
                text = read_pdf(link)
            elif link.endswith('txt'):
                text = read_txt(link)
            elif link.endswith('csv'):
                text = read_csv(link)
            else:
                print('Unsupported format. Please provide a valid URL or file path.')
                # continue

            if not text.strip():
                print('No text found in the document or web server.')
                continue
            else:
                print('Generating summary...')
                summary = summarize(text)
                print('\nSummary:\n', summary) 
                print('*' * 50, '\n')
            with open('History.html', 'a', encoding='utf-8') as file:
                file.write(f'''
                <article>
                    <h2>{link}</h2>
                    <p>{summary}</p>
                    <hr>
                </article>
                ''')
        except Exception as e:
            print(f'Error reading the document: {e}')    
     
# This will run the main function when the script is executed.
if __name__ == "__main__":
    main()