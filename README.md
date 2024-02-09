# AI Chatbot with Text-to-Speech Integration

This simple Python application demonstrates an AI chatbot using the OpenAI API for natural language generation. Additionally, it incorporates text-to-speech functionality using the Eleven Labs API for a more interactive experience.

## Prerequisites

Before running the application, ensure you have the following:

- Python installed on your machine.
- API keys for OpenAI and Eleven Labs (replace placeholders in the code with your actual keys).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install the required Python packages:

   ```bash
   pip install openai requests pygame
   ```

## Usage

1. Open the Python script in your preferred editor (e.g., PyCharm).

2. Replace the placeholder API keys in the code:

   - Replace `'your-api-key-here'` with your OpenAI API key.
   - Replace `'your-api-key-here'` with your Eleven Labs API key.

3. Run the script:

   ```bash
   python chatbot.py
   ```

4. The application window will appear. Enter your text in the input field and click the "Generate" button to initiate a conversation with the AI chatbot.

## Features

- **User Input:** Enter text in the input field to communicate with the AI chatbot.

- **AI Response:** View the AI's response in the application window.

- **Text-to-Speech:** The AI's response is also converted to speech using the Eleven Labs API, and you can listen to the generated audio.

## Notes

- The application uses the OpenAI GPT-3.5-turbo model for chat completions.

- The Eleven Labs API is employed for text-to-speech functionality.

- Pay attention to the API rate limits and terms of service for both OpenAI and Eleven Labs.

- Ensure that you have an internet connection to make API requests.

## Acknowledgments

- This application uses the OpenAI and Eleven Labs APIs to provide advanced natural language processing and text-to-speech capabilities.

Feel free to customize the code and expand the features based on your requirements!
