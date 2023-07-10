from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#item1 = types.KeyboardButton('Version')
item2 = types.KeyboardButton('Main Office 🏢')
item3 = types.KeyboardButton('Office Main 🏢')
item4 = types.KeyboardButton('Office Second 🏢')
item5 = types.KeyboardButton('Restart Bot 🔄')
markup.add(item2, item3, item4, item5)


button_1 = types.KeyboardButton('Network 📡')
button_2 = types.KeyboardButton('Power 💡')
button_3 = types.KeyboardButton('WiFi 📡')
button_4 = types.KeyboardButton('Back ↩️')

button_5 = types.KeyboardButton('Network 🌐')
button_6 = types.KeyboardButton('Power⚡️')
button_7 = types.KeyboardButton('Back ↩️')
button_8 = types.KeyboardButton('Server room ⚙️')
button_9 = types.KeyboardButton('Office room 🖥')
button_10 = types.KeyboardButton('Back ↩️')
button_11 = types.KeyboardButton('Ethernet 🌐')
button_12 = types.KeyboardButton('Restart Bot 🔄')
button_13 = types.KeyboardButton("Users Main 👨‍💻")
button_14 = types.KeyboardButton("Users Second 👨‍💻")

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup2.add(button_1, button_2, button_3, button_4)

markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markup_3.add(button_5, button_6, button_7)

markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markup_4.add(button_8, button_11, button_10)

keybord_update = types.ReplyKeyboardMarkup(resize_keyboard=True)
keybord_update.add(button_12)

keybord_admin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybord_admin.add(button_13, button_14, item2, item3, item4, item5, button_10)