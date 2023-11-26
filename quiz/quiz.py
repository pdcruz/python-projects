#!/usr/bin/env python3
import random
import time

DEFAULT_SLEEP = 1
### SECTION - QUESTION DATA ###

category_options = {
    "a":"History",
    "b":"Geography",
    "c":"Science",
    "d":"Music"
}

# Dictionary of all questions and answer options,
# Correct answer MUST be first item of the options list!
# Option order is randomized before presenting to the player.
history_questions = {
   "Which country won the battle of Austerlitz in 1805?": ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?": ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"],
   "Which general led his army across the Alps in the Second Punic War?": ["Hannibal Barca", "Julius Caesar", "Spartacus", "Marcus Agrippa"],
   "Which Indian river marks the furthest point of the expedition of Alexander the Great?": ["Beas", "Hydaspes", "Ganges", "Mandovi"],
   "The standard ancient Greek spear-wall battle formation is called a . . . ": ["Phalanx", "Testudo", "Lembos", "Sarissa"],
}

geography_questions = {
    "What is the world's longest river?" : ["Nile", "Amazon", "Mekong", "Mississippi"],
    "In which city is Sugarloaf Mountain located?" : ["Rio de Janeiro", "Cape Town", "Lisbon", "Chennai"]
}

science_questions = {
    "Which of the following is an SI base unit?" : ["Candela", "Volt", "Pascal", "Radian"],
    "In 2012, a space probe became the first human-made object to exit the solar system. What is its name?" : ["Voyager", "Cassini", "Discovery", "Pioneer"]
}

music_questions = {
    "How many strings does a standard guitar have?" : ["6", "7", "4", "8"],
    "In the Western musical system, what is the smallest division between two notes called?" : ["Semitone", "Whole step", "Interval", "Slide"],
    "Jerry Garcia was the lead guitarist of which band?" : ["The Grateful Dead", "Pink Floyd", "Rush", "Blue Oyster Cult"]
}


### END SECTION - QUESTION DATA ###



### SECTION - FUNCTIONS ###
def start_quiz():
    print("\n***** WELCOME TO THE {} QUIZ *****".format(__name__))
    time.sleep(DEFAULT_SLEEP)
    print("\nINSTRUCTIONS\nAfter each question, type the letter of your answer and hit \"Enter\"")
    print("The only valid letters are a, b, c, or d")
    time.sleep(DEFAULT_SLEEP)


def display_options(input_dict):
    for key in input_dict:
        print("{}. {}".format(key, input_dict[key]))


def set_quiz_category(category_dict):
    print("\nQuiz Categories")
    display_options(category_dict)
    category_choice = input("Enter a letter to choose a category: ").lower()
    # NOT a great implementation of the KeyError check here, find a better way
    try:
        category_name = category_dict[category_choice]
    except KeyError:
        print("Invalid choice, enter a letter valid letter option from the list")
        # Hopefully they don't cock this up 1000 times and hit the recursion limit
        category_name = set_quiz_category(category_dict)
    print("\nStarting the {} quiz".format(category_name))
    match category_choice:
        case "a":
            return history_questions
        case "b":
            return geography_questions
        case "c":
            return science_questions
        case "d":
            return music_questions


def ask_question(key, all_questions):
    print("\n{}".format(key))
    options = generate_options(all_questions[key])
    return options


def generate_options(option_list):
    options = {"a":"", "b":"", "c":"", "d":""}
    shuffled_options_list = random.sample(option_list, len(option_list))
    for key in options:
        options[key] = shuffled_options_list.pop(0)
    display_options(options)
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
questions = set_quiz_category(category_options)

for key in questions:
    time.sleep(DEFAULT_SLEEP)
    correct_answer = questions[key][0]
    options = ask_question(key, questions)
    player_answer = input("Enter choice: ").lower()
    result = check_answer(player_answer, correct_answer, options)
    print_feedback(result, correct_answer)
    score += result

print("\nYour score: {0}/{1}".format(score, len(questions)))

### END SECTION - MAIN ###
