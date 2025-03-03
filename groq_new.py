import pyautogui
import time
import os
from groq import Groq
from dotenv import load_dotenv
import pyperclip  # Clipboard handling

# Load environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=api_key)

def get_groq_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": user_input,
        }],
        model="llama3-8b-8192",  # Make sure the model ID is correct
    )
    response = chat_completion.choices[0].message.content.strip()
    
    # Ensure the response ends with a dot and is one line
    if response and not response.endswith('.'):
        response = response + '.'

    # Clean up any trailing words after a dot
    if '.' in response:
        # Find the first period and cut off everything after it
        response = response.split('.')[0] + '.'

    # Remove newlines and return the response as one line
    return response.replace('\n', ' ').replace('\r', '')

def automate_reply():
    # Initial click to activate the area
    pyautogui.click(847, 1046)
    time.sleep(1)

    while True:
        # Select and copy text from the screen
        pyautogui.moveTo(720, 172)
        pyautogui.mouseDown()
        pyautogui.moveTo(726, 785)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')