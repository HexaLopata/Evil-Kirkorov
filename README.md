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

4. **Run the bot:**
   ```bash
   python main.py
   ```
