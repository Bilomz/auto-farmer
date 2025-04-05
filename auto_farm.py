import pyautogui
import time

# Set a reasonable interval between key presses (in seconds)
interval = 0.5
key_to_press = 'space'  # Key to press

while True:
    pyautogui.press(key_to_press)  # Simulate pressing the space key
    print(f"Pressed '{key_to_press}' to farm!")
    print("Left mouse click simulated!")
    
    time.sleep(interval)  # Wait for the interval before clicking again
