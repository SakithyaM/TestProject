from google import genai
from google.genai import types
import pathlib

client = genai.Client(api_key="GEMINI_API_KEY")

filepath = pathlib.Path('data.pdf')
prompt = "What are the benefits of this competition?"
response = client.models.generate_content(
 model="gemini-2.5-flash",
 contents=[
 types.Part.from_text(text=f"Name : Amal, Age : 24, Study Degree :
BSc Honours in Business Information Systems, Undergraduate"
 "write self introduction paragraph using these details"),
 ]
)
print(response.text)