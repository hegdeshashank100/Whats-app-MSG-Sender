import pywhatkit as kit
import pyautogui
import time
import datetime

# Function to validate phone number
def validate_phone_number(number):
    if number.isdigit() and len(number) > 10:
        return True
    else:
        return False

# Input recipient's phone number
phone_number = input("Enter the recipient's phone number (with country code, e.g., 919876543210): ")

# Validate phone number
if not validate_phone_number(phone_number):
    print("Invalid phone number! Ensure it includes the country code and has no spaces or symbols.")
else:
    # Input the message
    message = input("Enter the message you want to send: ")

    # Schedule the message (2 minutes ahead of current time)
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute + 2

    # Adjust for overflow of minutes
    if minutes >= 60:
        minutes -= 60
        hours += 1

    # Send the message
    try:
        print("Preparing to send the WhatsApp message...")
        kit.sendwhatmsg(f"+{phone_number}", message, hours, minutes)

        # Wait a few seconds for WhatsApp Web to open and load
        time.sleep(15)

        # Press Enter to send the message
        print("Sending the message...")
        pyautogui.press("enter")
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
