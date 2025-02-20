import tkinter
User_Answers = []
#Right_Answers = ["Put","Swam","Built","Woken","Slept","Played", "Seen", "Run"]
Right_Answers = ["Put","Swam"]
def Render_Result():
    Procent_Right_Answers = Check_Answers(User_Answers, Right_Answers)
    frame = tkinter.Frame(borderwidth=1, relief="solid")
    Label = tkinter.Label(frame, text=f"{Procent_Right_Answers}", background="#FFCDD2", foreground="#B71C1C")
    Label.place(x=600, y = 100)
    frame.pack(anchor="center", padx=5, pady=5, expand=True)
    return frame
def Save_Answers(Answer):
    User_Answers.append(Answer)
def Next_Question(Answer, Previous_Question_Number):
    Save_Answers(Answer)
    clear_all_inside_frame()
    Current_Question_Number = Previous_Question_Number + 1
    if Current_Question_Number >= len(Right_Answers):
        Render_Result()
    else:
        render_frame_question_with_options(Current_Question_Number)
    print(User_Answers)
def render_frame_question_with_options(Question_Number):
    Answers = list(Questiions.values())[Question_Number]
    frame = tkinter.Frame(borderwidth=1, relief="solid")
    Label = tkinter.Label(frame, text=f"{list(Questiions.keys())[Question_Number]}", background="#FFCDD2", foreground="#B71C1C")
    Label.place(x=600, y = 100)
    for c in range(2): Root.columnconfigure(index=c, weight=1)
    for r in range(2): Root.rowconfigure(index=r, weight=1)
    I_Index = 0
    for r in range(2):
        for c in range(2):
            btn_Text = Answers[I_Index]
            btn = tkinter.Button(frame, text= f"{btn_Text}", command= lambda: Next_Question("Put" , Question_Number))     
            #некоректно
            btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky="sew")
            I_Index += 1
    #frame.pack(anchor="center", padx=5, pady=5, expand=True)
    return frame
def Check_Answers(User_Answers, Right_Answers):
    a = 0
    for i in range(len(Right_Answers)):
        if Right_Answers[i] == User_Answers[i]:
            a += 1
    Procent_Right_Answers = a / len(Right_Answers) * 100
    return Procent_Right_Answers
def clear_all_inside_frame():
    # Iterate through every widget inside the frame
    #for widget in frame.winfo_children():
        #widget.destroy()  # deleting widget
    frame.destroy()
Questiions = {"Second form of PUT":("Put","Putten","Pot","Pyt"),
               "Second form of Swim":("Swam","Swimmen", "Swum", "Swim"),
                 "Third form of Build":("Boult","Built", "Builden", "Boulght"),
                   "Second form of Wake":("Woke","Woken", "Wokn", "Wake"),
                   "Third form of Sleep":("Sleep","Slep", "Slept", "Sleepen"),
                     "Second form of Play":("Played","Playn", "Play", "Pluy"),
                       "Third form of See":("Saw","Seen", "See", "Seenen"),
                         "Third form of Run":("Runnen","Ran", "Run", "Runn")}
Root = tkinter.Tk() 
Root.title()
Root.geometry("1200x1200")
frame = render_frame_question_with_options(0)


Root.mainloop()
#TODO запись ответов, размножение фреймов