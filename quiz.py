question_data = [
    {
        "category" : "Science : Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False"
        "Incorrect_answer":[
            "True"
        ]
    },
    {
        "category" : "Science : Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True"
        "Incorrect_answer":[
            "False"
        ]
    },
    {
        "category" : "Science : Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first computer 64-bit processor.",
        "correct_answer": "True"
        "Incorrect_answer":[
            "False"
        ]
    },
    {
        "category" : "Science : Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "HTML stand for Hypertext Markup Language",
        "correct_answer": "True"
        "Incorrect_answer":[
            "False"
        ]
    },
            
]



from question_model import question 
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = question (question_text, question_answer)
    
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
     quiz.next_questions()

print("YOU HAVE COMPLETED THE QUIZ")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


class Question:

    def __init(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer




class quizbrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print ("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
