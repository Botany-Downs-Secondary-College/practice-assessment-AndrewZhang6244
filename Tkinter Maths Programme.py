from tkinter import* 
from random import*
root = Tk()
root.title("Welcome to my app")
root.geometry("400x275+500+0")  
frame1 = Frame(root)
frame2 = Frame(root)
i = 1


TitleLabel = Label(frame1, bg = "orange" , fg = "white", width = 35, padx  = 20, pady = 20, text = "Welcome to Math Quiz", font=("Times", "14", "bold italic"))
TitleLabel.grid(columnspan = 2) 
def Screen1():
    global frame1
    global frame2
    frame2.grid_remove()
    frame1.grid(row=0, column=0)
    
    rb1 = Radiobutton(frame1, width = 20, value = 1, text = "Easy", anchor = W)
    rb1.grid(column = 0, row = 8)
    rb2 = Radiobutton(frame1, width = 20, value = 2, text = "Medium", anchor = W)
    rb2.grid(column = 0 , row = 9)
    rb3 = Radiobutton(frame1, width = 20, value = 3, text = "Hard", anchor = W)
    rb3.grid(column = 0, row = 10)
    button1 = Button(frame1, text = "Next", anchor = W, command = Screen2)
    button1.grid(column = 0, row = 11) 
    label2 = Label(frame1, text = "Name", width = 20, font=("Times", "14", "bold italic"))
    label2.grid(column = 0, row = 3)
    textbox1 = Entry(frame1, width = 20)
    textbox1.grid(column = 0, row = 7)
    label3 = Label(frame1, text = "Age", width = 20, font=("Times", "14", "bold italic"))
    label3.grid(column = 0, row = 6)
    textbox2 = Entry(frame1, width = 20)
    textbox2.grid(column = 0, row = 5) 
    
def Screen2():
    global frame1
    global frame2
    frame1.grid_remove()
   
    frame2.grid(row=0, column=0)
    

    def next_question():
        global i
        global x
        global y
        
        x = randrange(10)
        y = randrange(10)    
        
        question_text = str(x) + " + " + str(y) + " = "
        problem_label.configure(text = question_text)
        ans_entry.delete(0, END)
        ans_entry.focus()
        
        lbl_question = Label(frame2, width = 10, padx = 40, pady = 10, font = ("Times", "15", "bold italic"), text = "Question " + str(i))
        lbl_question.grid(row=0, column=0)
        i = i + 1
        
    def check_answer():
        answer = x + y
        try:
            user_answer = int(ans_entry.get())
            
            if user_answer == answer:
                feedback.configure(text = "Correct!")
            elif user_answer == "":
                feedback.configure(text = "Please answer the question")
            else:
                feedback.configure(text = "Wrong!")
                ans_entry.delete(0, END)
                next_question()
        except ValueError:
            feedback.configure(text = "That is not a number!")
            ans_entry.delete(0, END)
            ans_entry.focus()
     
            
    feedback = Label(frame2, text = "", height = 3)
    feedback.grid(row=7, column=0)
    
    question_label = Label(frame2, width = 10, padx = 40, pady = 10, font = ("Times", "15", "bold italic"))
    question_label.grid(row=0, column = 0)
    
    problem_label = Label(frame2, width = 10, padx = 40, pady = 10, text = "", font = ("Times", "15", "bold italic"))
    problem_label.grid(row=1, column=0, sticky = W)
    
    ans_entry = Entry(frame2, width=15)
    ans_entry.grid(row=2, column=0)
    
    check_btn = Button(frame2, text = "Check your answer", command = check_answer, relief = RIDGE)
    check_btn.grid(row=3, column=0)
    
    next_btn = Button(frame2, text = "Next", command = next_question, relief = RIDGE)
    next_btn.grid(row=4, column=0)
    
    home_btn = Button(frame2, text = "Home", anchor = W, command = Screen1, relief = RIDGE)
    home_btn.grid(row=5, column=0)   
    
    next_question()
Screen1()
root.mainloop()
