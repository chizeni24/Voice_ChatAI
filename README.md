# AI Voice Chat - Bayou Movers Assistant

An AI-powered voice assistant system built for Bayou Movers to handle customer inquiries and schedule moving services. The system uses OpenAI's GPT model and Twilio's voice services to provide a natural conversation experience.

## Features

- Real-time voice interaction using OpenAI's GPT model
- Automated customer service for moving inquiries
- Information gathering for moving estimates
- Integration with Twilio for voice calls
- Email notification system
- Google Calendar integration for scheduling

## Prerequisites

- Python 3.8+
- OpenAI API key
- Twilio account and credentials
- Google Calendar API credentials (for scheduling features)

## Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PORT=5050
   # Add other required credentials
   ```

## Project Structure

- `main.py` - Main application file containing the FastAPI server and WebSocket handlers
- `email_sender.py` - Email notification system
- `google_calendar.py` - Google Calendar integration for scheduling
- `config/` - Configuration files and templates
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not tracked in git)

## Running the Application

1. Ensure all environment variables are set
2. Start the server:
   ```bash
   python main.py
   ```
   The server will start on port 5050 (or the port specified in your .env file)

## Features

### Voice Assistant (Jones)
- Handles customer inquiries about moving services
- Collects essential information:
  - Customer contact details
  - Moving locations
  - Service type requirements
  - Scheduling preferences
  - Special item handling needs
- Provides service information and pricing structure
- Escalates complex queries to human representatives

### Technical Features
- Real-time audio streaming
- Speech-to-text and text-to-speech conversion
- WebSocket communication
- Interrupt handling for natural conversation flow
- Session management
- Error handling and logging

## Security

- API keys and sensitive credentials are stored in environment variables
- Secure WebSocket connections
- Input validation and sanitization

## Contributing

Please follow the standard pull request process for contributions.

## License

[Add your license information here] 