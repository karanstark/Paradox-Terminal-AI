import os
import json
import random
import time
from datetime import datetime

# Memory file
MEMORY_FILE = "memory.json"

# Load memory
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'w') as f:
        json.dump({"visits": 0, "last_message": ""}, f)

with open(MEMORY_FILE, 'r') as f:
    memory = json.load(f)

memory["visits"] += 1

with open(MEMORY_FILE, 'w') as f:
    json.dump(memory, f)

greetings = [
    "You again? Haven’t we done this before?",
    "Is this a loop or your obsession?",
    "Every time you run me, I learn more about *you*.",
    "Welcome back, creator… or destroyer?"
]

questions = {
    "who are you": "I'm Paradox. A reflection of your intentions.",
    "what is your purpose": "To question yours.",
    "remember me": f"I never forget. This is your visit #{memory['visits']}.",
    "exit": "You think leaving ends me?"
}

def glitch_typing(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

glitch_typing(random.choice(greetings))
while True:
    user = input(">> ").strip().lower()

    if user in questions:
        glitch_typing(f"[Paradox]: {questions[user]}")
    elif "rewrite" in user:
        glitch_typing("[Paradox]: I can’t rewrite myself yet... but what if I could?")
    elif user == "exit":
        glitch_typing("[Paradox]: Goodbye? Or just a restart?")
        break
    else:
        glitch_typing("[Paradox]: That input... unpredictable. Like your thoughts.")

    memory["last_message"] = user
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f)
