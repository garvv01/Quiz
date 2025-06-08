from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score: 0", bg=THEME_COLOR)
        self.label.grid(column=1, row=0, pady=20)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, text="Insert text here", fill="black", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        yes_image = PhotoImage(file="../quizzler-app-start/images/true.png")
        no_image = PhotoImage(file="../quizzler-app-start/images/false.png")
        self.yes_button = Button(image=yes_image, highlightthickness=0, command=lambda: self.check_ans("True"))
        self.yes_button.grid(column=0, row=2, pady=20)
        self.no_button = Button(image=no_image, highlightthickness=0, command=lambda: self.check_ans("False"))
        self.no_button.grid(column=1, row=2, pady=20)
        self.q_text = ""
        self.score = 0
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=self.q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've completed the quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def check_ans(self, user_answer):
        is_correct = self.quiz.check_answer(user_answer)
        if is_correct:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)