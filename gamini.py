
import google.generativeai as genai

from IPython.display import display

GOOGLE_API_KEY='AIzaSyChu5_IibibM5R05b8Uwl-NenXa-lpJnlc'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

# 
explaination4= model.generate_content("https://www.youtube.com/watch?v=dj0bk6j9erQ&pp=ygUUMTAgbWluIGVuZ2xpc2ggc3Rvcnk%3D what is in this youtube video in detail?")

print(explaination4.text)