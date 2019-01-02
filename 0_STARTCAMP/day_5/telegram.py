
import requests

MY_CHAT_ID = '798658564'
BOT_TOKEN = '668815852:AAGncf4MrgoGtZYtxF47lM_XoAMDNKFJ2o4'
msg = '치킨 먹고 싶다'

url = 'https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_TOKEN, MY_CHAT_ID, msg)

res = requests.get(url)
print(res.json())


# https://api.telegram.org/
#     bot668815852:AAGncf4MrgoGtZYtxF47lM_XoAMDNKFJ2o4/
#     sendMessage?
#     chat_id=
#     798658564
#     &
#     text=
#     %EC%A7%91%EC%97%90%EA%B0%80%EA%B3%A0%EC%8B%B6%EB%8B%A4

