import telebot
from telebot import types

bot_token = "7406063194:AAFcc3LpqIvhG-pii4lSKJobGPtxLcMJqu4"
bot = telebot.TeleBot(bot_token)

zip_file_ids = [
    "BQACAgQAAxkBAAM0Z_b7iLeEOBogKlKKdDSHn8QgS7UAAgsPAAJ2EmhR_flgf_6OgJk2BA",
    "BQACAgQAAxkBAAM1Z_b7iCAyMJPlurAIk8jdisR6b04AAg0PAAJ2EmhRCuO_Jh4djuA2BA",
    "BQACAgQAAxkBAAM2Z_b7iPmF1NX006P1DRALkcPob8MAAhAPAAJ2EmhR_LzUSaVFMkI2BA",
    "BQACAgQAAxkBAAM3Z_b7iHSMOmdz-hJ6Ubq3-YKLe4AAAhcPAAJ2EmhRuKnWbwIdSY02BA",
    "BQACAgQAAxkBAAM4Z_b7iGk5so-lwuWUhNe3-BTnJd8AAhoPAAJ2EmhRXNCuRINfZ7Q2BA",
    "BQACAgQAAxkBAAM5Z_b7iC1ITXph3njUUx2wgG2EnQIAAhsPAAJ2EmhRH6qsKIMBUOs2BA",
    "BQACAgQAAxkBAAM6Z_b7iP4-AWHDM9tYm4d5ZvemHEMAAhwPAAJ2EmhR_c_zg9tXLJM2BA",
    "BQACAgQAAxkBAAM7Z_b7iFNsG2yTjr_HeRCJBbvgIGcAAh0PAAJ2EmhRCYsfJMaTJxA2BA",
    "BQACAgQAAxkBAAM8Z_b7iAJHEM_4dEsMHLzK8hZjuroAAiEPAAJ2EmhRCL0iBh_iQ4U2BA",
    "BQACAgQAAxkBAAM9Z_b7iFDesssFs0YjmQ_wwvdYj1IAAiYPAAJ2EmhRUH_qr4n_h6c2BA",
    "BQACAgQAAxkBAAM-Z_b7iCOlFY2U9HUsbmYCjZ98N7cAAisPAAJ2EmhRXyHnD81AY0Q2BA",
    "BQACAgQAAxkBAAM_Z_b7iOZML30h4M6BHbOcLMxMaH4AAksNAAIm7XlRfxUjgQiLO_42BA",
    "BQACAgQAAxkBAANAZ_b7iDjAZDRvUk9_azmzIa0xXsgAAkwNAAIm7XlRStnlURNPSHY2BA",
    "BQACAgQAAxkBAANBZ_b7iCnalYVYj4mDgWm-bd5Eu_UAAu8JAAK9QIlRCCipWFkYGh82BA",
    "BQACAgQAAxkBAANCZ_b7iCpNCactQt2Dvie-kDseL88AAvAJAAK9QIlRlXzds4-nbg82BA",
    "BQACAgQAAxkBAANDZ_b7iFNAporDTjr7SwABM9seS2HRAALxCQACvUCJUY5YeaqJ9dR3NgQ",
    "BQACAgQAAxkBAANEZ_b7iP3Gd5nBwqwzQ9wwgg-GnyQAAvMJAAK9QIlRH_FUdzCKx5Q2BA",
    "BQACAgQAAxkBAANFZ_b7iL1pE5S2iPrX4H99MPfUWNIAAvQJAAK9QIlRhrY_zytvtDk2BA",
    "BQACAgQAAxkBAANGZ_b7iCbkoullPTQ-by1eRKHAAqcAAjsLAALrB6FRsL3sleI39sg2BA",
    "BQACAgQAAxkBAANaZ_b7s0PgYoFl0Sg8TPMnLqyinc0AAjwLAALrB6FRWwVHAs65cx82BA",
    "BQACAgQAAxkBAANcZ_b7xkxwYzPD70mXiW7Cz9EvDXoAAj0LAALrB6FRod_HMU-pbD42BA"
]

linux_video_ids = [
    "BAACAgQAAxkBAAIBMWYjFS4tKYPflg6kTVptLQEZHbd4AAJXMgACg-FRUP6BpjHqAAG1wjYE",
    "BAACAgQAAxkBAAIBM2YjFVZcMIfIjSK0zIvqnIPlsChdAAJYMgACg-FRUPmZ-FW8K4mNwjYE"
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        types.KeyboardButton("💻 FULL HACKING COURSE"),
    )
    markup.row(
        types.KeyboardButton("📱 VIRTUAL SMS"),
        types.KeyboardButton("🐧 LINUX BASICS")
    )
    markup.row(
        types.KeyboardButton("📞 CONTACT US")
    )

    welcome_text = (
        "👋 *Welcome to the Hacking Resource Bot!*\n\n"
        "Please choose an option from the menu below to get started:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')
    print(f"[+] Bot started by user: {message.from_user.first_name} (@{message.from_user.username})")
    print("[*] Course Teacher: Aleksa Tamburkovski")

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if message.text == "💻 FULL HACKING COURSE":
        print("[*] Sending Full Hacking Course ZIPs...")
        bot.send_message(message.chat.id, "📦 Sending Full Hacking Course ZIPs...")
        for file_id in zip_file_ids:
            bot.send_document(message.chat.id, file_id)
        print("[+] Full Hacking Course sent.")

    elif message.text == "📱 VIRTUAL SMS":
        print("[*] Sending Virtual SMS info...")
        bot.send_message(message.chat.id, "🔗 Visit this link to access Virtual SMS:\nhttps://smsreceivefree.com/")
        print("[+] Virtual SMS info sent.")

    elif message.text == "🐧 LINUX BASICS":
        print("[*] Sending Linux Basics videos...")
        bot.send_message(message.chat.id, "🎥 Sending Linux Basics Videos...")
        for file_id in linux_video_ids:
            bot.send_video(message.chat.id, file_id)
        print("[+] Linux Basics videos sent.")

    elif message.text == "📞 CONTACT US":
        bot.send_message(message.chat.id, "📩 You can reach us at: @Cyb37h4ck37")
        print("[+] Contact info sent.")

    else:
        bot.send_message(message.chat.id, "❌ Invalid option. Please select from the menu.")
        print(f"[!] Unknown command received: {message.text}")

print("[*] Bot is running and waiting for commands...")
bot.infinity_polling()
