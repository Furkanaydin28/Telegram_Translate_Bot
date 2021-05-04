from telegram.ext import *
from selenium import webdriver

API_KEY = '#your telegram bot token'

def get_Data(url_path,sl,tl):
    browser = webdriver.Chrome()
    url = f"https://translate.google.com/?hl=tr&sl={sl}&tl={tl}&text={url_path}&op=translate"
    browser.get(url)
    elements = browser.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
    result = elements.text
    browser.close()
    return result

def start_command(update, context):
    user = update.message.from_user
    update.message.reply_text(f""" Hello {user['first_name']} Welcome to Translate Bot. Command For /help""")

def help_command(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Hello {user['first_name']}, Commands
/entotr sometext Translate English to Turkish
/trtoen sometext Translate Turkish to English""")

def translateEn_to_Tr(update, context):
    text = update.message.text
    text = str(text)
    text = text.replace("/entotr", "")
    text = text.replace(" ", "%20")
    result = get_Data(text,"en","tr")
    update.message.reply_text(result)

def translateTr_to_En(update, context):
    text = update.message.text
    text = str(text)
    text = text.replace("/trtoen", "")
    text = text.replace(" ", "%20")
    result = get_Data(text,"tr","en")
    update.message.reply_text(result)

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("entotr", translateEn_to_Tr))
    dp.add_handler(CommandHandler("trtoen", translateTr_to_En))

    updater.start_polling()
    updater.idle()

main()
