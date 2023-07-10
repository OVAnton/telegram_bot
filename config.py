import datetime
from pyzabbix import ZabbixAPI
import telebot
import routeros_api

#staging


token = "TELEGRAM_TOKEN"
#wokr_token
bot = telebot.TeleBot(token)

##zabbix_connect
zabbix = ZabbixAPI(url='http://zabbix_ip/', user='_USER_', password='_PASSWORD_')

mikrotik_malevich = routeros_api.RouterOsApiPool(
    host='MIKROTIK_IP',
    username='api_user',
    password='pass_for_api_user',
    port=8728,
    plaintext_login=True
)
try:
    l_m_api = mikrotik_l.get_api()
except:
    print("error_connect_to_mikrotik_malevich")

mikrotik_davinchi = routeros_api.RouterOsApiPool(
    host='MIKROTIK_IP',
    username='api_user',
    password='pass_for_api_user',
    port=8728,
    plaintext_login=True
)
try:
    r_m_api = mikrotik_r.get_api()
except:
    print("error_connect_to_mikrotik_davinchi")

def log(message):
    l = open('log/' + str(message.chat.first_name) + "__" + str(message.chat.id) + "__" + str(datetime.date.today()) +
             '_log.txt', 'a+', encoding='UTF-8')
    l.write("ID : " + str(message.chat.id) + " _/_ " + "First Name: " + str(message.chat.first_name) + " _/_ "
                   + "Last Name: " + " _/_ " + str(message.chat.last_name) + " _/_ " + "Text: " + str(message.text) +
                   " _/_ " + "Date: " + str(datetime.date.today()) + '\n')
    l.close()

def deny_users_log(message):
    deny_log = open('log/' + 'deny_users_id_log.txt', 'a+', encoding='UTF-8')
    deny_log.write("ID : " + str(message.chat.id) + " _/_ " + "First Name: " + str(message.chat.first_name) + " _/_ "
                   + "Last Name: " + " _/_ " + str(message.chat.last_name) + " _/_ " + "Text: " + str(message.text) +
                   " _/_ " + "Date: " + str(datetime.date.today()) + '\n')
    deny_log.close()

def status_bot_log():
    status_bot = open('log/' + "status_bot.txt", 'a+', encoding='UTF-8')
    status_bot.write(str(datetime.date.today()) + '\n')
    status_bot.close()
