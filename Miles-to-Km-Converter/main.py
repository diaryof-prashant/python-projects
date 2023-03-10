from tkinter import *

window=Tk()
window.title("Miles to Km")
window.minsize(width=200,height=50)
window.config(padx=20,pady=20)

def btn_clicked():
    mile=mile_input.get()
    km=1.6*int(mile)
    km_output.config(text=km)


mile_input=Entry(text="Enter something")
mile_input.grid(column=1,row=0)

mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)

equal_label=Label(text="is equal to ")
equal_label.grid(column=0,row=1)

km_output=Label(text="0")
km_output.grid(column=1,row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

conv_btn=Button(text="Calculate",command=btn_clicked)
conv_btn.grid(column=1,row=2)
















window.mainloop()
