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
   "Which country won the battle of Austerlitz in 1805?" : ["France", "Russia", "England", "Germany"],
   "Who was NOT a political leader during WW2?" : ["Woodrow Wilson", "Joseph Stalin", "Winston Churchill", "Benito Mussolini"],
   "This general led a Carthaginian army across the Alps in the Second Punic War." : ["Hannibal Barca", "Julius Caesar", "Spartacus", "Boudicca"],
   "The army of Alexander the Great refused to march further east beyond this Indian river." : ["Beas", "Hydaspes", "Ganges", "Mandovi"],
   "The standard ancient Greek spear-wall battle formation is called a . . . " : ["Phalanx", "Testudo", "Lembos", "Sarissa"],
}

geography_questions = {
    "What is the world's longest river?" : ["Nile", "Amazon", "Mekong", "Mississippi"],
    "In which city is Sugarloaf Mountain located?" : ["Rio de Janeiro", "Cape Town", "Lisbon", "Chennai"],
    "This sea separates Greece and Turkey." : ["Aegean", "Ionian", "Adriatic", "Balearic"],
    "What is the world's deepest lake?" : ["Baikal", "Michigan", "Victoria", "Titicaca"],
    "What percentage of the Earth is covered by water?" : ["71%", "52%", "85%", "48%"]
}

science_questions = {
    "What phenomenon is caused by charged solar particles hitting the Earth's atmosphere?" : ["Aurora", "Sunspot", "Mirage", "Shining"],
    "In 2012, this space probe became the first human-made object to exit the solar system." : ["Voyager 1", "Cassini", "Discovery", "Pioneer 3"],
    "What machine performs the opposite function of a motor?" : ["Generator", "Pulley", "Engine", "Gyroscope"],
    "How many litres of blood does an average human adult have?" : ["5", "2", "12", "30"],
    "Which of these species has the longest lifespan?" : ["Greenland Shark", "Galapagos Tortoise", "Red King Crab", "Komodo Dragon"]
}

music_questions = {
    "How many strings does a standard guitar have?" : ["6", "7", "4", "8"],
    "In the Western musical system, what is the smallest possible pitch distance between two notes?" : ["Semitone", "Whole step", "Interval", "Slide"],
    "Jerry Garcia was the lead guitarist of which band?" : ["The Grateful Dead", "Pink Floyd", "Rush", "Blue Oyster Cult"],
    "What is the second-lowest of the six voical ranges?" : ["Baritone", "Contralto", "Tenor", "Iago"],
    "Which of these musicians did not die at age 27?" : ["Biggie Smalls", "Jimi Hendrix", "Amy Winehouse", "Kurt Cobain"]
}


### END SECTION - QUESTION DATA ###



### SECTION - FUNCTIONS ###
def start_quiz():
    print("\n***** WELCOME TO THE {} QUIZ *****".format(__name__))


def show_instructions():
    print("\nINSTRUCTIONS\nAfter each question, type the letter of your answer and hit \"Enter\"")
    print("The only valid letters are a, b, c, or d")
    input("\nPress Enter to begin: ")


def display_options(input_dict):
    for key in input_dict:
        print("{}. {}".format(key, input_dict[key]))


def shuffle_dictionary(input_dict):
    item_list = list(input_dict.items())
    random.shuffle(item_list)
    return dict(item_list)


def set_quiz_category(category_dict):
    print("\nCHOOSE A CATEGORY")
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
            return shuffle_dictionary(history_questions)
        case "b":
            return shuffle_dictionary(geography_questions)
        case "c":
            return shuffle_dictionary(science_questions)
        case "d":
            return shuffle_dictionary(music_questions)


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
time.sleep(DEFAULT_SLEEP)
questions = set_quiz_category(category_options)
time.sleep(DEFAULT_SLEEP)
show_instructions()
time.sleep(DEFAULT_SLEEP)

for key in questions:
    correct_answer = questions[key][0]
    options = ask_question(key, questions)
    player_answer = input("Enter choice: ").lower()
    result = check_answer(player_answer, correct_answer, options)
    print_feedback(result, correct_answer)
    score += result

print("\nYour score: {0}/{1}".format(score, len(questions)))

### END SECTION - MAIN ###
