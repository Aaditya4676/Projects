import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text-to-speech")
root.geometry("1000x500+100+200")
root.resizable(False,False)
root.configure(bg="#302066")

engine = pyttsx3.init()

def speaknow():
	text = text_area.get(1.0, END)
	gender = gender_select.get()
	speed = speed_select.get()
	voices = engine.getProperty('voices')
	
	def setvoice():
		if (gender == 'Male'):
			engine.setProperty('voice', voices[0].id)
			engine.say(text)
			engine.runAndWait()
		else:
			engine.setProperty('voice', voices[1].id)
			engine.say(text)
			engine.runAndWait()
	if (text):
		if(speed == "Fast"):
			engine.setProperty('rate',250)
			setvoice()
		elif(speed == 'Normal'):
			engine.setProperty('rate',150)
			setvoice()
		else:
			engine.setProperty('rate',60)
			setvoice()

def download():
	text = text_area.get(1.0, END)
	gender = gender_select.get()
	speed = speed_select.get()
	voices = engine.getProperty('voices')
	
	def setvoice():
		if (gender == 'Male'):
			engine.setProperty('voice', voices[0].id)
			path = filedialog.askdirectory()
			os.chdir(path)
			engine.say(text)
			engine.save_to_file(text,'text.mp3')
			engine.runAndWait()
		else:
			engine.setProperty('voice', voices[1].id)
			path = filedialog.askdirectory()
			os.chdir(path)
			engine.say(text)
			engine.save_to_file(text,'text.mp3')
			engine.runAndWait()
	if (text):
		if(speed == "Fast"):
			engine.setProperty('rate',250)
			setvoice()
		elif(speed == 'Normal'):
			engine.setProperty('rate',150)
			setvoice()
		else:
			engine.setProperty('rate',60)
			setvoice()


################

icon = PhotoImage(file="microphone.png")
root.iconphoto(False,icon)

Top_side = Frame(root,bg="black",width = 1000,height = 100)
Top_side.place(x=0,y=0)

Logo = PhotoImage(file="microphone.png")
Label(Top_side,image=Logo,bg="black").place(x=10,y=5)


Label(Top_side,text="Text to Speech",font = "Calisto 20 bold",bg="black",fg="white").place(x=100,y=30)

##############

text_area = Text(root,font="Robote 20",bg="gray",relief=GROOVE,wrap=WORD)
text_area.place(x=25,y=130,width=500,height=200)


Label(root,text="VOICE",font = "arial 15 bold",bg="#302066",fg="Black").place(x=580,y=150)
Label(root,text="SPEED",font = "arial 15 bold",bg="#302066",fg="Black").place(x=780,y=150)


val_gender = ['Male', 'Female']
gender_select = Combobox(root,values=val_gender,font="arial 14", state = 'r',width = 10)
gender_select.place(x=550,y=200)
gender_select.set('Male')

val_speed = ['Fast', 'Normal', 'Slow']
speed_select = Combobox(root,values=val_speed,font="arial 14", state = 'r',width = 10)
speed_select.place(x=750,y=200)
speed_select.set('Normal')


#img_icon = PhotoImage(file="microphone.png")
btn = Button(root,text="Speak",compound=LEFT,width=10,font = "arial 15 bold",command = speaknow)
btn.place(x=550,y=280)

#img_icon1 = PhotoImage(file="microphone.png")
save = Button(root,text="Save",compound=LEFT,width=10,font = "arial 15 bold",command = download)
save.place(x=750,y=280)


root.mainloop()

