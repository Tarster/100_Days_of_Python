import sys
sys.path.append("Data\Day17")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = [] 
for object_values in question_data:
    question_bank.append(Question(object_values["text"],object_values["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.complete_quiz_popup()