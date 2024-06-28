import random
import time

def random_text_generator():
    messages = [
        "Hello, world!",
        "This is a random message.",
        "Logging to the GUI is fun!",
        "Another random message.",
        "Yet another message!"
    ]
    while True:
        print(random.choice(messages))
        time.sleep(2)