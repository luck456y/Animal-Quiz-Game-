def check_guess(question, answer, attempts=3):

    for attempt in range(attempts):
        guess = input(question + " ").strip()
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            return 1
        elif attempt < attempts - 1:
            print("Sorry, wrong answer. Try again!")
    print(f"The correct answer is: {answer}")
    return 0

def main():

    questions = {
        "Which bear lives at the North Pole?": "polar bear",
        "Which is the fastest land animal?": "cheetah",
        "Which is the largest animal?": "blue whale",
    }
    
    print("Guess the Animal!")
    score = sum(check_guess(question, answer) for question, answer in questions.items())
    
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
