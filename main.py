from question import Question
from data import question_data
from quiz_logic import QuizBrain
from ui import QuizInterface

# ----------------> Loop through all the data and create the questions <----------------- #
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# --------------------> Run the app <------------------ #
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# -------------------> Informative only > Console <-------------------- #
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
