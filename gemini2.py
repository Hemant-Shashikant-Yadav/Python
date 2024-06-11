import threading
import textwrap

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY='AIzaSyChu5_IibibM5R05b8Uwl-NenXa-lpJnlc'

genai.configure(api_key=GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)


def generate_content(model, prompt, result_container):
    response = model.generate_content(prompt)
    result_container.append(response.text)


model = genai.GenerativeModel('gemini-pro')

prompts = [
    "Generate a list of 10 car names.",
    "Generate a list of 10 bike names.",
    "Generate a list of 10 flowers names.",
    "Generate a list of 10 smartphone names."
]  # List of prompts for each thread
results = []

threads = []
for prompt in prompts:
    result_container = []
    thread = threading.Thread(target=generate_content, args=(model, prompt, result_container))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for result in results:
    print(to_markdown(result))
