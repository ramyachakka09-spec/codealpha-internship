# Simple Python Chatbot

## Overview

This is a simple rule-based chatbot built using Python. The chatbot responds to a few predefined user inputs and continues the conversation until the user types **"bye"**.

## Features

- Responds to basic greetings.
- Answers "How are you?".
- Ends the conversation when the user types "bye".
- Handles unknown inputs with a default response.
- Easy to understand and modify for beginners.

## Technologies Used

- Python 3

## Project Structure

```
.
├── chatbot.py
└── README.md
```

## How It Works

The chatbot checks the user's input against predefined conditions.

Supported commands:

| User Input | Bot Response |
|------------|--------------|
| hello | Hi! |
| how are you | I'm fine, thanks! |
| bye | Goodbye! |
| Any other input | Sorry, I don't understand. |

## Installation

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.

## Running the Chatbot

Run the following command:

```bash
python chatbot.py
```

## Example Output

```
Chatbot started. Type 'bye' to quit.

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: what's your name?
Bot: Sorry, I don't understand.

You: bye
Bot: Goodbye!
```

## Code Explanation

### `chatbot_response(user_input)`

- Converts the input to lowercase.
- Checks for predefined messages.
- Returns the appropriate response.

### `run_chatbot()`

- Starts the chatbot.
- Accepts user input continuously.
- Displays the chatbot's response.
- Exits when the user enters `bye`.

## Future Improvements

- Add more conversational responses.
- Support partial matches (e.g., "Hi there").
- Use Natural Language Processing (NLP).
- Store conversation history.
- Build a graphical user interface (GUI).
- Connect the chatbot to a database or web application.

## Author

Created as a beginner Python chatbot project.