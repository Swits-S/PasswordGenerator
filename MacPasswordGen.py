"""
Password generator v1.0
Jake Gourley
2020
"""
import yagmail
import random
import datetime
from tkinter import *
from tkinter.messagebox import showinfo
import os
from time import sleep
import webbrowser
from os.path import expanduser


# Modules
# defaults setting module
def restore():
    f = open("config.txt", "w")
    f.write("8")
    f.write("\n")
    f.write("TrueA")
    f.write("\n")
    f.write("TrueB")
    f.write("\n")
    f.write("TrueC")
    f.write("\n")
    f.write("TrueD")
    f.write("\n")
    f.write("Blank")
    f.close()
    # sets all buttons to on position
    Button2.config(highlightbackground='green')
    Button1.config(highlightbackground='white')
    Button4.config(highlightbackground='green')
    Button3.config(highlightbackground='white')
    Button6.config(highlightbackground='green')
    Button5.config(highlightbackground='white')
    Button8.config(highlightbackground='green')
    Button7.config(highlightbackground='white')
    showinfo('Settings Loaded!', 'Default settings loaded')


# finds out if the preloaded settings are active
# sets the account data
def accountData(e2, accountName):
    with open("config.txt", "r") as f:
        for i in range(0, 6):
            s = f.readline()

        if s == "Blank":

            account = e2.get()
            account = str(account) + " account password"
            accountName.destroy()
        elif s == "Gmail":
            account = "Gmail account password"
        elif s == "Facebook":
            account = "Facebook account password"
        elif s == "Apple":
            account = "Apple ID password"

    return account


# shuts the program down
def shutdown(win):
    win.destroy()


# loads Gmail passowrd requirements
def gmail():
    with open("config.txt", "r") as f:
        oglength = f.readline().strip()
        f.close()
    s = open("config.txt").read()
    s = s.replace(str(oglength), "14")
    # sets buttons to correct colour
    Button2.config(highlightbackground='green')
    Button1.config(highlightbackground='white')
    s = s.replace("FalseA", "TrueA")
    # sets buttons to correct colour
    Button4.config(highlightbackground='green')
    Button3.config(highlightbackground='white')
    s = s.replace("FalseB", "TrueB")
    # sets buttons to correct colour
    Button6.config(highlightbackground='green')
    Button5.config(highlightbackground='white')
    s = s.replace("FalseC", "TrueC")
    # sets buttons to correct colour
    Button8.config(highlightbackground='green')
    Button7.config(highlightbackground='white')
    s = s.replace("FalseD", "TrueD")
    s = s.replace("Facebook", "Gmail")
    s = s.replace("Apple", "Gmail")
    s = s.replace("Blank", "Gmail")
    f = open("config.txt", "w")
    f.write(s)
    f.close()
    showinfo("Settings loaded!", "Gmail password settings loaded")


# loads facebook passowrd requirements
def facebook():
    with open("config.txt", "r") as f:
        oglength = f.readline().strip()
        f.close()
    s = open("config.txt").read()
    s = s.replace(str(oglength), "12")
    # sets buttons to correct colour
    Button2.config(highlightbackground='green')
    Button1.config(highlightbackground='white')
    s = s.replace("FalseA", "TrueA")
    # sets buttons to correct colour
    Button4.config(highlightbackground='green')
    Button3.config(highlightbackground='white')
    s = s.replace("FalseB", "TrueB")
    # sets buttons to correct colour
    Button6.config(highlightbackground='green')
    Button5.config(highlightbackground='white')
    s = s.replace("FalseC", "TrueC")
    # sets buttons to correct colour
    Button8.config(highlightbackground='green')
    Button7.config(highlightbackground='white')
    s = s.replace("FalseD", "TrueD")
    s = s.replace("Gmail", "Facebook")
    s = s.replace("Apple", "Facebook")
    s = s.replace("Blank", "Facebook")
    f = open("config.txt", "w")
    f.write(s)
    f.close()
    showinfo("Settings loaded!", "Facebook password settings loaded")


