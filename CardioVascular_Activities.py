from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("Heart_Diagnose_Report")
root.geometry("600x600")
root.configure(background="Yellow")

question1_radionButton=StringVar(value="0")
question1=Label(root,text="Do you experience shortness of breath during routine activities")
question1.pack()
question1_r1=Radiobutton(root,text="yes",variable=question1_radionButton,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="no",variable=question1_radionButton,value="no")
question1_r2.pack()

question2_radionButton=StringVar(value="0")
question2=Label(root,text="Do you have swelling in the feet/ankles/legs(shoes feel tighter) or abdomen")
question2.pack()
question2_r1=Radiobutton(root,text="yes",variable=question2_radionButton,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="no",variable=question2_radionButton,value="no")
question2_r2.pack()

question3_radionButton=StringVar(value="0")
question3=Label(root,text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
question3.pack()
question3_r1=Radiobutton(root,text="yes",variable=question3_radionButton,value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="no",variable=question3_radionButton,value="no")
question3_r2.pack()

question4_radionButton=StringVar(value="0")
question4=Label(root,text="Do you experience shortness of breath while at rest/lying down?")
question4.pack()
question4_r1=Radiobutton(root,text="yes",variable=question4_radionButton,value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root,text="no",variable=question4_radionButton,value="no")
question4_r2.pack()

question5_radionButton=StringVar(value="0")
question5=Label(root,text="Do you experience persistent wheezing/coughing that produce white or pink blood tinged muscle")
question5.pack()
question5_r1=Radiobutton(root,text="yes",variable=question5_radionButton,value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root,text="no",variable=question5_radionButton,value="no")
question5_r2.pack()

def cardioVascular_activities():
    score=0
    if question1_radionButton.get()=="yes":
        score=score+10
        print(score)
    if question2_radionButton.get()=="yes":
        score=score+10
        print(score)
    if question3_radionButton.get()=="yes":
        score=score+10
        print(score)
    if question4_radionButton.get()=="yes":
        score=score+10
        print(score)
    if question5_radionButton.get()=="yes":
        score=score+10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to vist a Doctor")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report","You might perhaps need to visit a Doctor")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a Doctor")

btn=Button(root,text="Check",command=cardioVascular_activities)
btn.pack()

root.mainloop()