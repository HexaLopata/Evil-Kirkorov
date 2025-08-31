# Evil Kirkorov Telegram Bot

This Telegram bot copies all messages from the user with username `@pizdabalabol_bot`.

## Setup

1. **Create a new bot on Telegram:**

   - Message @BotFather on Telegram
   - Send `/newbot` and follow the instructions
   - Copy the bot token you receive

2. **Set the bot token in a .env file:**

   - Copy the example file: `cp .env.example .env`
   - Edit `.env` and replace `your_telegram_bot_token_here` with your actual token:

   ```
   TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or use the automated setup script:

   ```bash
   ./setup.sh
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## How it works

- The bot listens to all messages in any chat it's added to
- When it detects a message from the user `@pizdabalabol_bot`, it immediately copies that message to the same chat
- The bot uses the latest python-telegram-bot library (v20.8) with async/await support

## Usage

1. Add your bot to a group or channel where `@pizdabalabol_bot` sends messages
2. Make sure your bot has permission to read messages and send messages
3. The bot will automatically copy any message from `@pizdabalabol_bot`

## Notes

- The bot needs to be added to the same chat/group where the target user sends messages
- Make sure the bot has appropriate permissions in the chat
- The bot will copy all types of messages (text, images, files, etc.)