# loads apple passowrd requirements
def apple():
    with open("config.txt", "r") as f:
        oglength = f.readline().strip()
        f.close()
    s = open("config.txt").read()
    s = s.replace(str(oglength), "14")
    # sets buttons to correct colour
    Button2.config(highlightbackground='green')
    Button1.config(highlightbackground='white')
    s = s.replace("FalseA", "TrueA")
    # sets buttons to correct colour
    Button4.config(highlightbackground='green')
    Button3.config(highlightbackground='white')
    s = s.replace("FalseB", "TrueB")
    # sets buttons to correct colour
    Button6.config(highlightbackground='green')
    Button5.config(highlightbackground='white')
    s = s.replace("FalseC", "TrueC")
    # sets buttons to correct colour
    Button8.config(highlightbackground='green')
    Button7.config(highlightbackground='white')
    s = s.replace("FalseD", "TrueD")
    s = s.replace("Gmail", "Apple")
    s = s.replace("Facebook", "Apple")
    s = s.replace("Blank", "Apple")
    f = open("config.txt", "w")
    f.write(s)
    f.close()
    showinfo("Settings loaded!", "Apple password settings loaded")


# Mail input if account type is already known
def mailinpt(window):
    window.destroy()
    addresss = Toplevel(win)
    addresss.geometry("400x200")
    l = Label(addresss, text="Please enter your email")
    e = Entry(addresss)
    b = Button(addresss, text="Submit", command=lambda: accountinpt(addresss, e))
    l.pack()
    e.pack()
    b.pack()


# Mail input for when account type is unknown
def mailinpt2(window):
    window.destroy()
    e2 = ""
    accountName = Toplevel(win)
    addresss = Toplevel(win)
    addresss.geometry("400x200")
    l = Label(addresss, text="Please enter your email")
    e = Entry(addresss)
    b = Button(addresss, text="Submit", command=lambda: mail(addresss, e, e2, accountName))
    l.pack()
    e.pack()
    b.pack()
    accountName.withdraw()


# Gets account type from user
def accountinpt(addresss, e):
    accountName = Toplevel(win)
    accountName.geometry("400x200")
    l2 = Label(accountName, text="Please enter type of account E.G Gmail, Facebook...")
    e2 = Entry(accountName)
    b2 = Button(accountName, text="Submit", command=lambda: mail(addresss, e, e2, accountName))
    l2.pack()
    e2.pack()
    b2.pack()


# gets new length and saves to config file
def length(oglength):
    length = entry1.get()
    with open("config.txt", "r") as f:
        oglength = f.readline().strip()
        f.close()
    if int(length) < 8:
        showinfo("Length Error", "Password length is too short")
    elif int(length) > 15:
        showinfo("Length Error", "Password length is too long")
    else:
        s = open("config.txt").read()
        s = s.replace(str(oglength), str(length))
        f = open("config.txt", "w")
        f.write(s)
        f.close()


# Turns lowercase letters OFF
def lowerCaseF():
    Button1.config(highlightbackground='green')
    Button2.config(highlightbackground='white')
    let = False
    s = open("config.txt").read()
    s = s.replace('TrueA', 'FalseA')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns lowercase letters ON
def lowerCaseT():
    Button2.config(highlightbackground='green')
    Button1.config(highlightbackground='white')
    let = True
    s = open("config.txt").read()
    s = s.replace('FalseA', 'TrueA')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns uppercase letters OFF
def UpperCaseF():
    Button3.config(highlightbackground='green')
    Button4.config(highlightbackground='white')
    cap = False
    s = open("config.txt").read()
    s = s.replace('TrueB', 'FalseB')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns uppercase letters ON
def UpperCaseT():
    Button4.config(highlightbackground='green')
    Button3.config(highlightbackground='white')
    cap = True
    s = open("config.txt").read()
    s = s.replace('FalseB', 'TrueB')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns numbers OFF
