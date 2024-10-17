# Emojify 😎 [10 points]

## Task Overview
Create a command-line tool that encodes and decodes text messages using emojis. This task combines elements of cryptography, Unicode handling, and command-line interface design using the `click` library.

## Objectives
1. Implement a simple substitution cipher using emojis as the cipher alphabet.
2. Create a command-line interface using `click` for encoding and decoding messages.
3. Handle Unicode characters correctly to support a wide range of emojis.

## Requirements
- Python 3.7+
- click library
- emoji library

Install the required packages using:
```
pip install click emoji
```

## Usage
Run the script with the following commands:

Encode a message:
```
python emojify.py encode "Your message here"
```

Decode a message:
```
python emojify.py decode "Your 😎 emoji 😊 message 😍 here"
```

## Specifications
- The tool accepts two main commands: `encode` and `decode`.
- Encoding:
  - Input: A plain text message
  - Output: The message with each letter substituted by a unique emoji
- Decoding:
  - Input: An emoji-encoded message
  - Output: The original plain text message
- The emoji-to-letter mapping is consistent within a session but randomized between runs.
- Supports the 26 letters of the English alphabet (case-insensitive).
- Preserves spaces and punctuation in the original message.

## Bonus Challenges
- Add support for numbers and special characters. [2 points]
- Create a simple GUI to encode and decode using a framework like Tkinter or PyQt [5 points]

Happy emoji-ing! 🚀