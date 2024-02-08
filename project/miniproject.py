#!/usr/bin/env python3


import random

questions = [
    {"category": "Mario Bros.", "questions": [
        {"question": "Who is Mario's brother?", "options": {"a": "Luigi", "b": "Yoshi", "c": "Bowser", "d": "Toad"}, "answer": "a"},
        {"question": "What is the name of Mario's main enemy?", "options": {"a": "Luigi", "b": "Yoshi", "c": "Bowser", "d": "Toad"}, "answer": "c"},
        {"question": "What does Mario use to defeat enemies?", "options": {"a": "Hammer", "b": "Wrench", "c": "Sword", "d": "Fireball"}, "answer": "d"},
    ]},
    {"category": "Sonic the Hedgehog", "questions": [
        {"question": "What is the name of Sonic's sidekick?", "options": {"a": "Knuckles", "b": "Tails", "c": "Shadow", "d": "Amy"}, "answer": "b"},
        {"question": "Who is Sonic's arch-enemy?", "options": {"a": "Dr. Robotnik", "b": "Knuckles", "c": "Shadow", "d": "Amy"}, "answer": "a"},
        {"question": "What color are Sonic's shoes?", "options": {"a": "Blue", "b": "Red", "c": "Green", "d": "Yellow"}, "answer": "a"},
    ]},
    {"category": "The Legend of Zelda", "questions": [
        {"question": "What is the name of the princess in The Legend of Zelda?", "options": {"a": "Zelda", "b": "Peach", "c": "Daisy", "d": "Rosalina"}, "answer": "a"},
        {"question": "What is the main weapon used by Link in The Legend of Zelda?", "options": {"a": "Sword", "b": "Bow", "c": "Axe", "d": "Spear"}, "answer": "a"},
        {"question": "What is the name of the kingdom where most of The Legend of Zelda games take place?", "options": {"a": "Hyrule", "b": "Mushroom Kingdom", "c": "Dream Land", "d": "Skyloft"}, "answer": "a"},
    ]},
]

def classic_video_game_trivia():
    print("Welcome to Classic Video Game Trivia!")
    print("Please choose a category:")
    print("1. Mario Bros.")
    print("2. Sonic the Hedgehog")
    print("3. The Legend of Zelda")

    while True:
        try:
            category = int(input("Enter the number of your chosen category: "))
            if category < 1 or category > 3:
                print("Invalid input. Please enter a number between 1 and 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    questions_asked = set()
    while len(questions_asked) < len(questions[category - 1]['questions']):
        question_index = random.randint(0, len(questions[category - 1]['questions']) - 1)
        if question_index in questions_asked:
            continue
        questions_asked.add(question_index)
        question_data = questions[category - 1]['questions'][question_index]
        print(f"\nCategory: {questions[category - 1]['category']}")
        print(f"Question: {question_data['question']}")
        for option, value in question_data['options'].items():
            print(f"{option}) {value}")
        while True:
            answer = input("Enter your answer (a, b, c, or d): ").lower()
            if answer not in ['a', 'b', 'c', 'd']:
                print("Invalid input. Please enter a, b, c, or d.")
            else:
                break
        if answer == question_data['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question_data['options'][question_data['answer']]}.")

    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        classic_video_game_trivia()
    else:
        print("Thank you for playing Classic Video Game Trivia!")


if __name__ == "__main__":
    classic_video_game_trivia()

