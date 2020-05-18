from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import math

app = Tk()
app.title("GPA Calculator")

main = Frame(app, padx=10, pady=10)

######################## define global variables ###################################
global aString
global bString
global cString
global dString
global fString
global bplusString
global cplusString
global dplusString
global aminusString
global bminusString
global cminusString
global dminusString
global calculatedgpaLabel

######################## define calculate function #################################
def calculate():

#Get textbox values
    a=aString.get()
    b=bString.get()
    c=cString.get()
    d=dString.get()
    f=fString.get()
    bplus=bplusString.get()
    cplus=cplusString.get()
    dplus=dplusString.get()
    aminus=aminusString.get()
    bminus=bminusString.get()
    cminus=cminusString.get()
    dminus=dminusString.get()

#convert textbox value to integers
    atot=int(a)
    btot=int(b)
    ctot=int(c)
    dtot=int(d)
    ftot=int(f)
    bplustot=int(bplus)
    cplustot=int(cplus)
    dplustot=int(dplus)
    aminustot=int(aminus)
    bminustot=int(bminus)
    cminustot=int(cminus)
    dminustot=int(dminus)

#Summation of total credits
    gpaSum=sum([atot,aminustot,bplustot,btot,bminustot,cplustot,ctot,cminustot,dplustot,dtot,dminustot,ftot])

#Mulitply credits by associated GPA point value
    ax=(atot*4)
    bx=(btot*3)
    cx=(ctot*2)
    dx=(dtot*1)
    fx=(ftot*0)
    bplusx=(bplustot*3.3)
    cplusx=(cplustot*2.3)
    dplusx=(dplustot*1.3)
    aminusx=(aminustot*3.7)
    bminusx=(bminustot*2.7)
    cminusx=(cminustot*1.7)
    dminusx=(dminustot*0.7)
    
#Summation of total points
    totalPoints=sum([ax,bx,cx,dx,fx,bplusx,cplusx,dplusx,aminusx,bminusx,cminusx,dminusx])

#Calculating actual GPA/output to calculatedgpaLable "text" property
    calculatedgpaLabel['text'] = totalPoints/gpaSum


####################################################################################
######################## label and text entry box for A ############################

aLabel = Label(main, text="Enter total credits earned with an A:", width=30, anchor='w')
aLabel.grid(row=2, column=1)
aTextbox=IntVar(None)
aString=Entry(main,textvariable=aTextbox,width=10)
aString.grid(row=2,column=2)

####################################################################################
######################## label and text entry box for A- ###########################

aminusLabel = Label(main, text="Enter total credits earned with an A-:", width=30, anchor='w')
aminusLabel.grid(row=3, column=1)
aminusTextbox=IntVar(None)
aminusString=Entry(main,textvariable=aminusTextbox,width=10)
aminusString.grid(row=3,column=2)

####################################################################################
######################## label and text entry box for B+ ###########################

bplusLabel = Label(main, text="Enter total credits earned with an B+:", width=30, anchor='w')
bplusLabel.grid(row=4, column=1)
bplusTextbox=IntVar(None)
bplusString=Entry(main,textvariable=bplusTextbox,width=10)
bplusString.grid(row=4,column=2)

####################################################################################
######################## label and text entry box for B ########################

bLabel = Label(main, text="Enter total credits earned with an B:", width=30, anchor='w')
bLabel.grid(row=5, column=1)
bTextbox=IntVar(None)
bString=Entry(main,textvariable=bTextbox,width=10)
bString.grid(row=5,column=2)

####################################################################################
######################## label and text entry box for B- ###########################

bminusLabel = Label(main, text="Enter total credits earned with an B-:", width=30, anchor='w')
bminusLabel.grid(row=6, column=1)
bminusTextbox=IntVar(None)
bminusString=Entry(main,textvariable=bminusTextbox,width=10)
bminusString.grid(row=6,column=2)

####################################################################################
######################## label and text entry box for C+ ###########################

cplusLabel = Label(main, text="Enter total credits earned with an C+:", width=30, anchor='w')
cplusLabel.grid(row=7, column=1)
cplusTextbox=IntVar(None)
cplusString=Entry(main,textvariable=cplusTextbox,width=10)
cplusString.grid(row=7,column=2)

####################################################################################
######################## label and text entry box for C ############################

cLabel = Label(main, text="Enter total credits earned with an C:", width=30, anchor='w')
cLabel.grid(row=8, column=1)
cTextbox=IntVar(None)
cString=Entry(main,textvariable=cTextbox,width=10)
cString.grid(row=8,column=2)

####################################################################################
######################## label and text entry box for C- ###########################

cminusLabel = Label(main, text="Enter total credits earned with an C-:", width=30, anchor='w')
cminusLabel.grid(row=9, column=1)
cminusTextbox=IntVar(None)
cminusString=Entry(main,textvariable=cminusTextbox,width=10)
cminusString.grid(row=9,column=2)

####################################################################################
######################## label and text entry box for D+ ###########################

dplusLabel = Label(main, text="Enter total credits earned with an D+:", width=30, anchor='w')
dplusLabel.grid(row=10, column=1)
dplusTextbox=IntVar(None)
dplusString=Entry(main,textvariable=dplusTextbox,width=10)
dplusString.grid(row=10,column=2)

####################################################################################
######################## label and text entry box for D ############################

dLabel = Label(main, text="Enter total credits earned with an D:", width=30, anchor='w')
dLabel.grid(row=11, column=1)
dTextbox=IntVar(None)
dString=Entry(main,textvariable=dTextbox,width=10)
dString.grid(row=11,column=2)

####################################################################################
######################## label and text entry box for D- ###########################

dminusLabel = Label(main, text="Enter total credits earned with an D-:", width=30, anchor='w')
dminusLabel.grid(row=12, column=1)
dminusTextbox=IntVar(None)
dminusString=Entry(main,textvariable=dminusTextbox,width=10)
dminusString.grid(row=12,column=2)
######################## label and text entry box for F ############################

fLabel = Label(main, text="Enter total credits earned with an F:", width=30, anchor='w')
fLabel.grid(row=13, column=1)
fTextbox=IntVar(None)
fString=Entry(main,textvariable=fTextbox,width=10)
fString.grid(row=13,column=2)

####################################################################################
######################## Calculate button configuration ############################
    
gpaButton = Button(main, text="Calculate", width=20, anchor='n', bg='springgreen', command=calculate)
gpaButton.grid(row=14, column=1, columnspan=2)

####################################################################################
######################## label and label for calculated GPA ########################

gpaLabel = Label(main, text="GPA:", width=30, anchor='e')
gpaLabel.grid(row=15, column=1)
calculatedgpaLabel = Label(main, text="", width=10, anchor='w')
calculatedgpaLabel.grid(row=15, column=2)

####################################################################################

main.pack()

app.mainloop()
