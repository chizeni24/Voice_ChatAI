from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from .email_sender import send_email

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = '/home/surfer/Downloads/gen-lang-client-0481563702-4c1d9d239b5f.json'
CALENDAR_ID = "CALENDAR_ID"

def get_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=credentials)

def book_appointment(summary, description, start_datetime, end_datetime, recipient_email, conversation_summary):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'America/New_York',
        },
    }

    try:
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')
        
        # Send email with conversation summary and calendar link
        email_subject = f"Your Bayou Movers Appointment: {summary}"
        email_sent = send_email(recipient_email, email_subject, conversation_summary, event.get("htmlLink"))
        
        if email_sent:
            print(f"Email sent successfully to {recipient_email}")
        else:
            print(f"Failed to send email to {recipient_email}")
        
        return event
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def extract_appointment_details(content):
    import re
    from datetime import datetime, timedelta

    date_match = re.search(r'schedule your move for (\w+ \d+, \d{4}) at (\d{1,2}:\d{2} [AP]M)', content, re.IGNORECASE)
    if date_match:
        date_str, time_str = date_match.groups()
        start_datetime = datetime.strptime(f'{date_str} {time_str}', '%B %d, %Y %I:%M %p')
        end_datetime = start_datetime + timedelta(hours=2)  # Assume 2-hour duration

        # Extract email (this is a simple example, adjust based on your actual content structure)
        email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
        email = email_match.group(0) if email_match else None

        return {
            'summary': 'Bayou Movers - Moving Appointment',
            'description': content,
            'start_datetime': start_datetime,
            'end_datetime': end_datetime,
            'recipient_email': email,
        }
    return None