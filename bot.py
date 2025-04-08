
import telebot
import json
import random
import string
from telebot import types

API_KEY = "7669244795:AAFTzXaUt2NiJkU2UVTJdtDuRs4GuL8oJCQ"
bot = telebot.TeleBot(API_KEY)
bot.delete_webhook()

bot_id = 'DEVSUDIPX'
admin_ids = [7967175667, 1234567890]  # Multiple admins supported
channel_username = "@Aizamods"

# Temporary buffer for storing messages
admin_uploads = {}

def get_data(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
        return True
    except:
        return False

def generate_random_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@bot.message_handler(commands=['admin'])
def start_admin_upload(message):
    if message.from_user.id not in admin_ids:
        return
    admin_uploads[message.from_user.id] = []
    bot.send_message(message.chat.id, "✅ Send up to 25 files now. After that, send /done to generate a link.")

@bot.message_handler(commands=['done'])
def finish_upload(message):
    if message.from_user.id not in admin_ids:
        return
    uploaded = admin_uploads.get(message.from_user.id, [])
    if not uploaded:
        bot.send_message(message.chat.id, "❌ You didn't upload any files.")
        return
    code = generate_random_id()
    all_links = get_data(f"{bot_id}-files.json")
    all_links[code] = uploaded
    save_data(f"{bot_id}-files.json", all_links)
    bot.send_message(message.chat.id, f"✅ Your link is ready:\nhttps://t.me/{bot.get_me().username}?start={code}")
    admin_uploads[message.from_user.id] = []  # reset buffer

@bot.message_handler(commands=['start'])
def handle_start(message):
    text = message.text
    if text == "/start":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/Aizamods"))
        markup.add(types.InlineKeyboardButton("✅ Joined", callback_data='join'))
        bot.send_photo(message.chat.id, photo='https://t.me/Bots_Pay_Alert/941',
                       caption=f"<b>👋 Hey! You need to join our channel to use this bot.</b>",
                       reply_markup=markup, parse_mode='HTML')
        return

    user_id = message.from_user.id
    code = text.split("/start ")[-1]
    all_links = get_data(f"{bot_id}-files.json")
    if code in all_links:
        status = bot.get_chat_member(channel_username, user_id).status
        if status not in ["member", "administrator", "creator"]:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/Aizamods"))
            markup.add(types.InlineKeyboardButton("✅ Joined", callback_data='join'))
            bot.send_photo(message.chat.id, photo='https://t.me/Bots_Pay_Alert/941',
                           caption=f"<b>👋 Hey! You need to join our channel to access the files.</b>",
                           reply_markup=markup, parse_mode='HTML')
            return
        for file_id in all_links[code]:
            try:
                bot.copy_message(chat_id=user_id, from_chat_id='-1002565955658', message_id=file_id)
            except:
                continue

@bot.message_handler(content_types=['document', 'video', 'photo', 'audio'])
def handle_media(message):
    if message.from_user.id in admin_ids:
        uploads = admin_uploads.get(message.from_user.id, [])
        if len(uploads) >= 25:
            bot.send_message(message.chat.id, "⚠️ You already uploaded 25 files. Send /done to get the link.")
            return
        msg = bot.copy_message(chat_id='-1002565955658', from_chat_id=message.chat.id, message_id=message.message_id)
        uploads.append(msg.message_id)
        admin_uploads[message.from_user.id] = uploads
        bot.reply_to(message, f"✅ Added file {len(uploads)}/25")
    else:
        bot.reply_to(message, "❌ Only admin can upload files.")

@bot.callback_query_handler(func=lambda call: call.data == 'join')
def check_join(call):
    user_id = call.from_user.id
    status = bot.get_chat_member(channel_username, user_id).status
    if status in ["member", "administrator", "creator"]:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(user_id, "✅ You have joined the channel. Now plz reclick old link for files.")
    else:
        bot.answer_callback_query(call.id, "❌ Please join the channel first!")

bot.infinity_polling()
