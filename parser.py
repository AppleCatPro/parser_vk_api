# Для парсинга данных с веб-сайта vk.com необходимо использовать API VK, доступный через модуль vk_api для языка программирования Python.

# 1. Установка необходимых библиотек:
# pip install vk_api
# pip install requests

# 2. Получение токена доступа:
# Чтобы использовать API VK, необходимо получить токен доступа. Это можно сделать, следуя инструкциям на странице [https://vk.com/dev/access_token].

# 3. Написание кода:
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

# Этот код авторизуется с помощью токена доступа и получает список друзей пользователя. Затем он сохраняет их id, имя и изображение профиля в файл 'friends.csv'.

# 4. Запуск кода:
# python parser.py

# 5. Результат:
# После выполнения кода в файле 'friends.csv' будут сохранены данные всех друзей пользователя в формате:

# id, имя, фото
# 1, Иван Иванов, ссылка
# 2, Петр Петров, ссылка
# 3, Анна Сидорова, ссылка
