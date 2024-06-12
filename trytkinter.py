import tkinter as tk

def submit():
    print("Submitted: " + entry.get())

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
