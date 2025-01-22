# AI Voice Chat - Bayou Movers Assistant

An AI-powered voice assistant system built for Bayou Movers to handle customer inquiries and schedule moving services. The system uses OpenAI's GPT model and Twilio's voice services to provide a natural conversation experience.

## Features

- Real-time voice interaction using OpenAI's GPT model
- Automated customer service for moving inquiries
- Information gathering for moving estimates
- Integration with Twilio for voice calls
- Email notification system with Gmail integration
- Google Calendar integration for scheduling appointments

## Prerequisites

- Python 3.8+
- OpenAI API key
- Twilio account and phone number
- Gmail account (for email notifications)
- Google Cloud account (for Calendar integration)
- ngrok (for local development)

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   .\venv\Scripts\activate   # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### 1. Environment Variables
Create a `.env` file in the project root:
```
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# Server Configuration
PORT=5050

# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# Gmail Configuration (Choose one method)
# Method 1: App Password
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=your_app_password

# Method 2: OAuth2
GMAIL_USER=your.email@gmail.com
GOOGLE_OAUTH_CREDENTIALS=path_to_credentials.json

# Google Calendar Configuration
GOOGLE_CALENDAR_CREDENTIALS=path_to_calendar_credentials.json
CALENDAR_ID=your_calendar_id
```

### 2. Twilio Setup

1. Create a Twilio account at [Twilio's website](https://www.twilio.com)
2. Purchase a phone number from Twilio
3. Get your Account SID and Auth Token from the Twilio Console
4. Configure your Twilio phone number:
   - Go to Phone Numbers → Manage → Active numbers
   - Click on your number
   - Under "Voice & Fax" section:
     - Set "A Call Comes In" to "Webhook"
     - Set the webhook URL to `https://your-domain/incoming-call`
     - Set the HTTP method to POST

### 3. Gmail Setup (Choose one method)

#### Method 1: App Password (Simpler)
1. Enable 2-Step Verification in your Google Account
2. Go to Security → App passwords
3. Select "Mail" and your device
4. Use the generated 16-character password in your .env file

#### Method 2: OAuth2 (More Secure)
1. Go to Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials and save as `credentials.json`

### 4. Google Calendar Setup
1. Go to Google Cloud Console
2. Enable Google Calendar API
3. Create Service Account credentials
4. Download JSON key file
5. Share your calendar with the service account email

## Running the Application

1. Start ngrok (for local development):
   ```bash
   ngrok http 5050
   ```
   Copy the HTTPS URL provided by ngrok.

2. Update Twilio webhook URL:
   - Go to Twilio Console → Phone Numbers → Your Number
   - Set webhook URL to: `https://your-ngrok-url/incoming-call`

3. Start the server:
   ```bash
   python main.py
   ```
   The server will start on port 5050 (or the port specified in your .env file)

4. Test the system:
   - Call your Twilio phone number
   - The call should connect to your AI assistant
   - The assistant will handle the conversation
   - Appointments will be added to Google Calendar
   - Email confirmations will be sent via Gmail

## Project Structure

- `main.py` - FastAPI server and WebSocket handlers for voice processing
- `email_sender.py` - Email notification system using Gmail
- `google_calendar.py` - Google Calendar integration for appointment scheduling
- `config/` - Configuration files and templates
- `requirements.txt` - Python package dependencies
- `.env` - Environment variables (not tracked in git)

## Troubleshooting

1. **Twilio Connection Issues**
   - Verify your ngrok tunnel is running
   - Check Twilio webhook URL is correct
   - Ensure your server is running and accessible

2. **Email Sending Failures**
   - Verify Gmail credentials are correct
   - Check spam folder for test emails
   - Ensure less secure app access or App Password is properly set up

3. **Calendar Integration Issues**
   - Verify service account has proper permissions
   - Ensure calendar is shared with service account email
   - Check credential file path is correct

## Security Considerations

- Store all credentials in .env file (never commit to version control)
- Use HTTPS for all external communications
- Implement rate limiting for production use
- Regularly rotate API keys and credentials
- Use OAuth2 where possible for enhanced security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Support

For support, please [create an issue](your-repository-url/issues) or contact the maintainers. 