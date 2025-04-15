import telebot from telebot import types
                                                  bot_token = "7406063194:AAFcc3LpqIvhG-pii4lSKJobGPtxLcMJqu4"
bot = telebot.TeleBot(bot_token)
                                                  zip_file_ids = [
    "BQACAgQAAxkBAAM0Z_b7iLeEOBogKlKKdDSHn8QgS7UAAgsPAAJ2EmhR_flgf_6OgJk2BA",                           "BQACAgQAAxkBAAM1Z_b7iCAyMJPlurAIk8jdisR6b04AAg0PAAJ2EmhRCuO_Jh4djuA2BA",                           "BQACAgQAAxkBAAM2Z_b7iPmF1NX006P1DRALkcPob8MAAhAPAAJ2EmhR_LzUSaVFMkI2BA",
    "BQACAgQAAxkBAAM3Z_b7iHSMOmdz-hJ6Ubq3-YKLe4AAAhcPAAJ2EmhRuKnWbwIdSY02BA",                           "BQACAgQAAxkBAAM4Z_b7iGk5so-lwuWUhNe3-BTnJd8AAhoPAAJ2EmhRXNCuRINfZ7Q2BA",                           "BQACAgQAAxkBAAM5Z_b7iC1ITXph3njUUx2wgG2EnQIAAhsPAAJ2EmhRH6qsKIMBUOs2BA",
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

Python_ids = [
    "BQACAgQAAxkBAAICS2f9i1yhXN-ZQ5AH1lRPvizpsy4GAAImEwACfAKRUoVZz3g5_bvxNgQ",
    "BQACAgQAAxkBAAICTGf9i1wj612gKfXCuj16fd8XOye8AAIqEwACfAKRUvAwJM2N72gvNgQ",
    "BQACAgQAAxkBAAICTWf9i1wPDC9CraQAAfq-7aJfGnMNwgACNRMAAnwCkVLCIRLG8NfZYTYE",
    "BQACAgQAAxkBAAICTmf9i1wcNfSiWQwOprXVDP7fPxSmAAJFEwACfAKRUprLZmjRV8NxNgQ",
    "BQACAgQAAxkBAAICT2f9i1z3lv0Rhv3S0SWtg_wY9amiAAKFEQACfAKZUlHjvN2OuQNVNgQ",
    "BQACAgQAAxkBAAICUGf9i1z4CdVg__ejrq_7rJjpCxlCAAL_EwACv4ORUui1yl73QwAB-DYE",
    "BQACAgQAAxkBAAICUmf9i1x20Fcv54uhkV2phMnmQwYxAAIDFAACv4ORUrA2_PbuJGCdNgQ",
    "BQACAgQAAxkBAAICU2f9i1yROs-UMZc2lDsD0kOFFkf6AAIFFAACv4ORUl-IVPoKzdOwNgQ"
]

Rats = [
    ("BQACAgUAAxkBAAICiGf95nUxEpuRWBFtBJru5p_B0t6AAAKSEgAC2x6hVJcxpX7BLLzENgQ", "Password:\n`@ShadowProtocol01`"),
    ("BQACAgUAAxkBAAICh2f95nWAINtc2SdId6g879UonCBxAAILDgAClP0IVLxRIcSu5bjdNgQ", ""),
    ("BQACAgUAAxkBAAICiWf95nUd_gQCds68Rm1WTXDmvfF4AAK-DgAC7AmAVtf-_mm1tUr_NgQ", ""),
    ("BQACAgUAAxkBAAICimf95nWFm3PoSpGbqbTLjV3xFKhWAAKzEQACcydRVgn7bx3PvXVGNgQ", ""),
    ("BQACAgUAAxkBAAICi2f95nVUHLsxyDRdLoHfZllyUFF3AAIPEAACjfOZVNiUNtq9BMVcNgQ", ""),
    ("BQACAgUAAxkBAAICjGf95nWX9zd9wjUJFQ5c7b70xec_AAKfDgACIvzoVax_gjQ-JT6mNgQ", ""),
    ("BQACAgUAAxkBAAICjWf95nU326fj-I-umV2Q0XKh8AJzAAI0CgACEdcRVyGkdgaIVc5RNgQ", "Password >> I think not protected"),
    ("BQACAgUAAxkBAAICjmf95nWutS9SwiktRJmA9PG2L9MWAAKxEQACoHTZV4K7sbwx0ET4NgQ", "Password >> I don't know, I think not protected"),
    ("BQACAgUAAxkBAAICj2f95nVdax2xJMFqPNXciM4ubJ2mAAIIEQACp1dgVAfaeWgxDT0gNgQ", "🐀"),
    ("BQACAgUAAxkBAAICkWf95nUUFGXT407kZjVzjrd9aU95AAK2DgACpZ9pVSoWjTcas044NgQ", "🐀"),
    ("BQACAgUAAxkBAAICkmf95nVKutV1jqB1nS716I3O72X9AAILEAACtcZRVVhuzM1zIT_gNgQ", ""),
    ("BQACAgUAAxkBAAICk2f95nW72TFGLGIUyteilagGsA3VAAK3DgACpZ9pVWuq62c4JrPENgQ", ""),
    ("BQACAgUAAxkBAAIClGf95nVEXpZrxuf69ncCcHk4PQHMAAK5DgACpZ9pVdYlztsIxsmHNgQ", ""),
    ("BQACAgUAAxkBAAIClmf95nVtFFx9GTxUb1E0ufIHKSxGAAK6DgACpZ9pVTJSiIOrQmOlNgQ", ""),
    ("BQACAgEAAxkBAAICl2f95nVAYvib2POSPF91QgI6s9InAAIwBQACvajoR6JtwQH-EcOPNgQ", "Password >> 3214"),
    ("BQACAgUAAxkBAAICmGf95nXUen_DwPfnMu35FNEiwDVRAAIMCwACA8CxVNFOFLTR1TQaNgQ", ""),
    ("BQACAgUAAxkBAAICmWf95nX-jyuGxeqNevqfuvYb4nKFAAKFDgACddYwVocFdmTrM70HNgQ", "GhostRat - Clean & Stable\nUser: 1\nPass: 1\nSupport Android 14\n\nPassword: I think not protected"),
    ("BQACAgUAAxkBAAICm2f95nUc7yr3zF-U9P75XfhKqYbVAAIoEQACNDexVvBn2xuMghjfNgQ", "CRAXSRAT V7.6 - Latest\n\n• Android 14 Support\n• Boot Feature\n• Licence Bypass needed ⚠️")
]

linux_video_ids = [
    "BAACAgUAAxkBAAICQWf9fqJ7qtultqJRJDXBkuJC85A3AAI_FQAC0HDJVUTpNVOEOUu5NgQ",
    "BAACAgUAAxkBAAICQmf9fqIn1-1RXVN0BcD4k5GFPwtPAAJAFQAC0HDJVbVvpsqUQ1YiNgQ",
    "BAACAgUAAxkBAAICQ2f9fqJTScg9RhzzWYlNh00iOjgPAAJCFQAC0HDJVQ2MGxQLlo_KNgQ",
    "BAACAgUAAxkBAAICRGf9fqLtzJrqNv4o4cxvHMRs0kLDAAKCFAACHyzYVVJyIiMSr48vNgQ",
    "BAACAgUAAxkBAAICRWf9fqJplRxbf2cV9h8JQeKuNTakAAKIFAACHyzYVRVcyY5IUUtUNgQ"
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
    types.KeyboardButton("💻 FULL ETHC COURSE"),
    types.KeyboardButton("💻 CODING"))
    markup.row(
    types.KeyboardButton("📱 VIRTUAL SMS"),
    types.KeyboardButton("🐧 LINUX BASICS")
)
    markup.row(types.KeyboardButton("🐀 RATS "))
    markup.row(types.KeyboardButton("📞 CONTACT US"))

    welcome_text = (
        "👋 *Welcome to the Hacking Resource Bot!*\n\n"
        "Please choose an option from the menu below to get started:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')
    print(f"[+] Bot started by user: {message.from_user.first_name} (@{message.from_user.username})")

def show_coding_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("🐍 Python"), types.KeyboardButton("🌐 HTML & CSS"))
    markup.row(types.KeyboardButton("🔙 Back"))
    bot.send_message(chat_id, "Select a coding topic:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if message.text == "💻 FULL ETHC COURSE":
        print("[*] Sending Full Hacking Course ZIPs...")
        bot.send_message(message.chat.id, "📦 Sending Full Hacking Course ZIPs...")
        for file_id in zip_file_ids:
            bot.send_document(message.chat.id, file_id)
        print("[+] Full Hacking Course sent.")

    elif message.text == "📱 VIRTUAL SMS":
        print("[*] Sending Virtual SMS info...")
        bot.send_message(message.chat.id, "🔗 Visit this link to access Virtual SMS:\nhttps://smsreceivefree.com/")
        print("[+] Virtual SMS info sent.")

    elif message.text == "🐀 RATS":
        bot.send_message(message.chat.id, "Sending 🐀 RATS\nNote: For Educational Purposes Only!!!")
        for file_id, caption in Rats:
            bot.send_document(message.chat.id, file_id, caption=caption,parse_mode="Markdown")
        print("[+] Rats sent.")

    elif message.text == "🐧 LINUX BASICS":
        print("[*] Sending Linux Basics videos...")
        bot.send_message(message.chat.id, "🎥 Sending Linux Basics Videos...")
        for file_id in linux_video_ids:
            bot.send_video(message.chat.id, file_id)
        print("[+] Linux Basics videos sent.")

    elif message.text == "📞 CONTACT US":
        bot.send_message(message.chat.id, "📩 You can reach us at: @Cyb37h4ck37\n @Syevil011")
        print("[+] Contact info sent.")

    elif message.text == "💻 CODING":
        print("[*] Showing coding submenu...")
        show_coding_menu(message.chat.id)

    elif message.text == "🐍 Python":
        bot.send_message(message.chat.id, "Sending 🐍 Python Files...")
        for file_id in Python_ids:
            bot.send_document(chat_id=message.chat.id, document=file_id)
        print(f"[*] Sending: {file_id}")
    elif message.text == "🌐 HTML & CSS":
        bot.send_message(message.chat.id, "📚 HTML & CSS resources coming soon!")

    elif message.text == "🔙 Back":
        start(message)  # This will call the /start function to return to main menu

    else:
        bot.send_message(message.chat.id, "❌ Invalid option. Please select from the menu.")
        print(f"[!] Unknown command received: {message.text}")

print("[*] Bot is running and waiting for commands...")
bot.infinity_polling()