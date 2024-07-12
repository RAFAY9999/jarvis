import google.generativeai as genai
import os

def get_api_key():
  """
  Returns your Gemini API key (replace with your actual key).
  """
  return "YOUR_API_KEY"  # Replace with your actual API key (less secure)

try:
  # Attempt to configure with the hardcoded key in the function
  genai.configure(api_key=get_api_key())
except Exception as e:  # Catch any potential errors during configuration
  print(f"Error configuring API: {e}")
  exit(1)  # Exit the script with an error code

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("what is coding")
print(response.text)