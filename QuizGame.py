
quiz = []


def ask():
    num_questions = int(input("How many questions? "))

    for i in range(num_questions):
        print(f"\nQuestion {i + 1}:")
        question = input("Enter the question: ")
        options = []
        for j in range(4):
            opt = input(f"Option {j + 1}: ")
            options.append(opt)
        correct = int(input("Enter the number of the correct option (1-4): ")) - 1

        quiz.append({
            "question": question,
            "options": options,
            "answer": correct
        })


def start_quiz():
    print("\n--- Quiz Start ---\n")
    score = 0

    for q in quiz:
        print(q["question"])
        for i, opt in enumerate(q["options"]):
            print(f"{i + 1}. {opt}")
        ans = int(input("Your answer (1-4): ")) - 1
        if ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong.\n")

    print(f"Final score: {score}/{len(quiz)}")


ask()
start_quiz()

