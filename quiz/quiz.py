#!/usr/bin/env python3
import random

questions = {
   "Which country won the battle of Austerlitz?": ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?": ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"]
}

def start_quiz():
    print("Welcome to the {} quiz show!\n".format(__name__))
      
def ask_question(q_key):
    print(q_key)
    generate_options(questions[q_key])
    return input("Enter choice: ")

def generate_options(option_list):
    options = {"a":"", "b":"", "c":"", "d":""}
    shuffled_options = random.sample(option_list, len(option_list))
    for key in options:
        options[key] = shuffled_options.pop(0)
    print(options)

start_quiz()
for key in questions:
    answer = ask_question(key)
    print(answer)
