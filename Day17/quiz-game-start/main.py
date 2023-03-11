#from data import question_data
from data1 import question_data
from question_model import Questions
from quiz_brain import QuizBrain
question_bank= []

for question in question_data:
    #question_text = question["text"]
    question_text = question["question"]
    #question_answer = question["answer"]
    question_answer = question["correct_answer"]
    new_question =Questions(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz successfully")
print(f"Your final score was {quiz.score}/{quiz.question_number}  ")


#QuizBrain(question_bank)
#print(question_bank[0].text)





#     print(question_answer)
#     #q_bank.append()
#     #print(question["text"])
# #print(q_bank)