def NumbersF():
    Button5.config(highlightbackground='green')
    Button6.config(highlightbackground='white')
    num = False
    s = open("config.txt").read()
    s = s.replace('TrueC', 'FalseC')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns numbers ON
def NumbersT():
    Button6.config(highlightbackground='green')
    Button5.config(highlightbackground='white')
    num = True
    s = open("config.txt").read()
    s = s.replace('FalseC', 'TrueC')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns special characters OFF
def specialCharsF():
    Button7.config(highlightbackground='green')
    Button8.config(highlightbackground='white')
    spec = False
    s = open("config.txt").read()
    s = s.replace('TrueD', 'FalseD')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Turns special characters ON
def specialCharsT():
    Button8.config(highlightbackground='green')
    Button7.config(highlightbackground='white')
    spec = True
    s = open("config.txt").read()
    s = s.replace('FalseD', 'TrueD')
    f = open("config.txt", 'w')
    f.write(s)
    f.close()


# Gets type of account from User
def textAccount(window):
    window.destroy()
    accountName = Toplevel(win)
    accountName.geometry("400x200")
    l2 = Label(accountName, text="Please enter type of account E.G Gmail, Facebook...")
    e2 = Entry(accountName)
    b2 = Button(accountName, text="Submit", command=lambda: text(e2, accountName))
    l2.pack()
    e2.pack()
    b2.pack()
    return e2


# writes password to file
def text(e2, accountName):
    home = expanduser("~")
    pathh = str(home) + "/Passwords.txt"
    account = e2.get()
    accountName.destroy()
    with open('p891234.txt', 'r') as f:
        password = f.readline().strip()
        f.close()
    with open(str(pathh), 'a') as file1:
        file1.write("\n")
        file1.write(str(account))
        file1.write("\n")
        file1.write(": " + str(password))
        file1.write("\n")
        file1.close()
    os.remove("p891234.txt")
    showinfo('Password generated', 'Your new password is stored in ' + str(home) + '/Passwords.txt')


# writes password to file
def text2(window):
    window.destroy()
    with open('config.txt', 'r') as f:
        for i in range(0, 6):
            s = f.readline()
        account = str(s) + " account password"
        f.close()
    with open('p891234.txt', 'r') as f:
        password = f.readline().strip()
        f.close()
        home = expanduser("~")
        pathh = str(home) + "/Passwords.txt"
    with open(str(pathh), 'a') as file1:
        file1.write("\n")
        file1.write(str(account))
        file1.write("\n")
        file1.write(": " + str(password))
        file1.write("\n")
        file1.close()
    os.remove("p891234.txt")
    showinfo('Password generated', 'Your new password is stored in ' + str(home) + '/Passwords.txt')


# email module
def mail(addresss, e, e2, accountName):
    account = accountData(e2, accountName)
    accountName.destroy()
    with open('p891234.txt', 'r') as f:
        password = f.readline().strip()
        f.close()
    emailaddr = e.get()
    addresss.destroy()
    receivers = [str(emailaddr)]
    body = "Thank you for using password generator" + "\n" + "Here is your brand new password:    " + password + "\n"

    yag = yagmail.SMTP(user="noreply2390@gmail.com", password="qtyyhuoirzikwdhd")
    yag.send(
        to=receivers,
        subject=account,
        contents=body,
    )
    os.remove("p891234.txt")
    showinfo("Email sent", "Your new password is on its way to your inbox")


# menu for after generation
def Menu2(password):
    with open('p891234.txt', 'w') as f:
        f.write(password)
        f.close()
    window = Toplevel(win)
    window.geometry("400x200")
    button9 = Button(window, text="Email", command=lambda: mailinpt(window))
    button10 = Button(window, text="text file", command=lambda: textAccount(window))
    button11 = Button(window, text="Email", command=lambda: mailinpt2(window))
    button12 = Button(window, text="text file", command=lambda: text2(window))
    button9.pack()
    button11.pack()
    button10.pack()
    button12.pack()
    f = open("config.txt", "r")
    for i in range(0, 6):
        s = f.readline()
    if str(s) == "Blank":
        button11.pack_forget()
        button12.pack_forget()
    else:
        button9.pack_forget()
        button10.pack_forget()


