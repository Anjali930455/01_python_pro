import tkinter as tk


def convert():
    c=int(e1.get())
    f =(82.71) * (float(c))




    t1.config(state="normal")
    t1.delete('1.0' ,tk.END)
    t1.insert(tk.END,f)
    t1.congif(state="disabled")




window =tk.Tk()
window.geometry("300x250")
window.config(bg ="#c0c0c0")
window.resizable(width=False,height=False)
window.title("Dollar to Rupee Converter")


l1 = tk.Label(window,text="Dollar to Rupee Converter", font=("Arial",15),fg = "White",bg="black")
l2 = tk.Label(window,text="Enter Dollar Amount:", font=("Arial",10,"bold"),fg = "White",bg="#4B1147")
l3=tk.Label(window,text="Amount in Rupee:",font =("Arial",10,"bold"),fg="white",bg="sky blue")

empty_l1 = tk.Label(window,bg="#E9967A")
empty_l2 = tk.Label(window,bg="#E9967A")
# empty_l3=tk.Label(window,bg="#E9967A")
e1 = tk.Entry(window,font=("Arial",10))

btn =tk.Button(window,text="Convert the Dollor",font=("Arial",10),command=convert)

t1 = tk.Text(window,state="disabled",width=15,height=0)

l1.pack()
l2.pack()
e1.pack()
btn.pack()
l3.pack()
t1.pack()

window.mainloop()

