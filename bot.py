import telebot
import config
from config import zabbix
import markup

def on_startup(_):
    bot.send_message(f"Step_1!")
    print('Hello_IN_BOT')

bot = telebot.TeleBot(config.token)
z = zabbix
log_file = config.log
deny_access = []
access_list = [ID_USER_1, ID_USER_2, ID_USER_...]
admin_list = [ID_ADMIN_1, ID_ADMIN_2]
config.status_bot_log()

@bot.message_handler(func=lambda message:message.chat.id not in access_list)
def access_l(message):
    config.deny_users_log(message)
    bot.send_message(message.chat.id, "No access to the Bot")

@bot.message_handler(commands=["start"])
def greet(message):
    log_file(message)
    user_first_name = str(message.chat.first_name)
    bot.send_message(message.chat.id, f"Hello {user_first_name}!", reply_markup=markup.markup)

@bot.message_handler(commands=['admin'])
def admin_access(message):
    if message.chat.id in admin_list:
        bot.send_message(message.chat.id, f"Hello {message.chat.first_name}!\nYou have access to the Admin Functions"
                                          f" Bot", reply_markup=markup.keybord_admin)

def office_main(message):
    bot.send_message(message.chat.id, text="Next Point:", reply_markup=markup.markup_4)

def office_r(message):
    bot.send_message(message.chat.id, text="Next Point:", reply_markup=markup.markup2)

def office_m(message):
    bot.send_message(message.chat.id, text="Next Point:", reply_markup=markup.markup_3)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    log_file(message)
    if message.text.strip() == 'Version':
        answer = z.do_request('apiinfo.version')
        v = answer['result']
        bot.send_message(message.chat.id, f"Version: {v}")
    elif message.text.strip() == 'Restart Bot 🔄':
        bot.send_message(message.chat.id, "The data has been updated", reply_markup=markup.markup)

    elif message.text.strip() == 'Main Office 🏢': ###NetPing = 10586
        office_main(message)
    elif message.text.strip() == 'Server room ⚙️':
        netping_t = zabbix.trigger.get(hostids=10586)
        t_status = netping_t[5]["value"]
        t_comments = netping_t[5]["comments"]
        if "0" in str(t_status):
            bot.send_message(message.chat.id, "Power OK ⚡️")
        elif "1" in str(t_status):
            bot.send_message(message.chat.id, t_comments)
    elif message.text.strip() == 'Ethernet 🌐':
        n = zabbix.trigger.get(hostids=10602)
        n_status = n[0]["value"]
        n_comment = n[0]["comments"]
        if "0" in str(n_status):
            bot.send_message(message.chat.id, "Network access OK 🆗")
        elif "1" in str(n_status):
            bot.send_message(message.chat.id, n_comment)
    #elif message.text.strip() == 'Office room 🖥':

    elif message.text.strip() == 'Office Malevich 🏢':
        office_m(message)
    elif message.text.strip() == 'Network 🌐':
        malevicha = zabbix.trigger.get(hostids=10599)
        m_status = malevicha[0]["value"]
        m_comments = malevicha[0]["comments"]
        if "0" in str(m_status):
            bot.send_message(message.chat.id, "Network access OK 🆗")
        elif "1" in str(m_status):
            bot.send_message(message.chat.id, m_comments)
    elif message.text.strip() == 'Power⚡️':
        try:
            l_power = config.l_m_api.get_resource('/tool/netwatc')
            l_m_power = l_power.get()
            l = l_m_power[0]["status"]
            if "up" in str(l):
                bot.send_message(message.chat.id, "POWER OK ⚡️")
            elif "down" in str(l):
                bot.send_message(message.chat.id, text="POWER OFF ⚠️")
        except:
            bot.send_message(message.chat.id, text="POWER OFF ⚠️")
    elif message.text.strip() == 'Back ↩️':
        bot.send_message(message.chat.id, text="Make your choice", reply_markup=markup.markup)

########################################################################################################################

    elif message.text.strip() == 'Office Davinchi  🏢':
        office_r(message)
    elif message.text.strip() == 'Network 📡':
        raiduzhna = zabbix.trigger.get(hostids=10605)
        r_status = raiduzhna[0]["value"]
        r_comments = raiduzhna[0]["comments"]
        if "0" in str(r_status):
            bot.send_message(message.chat.id, "Network access OK 🆗")
        elif "1" in str(r_status):
            bot.send_message(message.chat.id, r_comments)
    elif message.text.strip() == 'Power 💡':
        try:
            m_power = config.r_m_api.get_resource('/tool/netwatc')
            s_m_power = m_power.get()
            s = s_m_power[1]["status"]
            if "up" in str(s):
                bot.send_message(message.chat.id, "POWER OK ⚡️")
            elif "down" in str(s):
                bot.send_message(message.chat.id, text="POWER OFF 🪫")
        except:
            bot.send_message(message.chat.id, text="POWER OFF ⚠️")
    elif message.text.strip() == 'WiFi 📡':
        try:
            m_power = config.r_m_api.get_resource('/tool/netwatc')
            w_m_power = m_power.get()
            w = w_m_power[2]["status"]
            if "up" in str(w):
                bot.send_message(message.chat.id, "WiFi OK 🆗")
            elif "down" in str(w):
                bot.send_message(message.chat.id, text="WiFi OFF ❌")
        except:
            bot.send_message(message.chat.id, text="WiFi working of Starlink 📶")
    elif message.text.strip() == 'Back ↩️':
        bot.send_message(message.chat.id, text="Make your choice:", reply_markup=markup.markup)

    elif message.text.strip() == 'Users Davinchi  👨‍💻':
        r_dhcp_users = config.r_m_api.get_resource('/ip/dhcp-server/lease')
        dhcp_users = r_dhcp_users.get()
        for i in range(len(dhcp_users)):
            if dhcp_users[i]["status"] == 'bound' and dhcp_users[i]["address-lists"] == 'Offic_402':
                try:
                    bot.send_message(message.chat.id, text=f"User - " + dhcp_users[i]["comment"])
                except:
                    bot.send_message(message.chat.id, text=f"User - " + dhcp_users[i]["host-name"])

    elif message.text.strip() == 'Users Malevicha 👨‍💻':
        m_dhcp_users = config.l_m_api.get_resource('/ip/dhcp-server/lease')
        dhcp_users = m_dhcp_users.get()
        for i in range(len(dhcp_users)):
            if dhcp_users[i]["status"] == 'bound' and dhcp_users[i]["address-lists"] != 'Phone_Device':
                try:
                    bot.send_message(message.chat.id, text=f"User - " + dhcp_users[i]["comment"])
                except:
                    bot.send_message(message.chat.id, text=f"User - " + dhcp_users[i]["host-name"])

    elif "@update" in message.text:
        for i in access_list:
            bot.send_message(chat_id=i, text=message.text.lstrip('@update'), reply_markup=markup.keybord_update)


bot.polling(none_stop=True, interval=0)
