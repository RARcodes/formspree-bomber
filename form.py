import requests
import random
import string
import time
from colorama import Fore, Style, init
from threading import Thread

init()

Fore.GREEN
Fore.RED
Style.RESET_ALL

last_code = input('Enter the code of the form submission: ')
url = f'https://formspree.io/f/{last_code}'

def generate_random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def print_status(status, color):
    print(f'{color}{status}{Style.RESET_ALL}')

def send_post_request():
    while True:
        name = generate_random_name()
        data = {
            'name': name,
            'email': f'{name}@gmail.com',
            'message': 'Hello, Formspree!'
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print_status(f'Form submission successful: {name}', Fore.GREEN)
        else:
            print_status(f'Form submission failed: {name}', Fore.RED)
        time.sleep(10)

thread = Thread(target=send_post_request)
thread.start()

thread.join()
