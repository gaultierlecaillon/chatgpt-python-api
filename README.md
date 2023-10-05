# chatgpt-python-api

This repository contains a Python script to interact with OpenAI's ChatGPT via the API. It sends a prompt from the user to the ChatGPT API and outputs the model's response.

## Requirements

- Python 3.6+
- requests
- python-dotenv

## Installation

1. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
2. **Set Up the API Key**
    - Create a `.env` file in the project root.
    - Add your API key:
        ```
        OPENAI_API_KEY=your_api_key_here
        ```
3. **Run the Script**
    ```bash
    python script_name.py
    ```

## Usage

Once you run the script, it will prompt you to enter a message. The message will be sent to ChatGPT and the response will be printed to the console.

```plaintext
What would you like to ask GPT-4? [Your message here]
GPT-4 says: [Response from GPT-4]