# generator module
def generatee(length, let, spec, num, cap):
    valid = False
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    nf = False
    pswd = []
    password = ""
    # checks if values are all set to OFF
    if num == False and let == False and cap == False and spec == False:
        showinfo("unable to create password", "this is because all values are set to OFF")
        nf = True
    # Loop for generation of correct password
    while nf == False:
        while valid == False:
            pswd = []
            # generates the value of what character shall be generated
            for i in range(0, int(length)):
                correct = False
                # initialise random generator
                random.seed()

                # Checks values from file to generate correct characters
                if num == True and let == True and cap == True and spec == True:
                    choice = random.randrange(1, 5)

                elif num == False and let == True and cap == True and spec == True:
                    choice = random.randrange(2, 5)

                elif num == True and let == False and cap == True and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == True and spec == True:
                    choice = random.randrange(3, 5)

                elif num == True and let == True and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == True and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3 or int(choice) == 1:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == True and let == False and cap == False and spec == True:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2 or int(choice) == 3:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == False and spec == True:
                    choice = random.randrange(4, 5)

                elif num == True and let == True and cap == True and spec == False:
                    choice = random.randrange(1, 4)

                elif num == False and let == True and cap == True and spec == False:
                    choice = random.randrange(2, 4)

                elif num == True and let == False and cap == True and spec == False:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 2 or int(choice) == 4:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == False and cap == True and spec == False:
                    choice = 3

                elif num == True and let == True and cap == False and spec == False:
                    choice = random.randrange(1, 5)

                    while correct == False:

                        if int(choice) == 3 or int(choice) == 4:
                            choice = random.randrange(1, 5)
                        else:
                            correct = True

                elif num == False and let == True and cap == False and spec == False:
                    choice = 2

                elif num == True and let == False and cap == False and spec == False:
                    choice = 1

                pswd.append(int(choice))

                # checks if all requirements are met

            for i in range(0, len(pswd)):
                if pswd[i] == 1:
                    check1 = True
                elif pswd[i] == 2:
                    check2 = True
                elif pswd[i] == 3:
                    check3 = True
                elif pswd[i] == 4:
                    check4 = True

            if check1 == num and check2 == let and check3 == cap and check4 == spec:
                valid = True

            # Generates the password from the choices made in the previous section
            for i in range(0, len(pswd)):
                if pswd[i] == 1:
                    random.seed()
                    value = random.randrange(48, 58)
                    password = password + str(chr(value))
                elif pswd[i] == 2:
                    random.seed()
                    value = random.randrange(97, 123)
                    password = password + str(chr(value))
                elif pswd[i] == 3:
                    random.seed()
                    value = random.randrange(65, 91)
                    password = password + str(chr(value))
                elif pswd[i] == 4:
                    choice2 = random.randrange(1, 5)
                    if choice2 == 1:
                        value = random.randrange(33, 48)
                        password = password + str(chr(value))
                    elif choice2 == 2:
                        value = random.randrange(58, 64)
                        password = password + str(chr(value))
                    elif choice2 == 3:
                        value = random.randrange(94, 97)
                        password = password + str(chr(value))
                    elif choice2 == 4:
                        value = random.randrange(123, 127)
                        password = password + str(chr(value))
                nf = True
        Menu2(password)


