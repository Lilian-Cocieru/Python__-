import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password
name = input("Как тебя зовут? ")
print(f"Привет, {name}")
length = int(input("Сколько символов в пароле? "))
print(f"Твой пароль: {generate_password(length)}")
