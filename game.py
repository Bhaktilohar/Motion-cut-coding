# Basic Quiz Game

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("Your answer (enter the option number): ")
    return answer == str(correct_option)

def main():
    questions = [
        {
         
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct_option": 3
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
            "correct_option": 1
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 3
        }
    ]
    
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    print(f"Your final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    main()

    
