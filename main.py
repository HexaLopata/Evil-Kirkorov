import logging
import os
import re

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def split_text(text):
    # Split by whitespace and punctuation (keeping the punctuation)
    return re.findall(r"\w+|[^\w\s]", text)


async def copy_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Copy messages from the target user."""
    if update.message:
        if not update.message.text:
            return
        try:
            if "да" == split_text(update.message.text.lower())[-1]:
                await update.message.reply_text("Золотые слова!")
                return

            if "нет" == split_text(update.message.text.lower())[-1]:
                await update.message.reply_text("Крутого мужика ответ!")
                return
        except Exception as e:
            logger.error(f"Error copying message: {e}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by Updates."""
    logger.error(f"Update {update} caused error {context.error}")


def main() -> None:
    """Start the bot."""
    # Get bot token from .env file
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("Please set the TELEGRAM_BOT_TOKEN in the .env file")
        print("Create a .env file and add: TELEGRAM_BOT_TOKEN=your_token_here")
        print("You can get a token by messaging @BotFather on Telegram")
        return

    # Create the Application
    application = Application.builder().token(token).build()

    # Add message handler to copy messages from target user
    application.add_handler(MessageHandler(filters.ALL, copy_message))

    # Add error handler
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    print("Press Ctrl+C to stop the bot")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
