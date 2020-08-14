from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import time
#import get_pictures
from datetime import datetime as dt

token = "b37704601a1e85ceef468b0423319a6d8861003684989d0948dbc9fcd615c60d8170f93334479f7a109d9"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and not event.from_me:
            receive_time = dt.now()
            print('Сообщение от пользователя vk.com/id' + str(event.user_id))
            print('Сообщение пришло в: ' + receive_time.strftime('%H:%M:%S'))
            print('Текст сообщения: ' + str(event.text))
            response = event.text.lower()
            if event.from_user and not event.from_me:
                if response == '1':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
                elif response == '2':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Пока, друг!', 'random_id': 0})
                else:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Не понял', 'random_id': 0})
               # elif response == '3':
                #    attachment = get_pictures.get(vk_session, -130670107, session_api)
                #    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Лови мемы!', 'random_id': 0, "attachment": attachment})