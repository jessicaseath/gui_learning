import tkinter
root = tkinter.Tk()

root.title("Hello World!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="pink", bg="pink", font=("Wide latin", "50", "italic"))
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hello there!", fg="green", bg="pink", font=("Wide latin", "50", "italic"))
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hey you!", fg="orange", bg="yellow", font=("Wide latin", "50", "italic"))
my_label.grid()

root.mainloop()
