from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = '#375362'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz game')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text = 'Score: 0', fg='white', bg = THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width = 290,
                                                     text = 'Question Text',
                                                     fill = THEME_COLOR,
                                                     font = ('Arial', 20, 'italic' )
                                    )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file = 'images/true.png')
        self.true_button = Button(image = true_img, command = self.pressed_true, highlightthickness = 0)
        self.true_button.grid(row = 2, column = 1)

        false_img = PhotoImage(file = 'images/false.png')
        self.false_button = Button(image = false_img, command = self.pressed_false, highlightthickness = 0)
        self.false_button.grid(row = 2, column = 0)
        self.get_next_question()
        self.window.mainloop()

    def change_canvas_bg(self, answer):
        if answer:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000,self.get_next_question)


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            score = self.quiz.score
            self.score_label.config(text = f'Score: {score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f'You finished the quiz.\nYour final score is {self.quiz.score}.')
            self.true_button.config(state = 'disabled')
            self.false_button.config(state='disabled')

    def pressed_true(self):
        answer = self.quiz.check_answer('True')
        self.change_canvas_bg(answer)

    def pressed_false(self):
        answer = self.quiz.check_answer('False')
        self.change_canvas_bg(answer)
