from tkinter import *
from tkinter import ttk
from Grader import runpoints
from class_password import password
pass_word = '' #the string that will eventually update to be the inputted password
window = Tk() #creation of the window
window.geometry("10000x10000")
welcome = Label(window, text = "Welcome to the passcode grader!!", font = ("Arial 52 bold")) # welcome message
welcome.pack()
Inputpasscode = Label(window, text = "Input passcode here:", font = ("Arial 52 bold")) #input message
Inputpasscode.pack()
passwrd = StringVar() #variable where the entry will be stored
def printinput(*args): #runs when continue is pressed. Takes in the two global variables and turns the StringVar of passwrd into the string pass_word that will be used later
   global passwrd 
   global pass_word
   word = passwrd.get() #gets the password
   pass_word = word #assigns to the global variable
   if word != '':
      window.destroy()#kills the window to then display the result
passwrd = Entry(window, width = 500)
passwrd.focus_set()
passwrd.pack()
Button(window, text= "continue",width= 20, command= printinput ).pack(pady=20)
window.mainloop()

p2 = password(pass_word)

passwords_grade = runpoints(pass_word) #assigns a variable to the total number of points
win2 = Tk() #creates second window
win2.geometry("10000x10000")
#the next if statements all control different outcomes based on the output of the password
if passwords_grade>=75: 
   win2.configure(bg = "green2") 
   great = Label(win2, text = "Great! :))))", font = ("Arial 60 bold"))#changes text of the screen
   great.pack()
elif 50<=passwords_grade<75:
   win2.configure(bg = "yellow")
   alright = Label(win2, text = "Alright :)", font = ("Arial 60 bold"))#changes text of the screen
   alright.pack()
elif 25<=passwords_grade<50:
   win2.configure(bg = "orange")
   needsimp = Label(win2, text = "Needs Improvement :|", font = ("Arial 60 bold"))#changes text of the screen
   needsimp.pack()
elif 1<=passwords_grade<25:
   win2.configure(bg = "brown")
   awful = Label(win2, text = "Awful :(", font = "Arial 60 bold")#changes  text of the screen
   awful.pack()
elif passwords_grade == 0:
   labelleak = Label(win2, text = "Oh No!!! :((( Your password was found in a data leak!", font = ("Arial 52 bold"))#changes color and text of the screen
   labelleak.pack()
   labelleak2 = Label(win2, text = "you HAVE to change your passcode", font = "Arial 60 bold")#changes color and text of the screen for if their passcode is amung the most common
   labelleak2.pack()
   win2.configure(bg = "red")
passwords_grade = str(passwords_grade)
labelfinal = Label(win2, text = "your score is "+ passwords_grade, font = ("Arial 52 bold ")) #returns their score out of 100
labelfinal.pack()
#these for loops provide suggestions on how they can improve their code
if p2.num_numbers()<3:
   labelwork0 = Label(win2, text = "you need more special characters", font = ("Arial 22 bold"))
   labelwork0.pack()
if p2.length() <10 :
   labelwork1 = Label(win2, text = "you need it to be longer", font = ("Arial 22 bold"))
   labelwork1.pack()
if p2.num_capital_letters() <3:
   labelwork3 = Label(win2, text = "you need more capital letters", font = ("Arial 22 bold"))
   labelwork3.pack()
if p2.num_special_char() <2:
   labelwork4 = Label(win2, text = "you need more numbers", font = ("Arial 22 bold"))
   labelwork4.pack()
win2.mainloop()
#https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/?ref=lbp
#https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter
#https://stackoverflow.com/questions/15495559/taking-input-from-the-user-in-tkinter
#https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
#https://www.educative.io/answers/how-to-change-a-tkinter-window-background-color
