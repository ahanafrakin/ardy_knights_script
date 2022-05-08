import time
import os
import keyboard
import mouse
import random

keep_running = true
esc_pressed = false

# Function to hold down the escape key
def keyboard_press():
    if(keyboard.is_pressed('f6')):
        keep_running = not keep_running
    if(not keep_running):
        keyboard.release('esc')
        esc_pressed=false
    elif(keep_running and not esc_pressed):
        keyboard.press('esc')
        esc_pressed=true


def mouse_clicks():
    if(keep_running):
        # Randomize intervals between press and release (should be pretty short)
        click_length = random.uniform(0.035, 0.065)
        mouse.press(button='left')
        time.sleep(click_length)
        mouse.release(button='left')


if __name__ == "main":
    # Wait before doing click, used my own clicks per second to determine this
    while(true):
        keyboard_press()
        time_between_clicks = random.uniform(0.125, 0.145)
        time.sleep(time_between_clicks)
        mouse_clicks()
        