# Gets Data from the config file and sets the variable values that are passed into the generator
def run():
    let = False
    num = False
    cap = False
    spec = False
    f = open("config.txt", "r")
    length = f.readline().strip()
    f.close()

    with open("config.txt", "r") as f:
        for i in range(0, 6):
            x = f.readline().strip()
            if x.strip() == "TrueA":
                let = True
            elif x.strip() == "FalseA":
                let = False
            elif x.strip() == "TrueB":
                cap = True
            elif x.strip() == "FalseB":
                cap = False
            elif x.strip() == "TrueC":
                num = True
            elif x.strip() == "FalseC":
                num = False
            elif x == "TrueD":
                spec = True
            elif x == "FalseD":
                spec = False

    f.close()
    generatee(length, let, spec, num, cap)


running = True
num = True
cap = True
let = True
spec = True
with open("config.txt", "r") as f:
    oglength = f.readline().strip()
    f.close
# Main

# Loads default values on start
s = open("config.txt").read()
s = s.replace("GmailGmail", "Blank")
s = s.replace("BlankBlank", "Blank")
s = s.replace("FacebookFacebook", "Blank")
s = s.replace("AppleApple", "Blank")
s = s.replace("Gmail", "Blank")
s = s.replace("Facebook", "Blank")
s = s.replace("Apple", "Blank")
s = s.replace("Blank", "Blank")
f = open("config.txt", "w")
f.write(s)
f.close()

# creates Menu GUI
win = Tk()
win.geometry("500x200")
button1Frame = Frame(win)
button2Frame = Frame(win)
button3Frame = Frame(win)
button4Frame = Frame(win)
button5Frame = Frame(win)
button6Frame = Frame(win)
button7Frame = Frame(win)

button1Frame.pack()
button2Frame.pack()
button3Frame.pack()
button4Frame.pack()
button5Frame.pack()
button6Frame.pack()
button7Frame.pack()

bottomFrame = Frame(win)
bottomFrame.pack(side=BOTTOM)

win.title("Password Genrator V2.0")

# Creates the buttons in the GUI
Button1 = Button(button1Frame, text="Lower Case OFF", command=lowerCaseF, highlightbackground='white')
Button2 = Button(button1Frame, text="Lower Case ON", command=lowerCaseT, highlightbackground='green')
Button3 = Button(button2Frame, text="Upper Case OFF", command=UpperCaseF, highlightbackground='white')
Button4 = Button(button2Frame, text="Upper Case ON", command=UpperCaseT, highlightbackground='green')
Button5 = Button(button3Frame, text="Numbers OFF", command=NumbersF, highlightbackground='white')
Button6 = Button(button3Frame, text="Numbers ON", command=NumbersT, highlightbackground='green')
Button7 = Button(button4Frame, text="Special Characters OFF", command=specialCharsF, highlightbackground='white')
Button8 = Button(button4Frame, text="Special Characters ON", command=specialCharsT, highlightbackground='green')
Button9 = Button(button5Frame, text="Submit Password length", command=lambda: length(oglength))
Button10 = Button(button6Frame, text="Gmail settings", command=gmail)
Button11 = Button(button6Frame, text="Facebook settings", command=facebook)
Button12 = Button(button6Frame, text="Apple settings", command=apple)
Button13 = Button(button7Frame, text="EXIT", command=lambda: shutdown(win))
Button14 = Button(button6Frame, text="Restore Defaults", command=restore)
entry1 = Entry(button5Frame)
generate = Button(bottomFrame, text='generate', command=run)

# Packs all the GUI elements into the correct place
Button1.pack(side=RIGHT)
Button2.pack(side=LEFT)
Button3.pack(side=RIGHT)
Button4.pack(side=LEFT)
Button5.pack(side=RIGHT)
Button6.pack(side=LEFT)
Button7.pack(side=RIGHT)
Button8.pack(side=LEFT)
entry1.pack(side=LEFT)
Button9.pack(side=RIGHT)
Button10.pack(side=LEFT)
Button11.pack(side=LEFT)
Button14.pack(side=RIGHT)
Button12.pack(side=RIGHT)
generate.pack()
Button13.pack()

# Displays main window
win.mainloop()
