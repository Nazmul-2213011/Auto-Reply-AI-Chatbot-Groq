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
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def automate_reply():
    # Initial click to activate the area
    pyautogui.click(847, 1046)
    time.sleep(1)

    while True:
        # Select and copy text
        pyautogui.moveTo(720, 172)
        pyautogui.mouseDown()
        pyautogui.moveTo(726, 785)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        copied_text = pyperclip.paste()
        print("Copied Text: ", copied_text)

        # Get response
        response = get_groq_response(copied_text)

        # Paste response
        pyautogui.click(775, 900)
        pyautogui.typewrite(response[:100], interval=0.1)

        # Submit reply
        pyautogui.click(1414, 959)

        # Delay only after submission
        time.sleep(5)

if __name__ == "__main__":
    automate_reply()
