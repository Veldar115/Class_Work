import tkinter
class SampleApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self._frame = None
        self.UserAnswers = []
        self.switch_frame(FrameQuestion1)
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    def AddUserAnswer(self, Answer):
        self.UserAnswers.append(Answer)


class FrameQuestion1(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        tkinter.Label(self, text= "Third form of Build", background="#FFCDD2", foreground="#B71C1C").pack()
        #for c in range(2): master.columnconfigure(index=c, weight=1)
        #for r in range(2): master.rowconfigure(index=r, weight=1)
        Answers = ("Boult","Built", "Builden", "Boulght")
        I_Index = 0
        for r in range(2):
            for c in range(2):
                btn_Text = Answers[I_Index]
                btn = tkinter.Button(self, text= f"{btn_Text}", command= lambda:(master.switch_frame(FrameQuestion2),master.AddUserAnswer(btn_Text))).pack()
                #некоректно
                #btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky="sew")
                I_Index += 1


class FrameQuestion2(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        tkinter.Label(self, text= "Second form of PUT", background="#FFCDD2", foreground="#B71C1C").pack()
        #for c in range(2): master.columnconfigure(index=c, weight=1)
        #for r in range(2): master.rowconfigure(index=r, weight=1)
        Answers = ("Put","Putten","Pot","Pyt")
        I_Index = 0
        for r in range(2):
            for c in range(2):
                btn_Text = Answers[I_Index]
                btn = tkinter.Button(self, text= f"{btn_Text}", command= lambda:master.switch_frame(FrameQuestion3)).pack()
                #некоректно
                #btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky="sew")
                I_Index += 1


class FrameQuestion3(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        tkinter.Label(self, text= "Second form of Swim", background="#FFCDD2", foreground="#B71C1C").pack()
        #for c in range(2): master.columnconfigure(index=c, weight=1)
        #for r in range(2): master.rowconfigure(index=r, weight=1)
        Answers = ("Swam","Swimmen", "Swum", "Swim")
        I_Index = 0
        for r in range(2):
            for c in range(2):
                btn_Text = Answers[I_Index]
                btn = tkinter.Button(self, text= f"{btn_Text}", command= lambda:print(master.UserAnswers)).pack()
                #некоректно
                #btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky="sew")
                I_Index += 1

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()