#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

trivurl="https://opentdb.com/api.php?amount=10"

import requests

def main():
    # Fetch trivia questions
    response = requests.get(trivurl)
    data = response.json()
    
    # Check if the response contains questions
    if "results" not in data:
        print("Questions not found error.")
        return

    # Separate and ask each question
    for index, question_data in enumerate(data["results"], start=1):
        print(f"Question {index}:")
        print(question_data["question"])  # Print the questions

        # Print incorrect answers
        for i, answer in enumerate(question_data["incorrect_answers"], start=1):
            print(f"{i}. {answer}")
        # Print correct answers
        correct_index = len(question_data["incorrect_answers"]) + 1
        print(f"{correct_index}. {question_data['correct_answer']}")
        
        # Ask user for input
        user_answer = input("What is your guess?")

        # Check if the user's answer is correct
        if int(user_answer) == correct_index:
            print("Correct!")
        else:
            print("Incorrect! The correct answer was: ", question_data["correct_answer"])
        
        print()
        

# data will be a python dictionary rendered from your API link's JSON!
    print(data)
if __name__ == "__main__":
    main()

