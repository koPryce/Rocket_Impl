from tkinter import *
from tkinter import messagebox


# Function
def parseString():
    string = stringBox.get()
    if not string.isalpha():
        messagebox.showerror("Alphabet Error", "The string entered contains characters that are not a part of the alphabet.", parent=main_frame)
    elif not string.islower():
        messagebox.showerror("Case Error", "The string entered contains uppercase characters that are not a part of the alphabet.", parent=main_frame)
    else:
        success_window = Toplevel()
        success_window.title("Simulation Starting...")
        success_window.iconbitmap('favicon.ico')
        success_window.geometry("200x75+500+300")
        success_window.attributes('-toolwindow', True)

        Label(success_window, text="Simulation is about to begin!").pack()
        success_window.after(5000, lambda: success_window.destroy())
        main_window.wm_state('iconic')
        listString = []
        listString[:0] = string
        simulation('Launch Pad', listString)

def simulation(state, string):

    if state == "Launch Pad":
        pass
    elif state ==

# IF IT GOES TO THE DEAD STATE, END THE PROGRAM
# IF IT GOES TO THE ABORT STATE, TELL IT THAT IT STAYS THERE

# Main Window
main_window = Tk()
main_window.title("Rocket Simulation")
main_window.iconbitmap('favicon.ico')
main_window.configure(bg="#fff")
main_window.geometry("900x600")

# Main Frame
main_frame = LabelFrame(main_window, text="String Input", padx=40, pady=40, borderwidth=5)
main_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

# Label
Label(main_frame, text="Enter a valid input string").grid(row=0, column=0)

# Textbox
stringBox = Entry(main_frame, width=50, borderwidth=5)
stringBox.grid(row=0, column=1)

# Button
Button(main_frame, text="Submit", command=parseString).grid(row=1, column=1, columnspan=2)

mainloop()
