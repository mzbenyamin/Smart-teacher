import os
from telegram.ext import Application
from dotenv import load_dotenv
from src.handlers import setup_handlers

load_dotenv()

def main():
    application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
    setup_handlers(application)
    application.run_polling()

if __name__ == "__main__":
    main()
