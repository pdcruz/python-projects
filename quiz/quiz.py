#!/usr/bin/env python3
import random
import time

DEFAULT_SLEEP = 1
### SECTION - QUESTION DATA ###
# Dictionary of all questions and answer options,
# Correct answer MUST be first item of the options list!
# Option order is randomized before presenting to the player.
questions = {
   "Which country won the battle of Austerlitz?": ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?": ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"],
   "Which general led his army across the Alps in the Second Punic War?": ["Hannibal Barca", "Julius Caesar", "Spartacus", "Marcus Agrippa"],
   "Which Indian river marks the end of the conquests of Alexander the Great?": ["Beas", "Hydaspes", "Ganges", "Mandovi"],
   "The standard ancient Greek spear-wall battle formation is called a . . . ": ["Phalanx", "Testudo", "Lembos", "Sarissa"],
}

### END SECTION - QUESTION DATA ###


### SECTION - FUNCTIONS ###
def start_quiz():
    print("\n***** WELCOME TO THE {} QUIZ *****".format(__name__))
    time.sleep(DEFAULT_SLEEP)
    print("\nINSTRUCTIONS\nAfter each question, type the letter of your answer and hit \"Enter\"")
    print("The only valid letters are a, b, c, or d")
    time.sleep(DEFAULT_SLEEP)
    input("\nPress Enter to begin ")


def ask_question(key):
    print("\n{}".format(key))
    options = generate_options(questions[key])
    return options

def generate_options(option_list):
    options = {"a":"", "b":"", "c":"", "d":""}
    shuffled_options_list = random.sample(option_list, len(option_list))
    for key in options:
        options[key] = shuffled_options_list.pop(0)
    print(options)
    return (options)

def check_answer(player_answer, correct_answer, options_dict):
    try:
        return options_dict[player_answer] == correct_answer
    except KeyError:
        player_answer = input("Invalid choice, enter a letter a, b, c, or d only: ").lower()
        # Hopefully they don't cock this up 1000 times and hit the recursion limit
        return check_answer(player_answer, correct_answer, options_dict)

def print_feedback(result, correct_answer):
    if result:
        print("Correct")
    else:
        print("Incorrect. The answer is {}".format(correct_answer))

### END SECTION - FUNCTIONS ###


### SECTION - MAIN ###
score = 0
start_quiz()

for key in questions:
    time.sleep(DEFAULT_SLEEP)
    correct_answer = questions[key][0]
    options = ask_question(key)
    player_answer = input("Enter choice: ").lower()
    result = check_answer(player_answer, correct_answer, options)
    print_feedback(result, correct_answer)
    score += result

print("\nYour score: {0}/{1}".format(score, len(questions)))

### END SECTION - MAIN ###
