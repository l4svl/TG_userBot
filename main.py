import random,time
from datetime import datetime, timedelta
import pyrogram.types
from pyrogram import Client, filters
from config import id, hash, priton

app_id = id
app_hash = hash
app = Client('account', app_id, app_hash)

result = dict()
keys = []
user_name=[]

def zxc_killer():
    i = 1000
    while True:
        app.send_message(priton, f'{i} -7 ={i - 7}')
        i = i - 7
        if i < 7:
            app.send_message(priton, f'Больше нельзя вычитать,но Рома попуск')
            return False


def users_id():
    a = app.get_chat_members(priton)
    for i in a:
        keys.append(i.user.username)
        user_name.append(i.user.username)
        result[i.user.username] = i.user.id


def Thanos():
    app.send_message(priton, 'ITS TIMEE FOR THANOS GAME!')
    app.send_video(priton, r"C:\Users\User\PycharmProjects\TG_userBot\resource\thanos-finger-snap.mp4",
                   caption='50% из вас будут уничтожены!')
    for i in range(int(app.get_chat_members_count(priton) // 2)):
        try:
            name = random.choice(keys)
            keys.remove(name)
            ud = result.get(name)
            app.restrict_chat_member(priton, ud, pyrogram.types.ChatPermissions(),
                                     datetime.now() + timedelta(minutes=15))
            app.send_message(priton, f'Пользователь {name} был успешно уничтожен, для баланса во вселенной!')
        except Exception as e:
            print(e)
    app.send_message(priton, f'{random.choice(user_name)} лох попуск ебаный (имхо) азазза')


app.start()
users_id()
Thanos()
