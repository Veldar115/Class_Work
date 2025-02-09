import tkinter
Right_Answers = []
def Save_Answers(Answer):
    Right_Answers.append(Answer)
def Next_Question(Answer):
    Save_Answers(Answer)
    clear_all_inside_frame()
    render_frame_question_with_options()
    print(Right_Answers)
def render_frame_question_with_options():
    frame = tkinter.Frame(borderwidth=1, relief="solid")
    Label = tkinter.Label(frame, text=f"{list(Questiions.keys())[0]}", background="#FFCDD2", foreground="#B71C1C")
    Label.place(x=600, y = 100)
    for c in range(2): Root.columnconfigure(index=c, weight=1)
    for r in range(2): Root.rowconfigure(index=r, weight=1)
    I_Index = 0
    for r in range(2):
        for c in range(2):
            btn_Text = Answers[I_Index]
            btn = tkinter.Button(frame, text= f"{btn_Text}", command= lambda: Next_Question(Answers[I_Index])) #вызывать функцию как - то по другому, ну все 
            btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky="sew")
            I_Index += 1
    frame.pack(anchor="center", padx=5, pady=5, expand=True)
    return frame
def clear_all_inside_frame():
    # Iterate through every widget inside the frame
    for widget in frame.winfo_children():
        widget.destroy()  # deleting widget
Questiions = {"Second form of PUT":("Put","Putten","Pot","Pyt")}
Answers = Questiions["Second form of PUT"]
Root = tkinter.Tk() 
Root.title()
Root.geometry("1200x1200")
frame = render_frame_question_with_options()

Root.mainloop()