from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import os

#logging --> bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

file_path='logs.txt'

def read_text_file(file_path='logs.txt'):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading the file: {str(e)}"

def export(update: Update, context: CallbackContext) -> None:
    try:
        if not os.path.exists(file_path):
            update.message.reply_text(f"Error: The file {file_path} does not exist.")
            return

        with open(file_path, 'rb') as file:
            update.message.reply_document(document=InputFile(file, filename=file_path))
        
        update.message.reply_text(f"The log file {file_path} has been sent successfully.")

    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your AuraMonitor.\nType /logs to get the content of the text file.\n Type /dellogs to delete the content of the log file \n Type /cmds to know all commands.\n')

def logs(update: Update, context: CallbackContext) -> None:
    file_content = read_text_file()

    max_message_length = 4096  
    if len(file_content) > max_message_length:
        for i in range(0, len(file_content), max_message_length):
            update.message.reply_text(file_content[i:i + max_message_length])
    else:
        update.message.reply_text(file_content)

def dellogs(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Your Logs have been deleted!!..')
    with open(file_path,'w') as file: pass

def cmds(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('List of all the commands to this bot')

def main():
    # Replace 'YOUR_API_TOKEN' with your actual bot API token
    updater = Updater("6817585174:AAEfUesnx1mSGlCXS8BRT8w32TLk2-3JD_w")

    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("logs", logs))
    dispatcher.add_handler(CommandHandler("dellogs", dellogs))
    dispatcher.add_handler(CommandHandler("cmds", cmds))
    dispatcher.add_handler(CommandHandler("export", export))

    # Start
    updater.start_polling()
    #exit
    updater.idle()

if __name__ == '__main__':
    main()
