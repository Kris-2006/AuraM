# AuraM

## Overview

This project demonstrates a keylogger implementation that captures user keystrokes and logs them to a server. The server processes the logs and provides access to authorized users through a Telegram bot. 

---

## Features

- **Keylogger**: Captures keystrokes on a target system.
- **Server Communication**: Sends logged data to a remote server securely.{which needs to be configured manually}
- **Telegram Bot Integration**: Provides real-time access to logs for authorized users via a Telegram bot.
- **Scapy Integration**: Utilized for network-related functionalities, such as packet manipulation and analysis.

---

## Project Structure

keylogger-project/ 
│ ├── keylogger/ 
│       └── keylogger.py
│       └── interface.py        
│ ├── server
│       ├── server.py 
│       └── bot.py 
├── requirements.txt  
├── README.md  



## Requirements

To run the project, install the following Python libraries:

- [Scapy](https://scapy.net/) for network packet manipulation and analysis.
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/) for interacting with Telegram's API.
- [Pynput](https://pynput.readthedocs.io/) for monitoring keyboard inputs.

You can install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt

-----


> **Disclaimer**: This project is for educational purposes only and should be used in controlled environments with explicit permission. Unauthorized use of keyloggers is illegal and unethical.
