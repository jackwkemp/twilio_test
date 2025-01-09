# Twilio Testing

This project is an example of integrating the Twilio API with a simple Flask application to send SMS messages. The goal was to test a new service provider for sending outbound SMS messages in a use case involving private hire vehicle drivers.

## Features:
- **Twilio API Integration**: Connects to Twilio for sending SMS.
- **Flask Application**: Simulates how the SMS service could be integrated into an existing system.
- **Test Environment**: Designed for sending messages to drivers based on certain conditions (e.g., high cancellations).

## Files:
- **`twilio.py`**: Python script connecting to the Twilio API.
- **`twilio_beta.py`**: A test script for experimenting with SMS sending.
- **`index.html`**: A simple interface for interacting with the Flask app.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install flask twilio`.
3. Set up your Twilio account and configure the necessary API keys.
4. Run the Flask app: `python twilio_beta.py`.

## Usage
This script allows you to send SMS messages to a list of phone numbers via the Twilio API.


