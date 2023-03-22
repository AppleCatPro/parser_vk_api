import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

# авторизация
vk_session = vk_api.VkApi(token='токен_доступа')
vk = vk_session.get_api()

# получение списка друзей
friends_list = vk.friends.get(fields='photo_100')

# сохранение данных в файл
with open('friends.csv', 'w', encoding='utf-8') as f:
    f.write('id, имя, фото\n')
    for friend in friends_list['items']:
        user_id = friend['id']
        user_name = friend['first_name'] + ' ' + friend['last_name']
        user_photo = friend['photo_100']

        f.write(f'{user_id}, {user_name}, {user_photo}\n')
