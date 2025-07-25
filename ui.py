from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self , quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20 , pady=20 , background=THEME_COLOR)

        self.score_label = Label(text=f"Score : {0}" , fg="white" , bg=THEME_COLOR)
        self.score_label.grid(column=1 , row=0)

        self.canva = Canvas(width=300 , height=250 , bg="white")
        self.question_text =  self.canva.create_text(150 , 125 , text="Some Question Text"
                            , width= 280
                            , fill=THEME_COLOR
                            , font=("Arial" , 20, "italic"))
        self.canva.grid(row=1 , column= 0 , columnspan=2 , pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_Button = Button(image=self.true_image , highlightthickness=0 , command= self.true_pressed )
        self.true_Button.grid(row=2 ,column=0)
        self.false_button = Button(image=self.false_image , highlightthickness=0  , command=self.false_pressed)
        self.false_button.grid(row=2 , column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canva.itemconfig(self.question_text , text = q_text)
        else:
            self.canva.itemconfig(self.question_text , text = "You have Answered all questions")
            self.false_button.config(state="disabled")
            self.true_Button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self , is_right : bool):
        if is_right :
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000 , self.get_next_question)
