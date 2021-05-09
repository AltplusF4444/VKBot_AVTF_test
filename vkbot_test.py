# -*- coding: utf-8 -*-

import requests
from tokenvk import token 

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


def main():
    session = requests.Session()
    vk_session = vk_api.VkApi(token=token['token'])  

    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)
    


    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            if event.text == 'Hi':
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Hello'
                )
                print('ok')
                continue
            else :
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Неудовлетворяющий запрос'
                )
            print('No')


if __name__ == '__main__':
    main()
