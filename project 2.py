
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials
account_sid = '*************************'
auth_token = '**************************'

client = Client(account_sid, auth_token)

# Function to send WhatsApp message
def send_whatsapp_message(recipient_number, message_body):
    try:
        # Sending the message
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio Sandbox WhatsApp number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
        print(f'Message status: {message.status}')  # Print the message status for debugging
    except Exception as e:
        print(f'An error occurred: {e}')  # Print detailed error message

# User input
name = input("Enter the recipient name: ")
recipient_number = input("Enter the recipient WhatsApp number with country code (e.g., +1234): ")
message_body = input(f"Enter the message you want to send to {name}: ")

# Date and time input
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")

    # Wait until the scheduled time
    time.sleep(delay_seconds)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)
