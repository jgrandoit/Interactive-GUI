import tkinter as tk
root = tk.Tk()
root.title("Guessing Game")
def check(answer):
    if answer[-1] == "*":
        print("Right, it is {}".format(answer[:-1]))
    else:
        print("Wrong answer! Try Again!")
class Question:
    def __init__(self, question):
        self.question = question
        self.label = tk.Label(root, text=question)
        self.label.pack()



class Answer:
    def __init__(self, answer):
        self.answer = answer
        self.label = tk.Label(root, text=answer[:-1])
        self.label.bind("<Button-1>", lambda x: check(answer)) 
# lambda allows data to be sent button object
        self.label.pack()

# Place the question and answers here, separated by comma
# right answer ends with *, wrong one ends with –

q = """What orange vegetable do rabbits like to eat?, Carrots*, Broccoli-, Oranges-,
What number comes after 9?, 4-, 10*, 8-, 
What language do people speak in Germany?,French-,Russian-,German*,
What color is a banana?, orange-,yellow*,red-,
How many sides does a square have?, 2-, 3-.4* 
"""
q = q.splitlines()
q2 = []
for line in q:
    q2.append(line.split(","))
q = q2
for quest in q:
    Question(quest[0])
    for ans in quest[1:]:
        Answer(ans)
root.mainloop()
