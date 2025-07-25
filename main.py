from question_model import Question
from quiz_brain import QuizBrain
from ui import *
import requests

parameters  = {
    "amount" : 10,
    "type" : "boolean",
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean" , params = parameters)
response.raise_for_status()
question_data = response.json()
question_data = question_data["results"]


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

