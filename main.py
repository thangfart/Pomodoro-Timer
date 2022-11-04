from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MYPHOTO_PATH = "/Users/philipthangngat/Dev/SpareTime/\
100DaysOfCodingPython/day28_tkinter_pomodoro/tomato.png"
STATUS_BREAK = "BREAK"
STATUS_WORK = "WORK"
STATUS_DEFAULT = "TIMER"
CLOCK_DEFAULT = "25:00"
LONG_BREAK = 4 # 30MIN BREAK [s]
SHORT_BREAK = 1 # 5MIN BREAK [s]
WORK_TIME = 2 #WORK TIME [s]
MINUTE_DEFAULT = "00"
HOUR_DEFAULT = "00"
SECOND_DEFAULT = "00"


class PomodoroGUI(tk.Tk):
    #self is master
    #show_window is what you see POV
    #gonna use 3x3 grid
    def __init__(self):
        super().__init__()
        #initialize main window and frame of tomato
        self.geometry("400x400")
        self.title("Pomodoro Fuck")
        self.config(padx=100,pady=50)
        self.resizable(False,False)
        self.nr_of_cycles = 0 #keeps track of how many mini periods there has been
        self.time_work = WORK_TIME
        self.short_time_off = SHORT_BREAK
        self.long_time_off = LONG_BREAK
        #initialize the state str to default value "BREAK"
        self.state_strVar = StringVar()
        self.state_strVar.set(STATUS_DEFAULT)

        #initialize the time formats to StringVars, set to h:m:s = 00:30:00
        self.hour_strVar = StringVar()
        self.minute_strVar = StringVar()
        self.second_strVar = StringVar()
        self.hour_strVar.set(HOUR_DEFAULT)
        self.minute_strVar.set(MINUTE_DEFAULT)
        self.second_strVar.set(SECOND_DEFAULT)

        #setup canvas for the tomato pic
        self.photo_img = tk.PhotoImage(file=MYPHOTO_PATH)
        self.canvas = Canvas(self,width=200,height=224)
        self.canvas.create_image(102,112,image=self.photo_img)
        self.canvas.grid(column=1,row=1,rowspan=3,columnspan=3)

        #setup labels
        self.hours_show_label = tk.Label(self,textvariable=self.hour_strVar,width=2)
        self.minutes_show_label = tk.Label(self,textvariable=self.minute_strVar,width=2)
        self.seconds_show_label = tk.Label(self,textvariable=self.second_strVar,width=2)

        #place labels
        self.hours_show_label.place(x=70,y=130)
        self.minutes_show_label.place(x=100,y=130)
        self.seconds_show_label.place(x=130,y=130)

        #setup buttons
        self.start_btn = tk.Button(self, text="Start", command=self.startTimer) 
        self.reset_btn = tk.Button(self, text="Reset", command=self.resetAll)

        #place buttons
        self.start_btn.place(x=10,y=250)
        self.reset_btn.place(x=150,y=250)

        #self.txt = tk.Text(self,command=self.startTimer)

    def countDown(self, total_secs) -> None:
        """
        This counts down from secs seconds and prints the out the remaining time for each iteration
        """
        print(f"input to counDown() [s]: {total_secs}")
        while total_secs > -1:
            minutes,seconds = divmod(total_secs,60)

            hours = 0
            if minutes>60:
                hours,minutes = divmod(minutes,60)

            self.hour_strVar.set("{0:2d}".format(hours))
            self.minute_strVar.set("{0:2d}".format(minutes))
            self.second_strVar.set("{0:2d}".format(seconds))
            self.update()
            time.sleep(1)

            #decrease every sec
            total_secs -= 1

    def resetAll(self) -> None:
        """
        Set all string variables to default value, also set
        the value holding nr of cycles to zero
        """
        self.state_strVar.set(STATUS_DEFAULT)
        self.hour_strVar.set(HOUR_DEFAULT)
        self.minute_strVar.set(MINUTE_DEFAULT)
        self.second_strVar.set(SECOND_DEFAULT)
        self.nr_of_cycles = 0

    def startTimer(self) -> None:
        """
        This method starts the actual timer method self.timerMechanics(self,total_secs)
        with correct input derived from the value of self.nr_of_cycles attribute.
        """

        
        finished = False
        while not finished:
            self.nr_of_cycles += 1
        
            if self.nr_of_cycles % 8 == 0: #Long break time
                self.countDown(LONG_BREAK)
                self.state_strVar.set(STATUS_BREAK)

            elif self.nr_of_cycles % 2 == 0: #Short break
                self.countDown(SHORT_BREAK)
                self.state_strVar.set(STATUS_BREAK)
                self.workPopUp()

            else: #work
                self.countDown(WORK_TIME)
                self.state_strVar.set(STATUS_WORK)
                self.restPopUp()

            if self.nr_of_cycles == 8:
                finished = True
                messagebox.showinfo("Alert","Youre done, click reset start over")
            


    def workPopUp(self) -> None:
        """
        Method makes sure the GUI alerts the user with a popup window
        that it´s time to WORK. This method is to be called by startTimer() method.
        """
        messagebox.showinfo("Status Info","Get your ass to work cocksuckah")

    def restPopUp(self) -> None:
        """
        Method makes sure the GUI alerts the user with a popup window
        that it´s time to for a BREAK. This method is to be called by startTimer() method.
        """
        messagebox.showinfo("Status Info","You can have a break now")


if __name__ == "__main__":
    app = PomodoroGUI()
    app.mainloop()
    
