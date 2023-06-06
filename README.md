# Telenote Bot


This project offers a solution for saving and managing notes through a Telegram bot. It not only allows you to store your important notes, but also provides an effortless way to send them in other chats. The application is powered by Python and aiogram. 


## Requirements
- Python 3.10
- Telegram bot api token

## Installation

First, you need to clone this repository:

```bash
git clone https://github.com/FominDanil/telenote.git
cd telenote
```

## Configuration
### .env
The application uses environment variables for configuration. Rename `.env.example` to `.env` and fill in the necessary details:

```bash
cp .env.example .env
nano .env
```

- TOKEN: get it from @BotFather

## Usage
```bash
pip install -r requirements.txt
python main.py
```

### Telegramm
1. Send your notes to the bot
![Imgur](https://i.imgur.com/pRnogpU.jpg)

2. While in the chat, write ```@your_bot_name ``` and choose one of the notes
![Imgur](https://i.imgur.com/kLC3hSu.jpg)
3. A message with a note will be sent to the chat on your behalf via the bot
![Imgur](https://i.imgur.com/wTfGSGp.jpg)
