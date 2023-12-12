import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        # Load background image
        background_image = tk.PhotoImage(file=r"C:\Users\Admin\C TUTORIALS\quiz1.png")
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.score = 0
        self.current_question = 0

        # Questions data
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "Madrid", "Rome"],
                "correct_option": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_option": "Mars"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Panda"],
                "correct_option": "Blue Whale"
            }
        ]

        # Label to display the question
        self.label_question = tk.Label(root, text="", font=("Helvetica", 16), bg="#ffffff")
        self.label_question.pack(pady=20)

        # Radio buttons for options
        self.radio_var = tk.StringVar()
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.select_option,
                                          font=("Helvetica", 12), bg="#ffffff")
            self.radio_buttons.append(radio_button)
            radio_button.pack(pady=10)

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Helvetica", 14), bg="#4CAF50", fg="white")
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label_question.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)

            self.radio_var.set("")
        else:
            self.show_result()

    def select_option(self):
        selected_option = self.radio_var.get()
        correct_option = self.questions[self.current_question]["correct_option"]

        if selected_option == correct_option:
            self.score += 1

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "_main_":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()