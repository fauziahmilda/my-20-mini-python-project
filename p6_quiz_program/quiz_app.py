# a dictionary that store questions and answers
# have a variable that tracks the score of the player
# loop  through the dictionary using the key values pairs
# display each questions to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is complete

quiz = {
    "question1": {
        "question": "what is the formula for mechanical energy",
        "answer": "EM = EK + EP"
    },
    "question2": {
        "question": "What is formula of gravity?",
        "answer": "F = G x (m1 x m2)/r2"
    },
    "question3": {
        "question": "What is the unit of force?",
        "answer": "Newton"
    },
    "question4": {
        "question": "Who find gravitaion laws?",
        "answer": "Isaac Newton"
    },
    "question5": {
        "question": "Who find relativity laws?",
        "answer": "Albert Einstain"
    },
    "question6": {
        "question": "Who find Coservation Laws of Energy?",
        "answer": "James Prescott Joule"
    },
    "question7": {
        "question": "2x+8=12",
        "answer": "2"
    },
    "question8": {
        "question": "17+4h+2=1-5h, h = ?",
        "answer": "-2"
    },
}
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print(f"Score = {score}")
        print("")
    else:
        print('Wrong!')
        print(f"The correct answer is {value['answer']}")
        print(f"Score = {score}")
        print("")

print(f"You got {score} out of {quiz.__len__()} questions correctly")
