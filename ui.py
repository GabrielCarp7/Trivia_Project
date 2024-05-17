from tkinter import *
from quiz_logic import QuizBrain
"""

Uses tkinter to create the ui for the app

"""


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window Creation
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Taking the images
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")

        # Text Score
        self.score = Label(text="Score: 0", font=("Arial", 15), background=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        # Canvas Creation
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.quizz_text = self.canvas.create_text(150, 125, text="Are you ready for the quizz?",
                                                  font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons Creation
        self.true_button = Button(text="", image=self.true, background=THEME_COLOR, highlightthickness=0,
                                  command=self.true_button)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(text="", image=self.false, background=THEME_COLOR, highlightthickness=0,
                                   command=self.false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quizz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quizz_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        elif not is_right:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
