import os
import requests

def translate(text, source_language, target_language):
    API_ENDPOINT = 'https://api.mymemory.translated.net/get'

    params = {
        'q': text,
        'langpair': f"{source_language}|{target_language}"
    }

    response = requests.get(API_ENDPOINT, params=params)
    response_json = response.json()
    return response_json['responseData']['translatedText']

# Create the "data" directory if it does not exist:
if not os.path.exists('data'):
    os.makedirs('data')

# Create the "out" directory if it does not exist:
if not os.path.exists('out'):
    os.makedirs('out')

# Create the input file if it does not exist:
if not os.path.exists('data/input.txt'):
    with open('data/input.txt', 'w') as input_file:
        input_file.write('')

# Read the text to be translated from the input file:
with open('data/input.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Prompt the user to enter the target language:
target_language = input("Enter the target language (e.g., 'fr' for French, 'ru' for Russian): ")

# Translate the text:
source_language = 'en'
translated_text = translate(text, source_language, target_language)

# Create the output file if it does not exist:
if not os.path.exists('out/output.txt'):
    with open('out/output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(translated_text)

# Write the translated text to the output file:
with open('out/output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(translated_text)

print("Translation successful! Check the 'out' folder for the translated text.")
