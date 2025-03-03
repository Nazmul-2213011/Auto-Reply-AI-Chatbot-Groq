import pyautogui
import pyperclip
import time

# Wait a moment to switch to the correct screen
time.sleep(2)

# Click on the icon at position (882, 1062)
pyautogui.click(882, 1062)

# Wait for any UI response
time.sleep(1)

# Click and drag to select text from (751, 213) to (851, 913)
pyautogui.moveTo(751, 213)
pyautogui.mouseDown()
pyautogui.moveTo(851, 913, duration=0.5)
pyautogui.mouseUp()

# Copy the selected text to clipboard using Ctrl + C
pyautogui.hotkey('ctrl', 'c')

# Wait for clipboard to update
time.sleep(1)

# Retrieve and print the copied text
copied_text = pyperclip.paste()
print("Copied Text:", copied_text)

# Deselect the text by clicking outside the selection
pyautogui.click(830,210)
