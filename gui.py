import tkinter
window = tkinter.Tk()
# to rename the title
window.title("NBA guessing game")
window.geometry('1000x1000+10+10')
label = tkinter.Label(window, text = "Welcome to the NBA guessing game! A random NBA player will be selected from the 2022-2023 season and hints will be provided to guess the NBA player. Good luck!", font=('helvetica', '18', 'bold'),  
wraplength=800, justify="center").pack()

window.mainloop()
