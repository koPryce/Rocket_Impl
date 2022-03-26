from tkinter import *
from tkinter import messagebox


# Function
def parseString():
    string = stringBox.get()
    if not string.isalpha():
        messagebox.showerror("Alphabet Error",
                             "The string entered contains characters that are not a part of the alphabet.",
                             parent=main_frame)
    elif not string.islower():
        messagebox.showerror("Case Error",
                             "The string entered contains uppercase characters that are not a part of the alphabet.",
                             parent=main_frame)
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
        main_window.after(5500, lambda: simulation('Launch Pad', listString))


def simulation(state, string):
    val = string.pop(0)
    if state.title() == "Launch Pad":
        if val == 'a':
            print("At the", state,
                  "the rocket received the Launch Signal at T minus 0 and proceeded to the Lift Off Condition.")
            simulation('Lift Off', string)
        elif val == 'b':
            print("At the", state,
                  "the rocket received the lightening observed with 10 nautical miles signal and proceeded to the Delay Launch Condition.")
            simulation('Delay Launch', string)
        elif val == 'd':
            print("At the", state,
                  "the rocket received the field mill instrument readings within 5 nautical miles exceed ±1,500 volts signal and proceeded to the Delay Launch Condition.")
            simulation('Delay Launch', string)
        elif val == 'f':
            simulation('Abort', string)
        elif val == 'g':
            simulation('Abort', string)
        elif val == 'h':
            simulation('Abort', string)
        elif val == 'i':
            simulation('Abort', string)
        elif val == 'j':
            simulation('Abort', string)
        elif val == 'k':
            simulation('Abort', string)
        elif val == 'l':
            simulation('Abort', string)
        elif val == 'm':
            simulation('Abort', string)
        elif val == 'n':
            simulation('Abort', string)
        else:
            simulation('Dead', string)

    elif state.title() == "Delay Launch":
        pass
    elif state.title() == "Lift Off":
        pass
    elif state.title() == "Powered Ascent":
        pass
    elif state.title() == "Ignition":
        pass
    elif state.title() == "Stage Separation":
        pass
    elif state.title() == "On Orbit Operations":
        pass
    elif state.title() == "Entry Burn":
        pass
    elif state.title() == "Splashdown":
        pass
    elif state.title() == "Abort":  # IF IT GOES TO THE ABORT STATE, TELL IT THAT IT STAYS THERE
        pass
    elif state.title() == "Dead":  # IF IT GOES TO THE DEAD STATE, END THE PROGRAM
        pass


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
