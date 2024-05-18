import random
import string
import os

from bot_counter.loader import bot

# Функция для генерации случайного реферрального кода
def generate_referral_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_referral_link(referral_code):
    return f"https://t.me/{bot.get_me().username}?start={referral_code}"

# Функция для проверки подписки пользователя на каналы
def check_subscription(user_id):
    try:
        chat_id = os.getenv('TELEGRAM_CHANNEL_ID')
        # Проверяем статус участия пользователя в канале
        status = bot.get_chat_member(chat_id, user_id).status
        # Если статус "member", "creator" или "administrator", значит пользователь имеет доступ
        return status in ["member", "creator", "administrator"]
    except Exception as e:
        print("Ошибка при проверке подписки на канал:", e)
        return False