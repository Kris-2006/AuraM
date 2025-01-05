# AuraM  

## Overview

This project demonstrates a keylogger implementation that captures user keystrokes and logs them to a server. The server processes the logs and provides access to authorized users through a Telegram bot. 

> **Disclaimer**: This project is for educational purposes only.
---

## Features

- **Keylogger**: Captures keystrokes on a target system.
- **Server Communication**: Sends logged data to a remote server securely.
- **Telegram Bot**: Provides real-time access to logs for authorized users via a Telegram bot.
- **Scapy Integration**: Utilized for network-related functionalities, such as packet manipulation and analysis.

---

## Project Structure

```
keylogger-project/
│
├── keylogger/                  
│   └── keylogger.py            
│   └── keylogger.py            
├── server/                     
│   ├── server.py               
│   └── telegram_bot.py         
│
├── requirements.txt            
└── README.md                     
```

---

## Requirements

To run the project, install the following Python libraries:

- [Scapy](https://scapy.net/) for network packet manipulation and analysis.
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/) for interacting with Telegram's API.
- [Pynput](https://pynput.readthedocs.io/) for monitoring keyboard inputs.

You can install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kris-2006/AuraM.git
   cd AuraM
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```



3. Run the server and bot:
    Make sure you set the addresses to host-server{eg \: AWS,GCP}.
    The Telegram bot is defaulted to read from local system . so if you plan to host it in another make sure you extend the functionality..
   ```bash
   python server/server.py
 
    ```
   ```bash
   python server/bot.py
   
   ``` 

---

## Settings 
- The Settings are preconfigured to send requests to localhost.
- In interface.py the script executes the keylogger as an executable file.
- Install winNcap driver for windows to enable packet sniffing.


### Telegram Bot
- Users can interact with the Telegram bot to access captured logs in real-time.
- Example commands:
  - `/start` - Start the bot interaction.
  - `/get_logs` - Retrieve the latest logs.
  - `/dellogs` - To delete the logs 

---




> **Disclaimer**: This project is for educational purposes only.

---
