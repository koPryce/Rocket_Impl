from tkinter import *
from tkinter import messagebox
import cv2
from ffpyplayer import writer
from ffpyplayer.player import MediaPlayer


# Functions
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
        listString.append('EOS')
        main_window.after(5500, lambda: simulation('Launch Pad', listString))


def rescaleframe(name):
    return cv2.resize(name, (500, 400), interpolation=cv2.INTER_AREA)


def playVideo(video_path):
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        rescaledframe = rescaleframe(frame)

        cv2.imshow("Video", rescaledframe)
        #cv2.resize(frame, (500, 400), interpolation=cv2.INTER_AREA)

        if val != 'eof' and audio_frame is not None:
            # audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


def simulation(state, string):
    val = string.pop(0)
    if state.title() == "Launch Pad":
        if val == 'a':
            playVideo('Videos/Rocket Liftoff.mp4')
            print("At the", state,
                  "the rocket received the Launch Signal at T minus 0 and proceeded to the Lift Off Condition.")
            simulation('Lift Off', string)
        elif val == 'b':
            playVideo('Videos/Rocket and Lightning.mp4')
            print("At the", state,
                  "the rocket received the lightening observed with 10 nautical miles signal and proceeded to the Delay Launch Condition.")
            simulation('Delay Launch', string)
        elif val == 'd':
            print("At the", state,
                  "the rocket received the field mill instrument readings within 5 nautical miles exceed ±1,500 volts signal and proceeded to the Delay Launch Condition.")
            simulation('Delay Launch', string)
        elif val == 'f':
            print("At the", state,
                  "the rocket received the 162-foot level exceeds 30 mph signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'g':
            print("At the", state,
                  "the rocket received the upper-level conditions are detected containing wind sheer signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'h':
            print("At the", state,
                  "the rocket received the attached thunderstorm anvil cloud is detected within 10 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'i':
            print("At the", state,
                  "the rocket received the detached thunderstorm anvil cloud is detected within 10 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'j':
            print("At the", state,
                  "the rocket received the thunderstorm debris cloud is detected within 3 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'k':
            print("At the", state,
                  "the rocket received the disturbed cloud extending into freezing temperatures is detected within 5 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'l':
            print("At the", state,
                  "the rocket received the cloud layer greater than 4,500 feet thick extending into freezing temperatures is detected signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'm':
            print("At the", state,
                  "the rocket received the cumulus clouds extending into freezing temperatures are detected within 10 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        elif val == 'n':
            print("At the", state,
                  "the rocket received the cumulus cloud is detected which formed because of or is directly attached to smoke plume signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Delay Launch":
        if val == 'c':
            print("At the", state,
                  "the rocket received the 30 minutes has passed signal and proceeded to the Launch Pad Condition.")
            simulation('Launch Pad', string)
        elif val == 'e':
            print("At the", state,
                  "the rocket received the thunderstorm producing lightening is detected within 10 nautical miles signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Lift Off":
        if val == 'o':
            playVideo('Videos/SRB Separation.mp4')
            print("At the", state,
                  "the rocket received the SRB Separation signal and proceeded to the Powered Ascent Condition.")
            simulation('Powered Ascent', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Powered Ascent":
        if val == 'p':
            playVideo('Videos/MECO.mp4')
            print("At the", state,
                  "the rocket received the Main Engine Cut Off (MECO) signal and proceeded to the Ignition Condition.")
            simulation('Ignition', string)
        elif val == 'q':
            print("At the", state,
                  "the rocket received the Return to Launch Site (RTLS) signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Ignition":
        if val == 'r':
            playVideo('Videos/ET Separation.mp4')
            print("At the", state,
                  "the rocket received the ET Separation signal and proceeded to the Stage Separation Condition.")
            simulation('Stage Separation', string)
        elif val == 's':
            print("At the", state,
                  "the rocket received the Transoceanic Abort Landing (TAL) signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Stage Separation":
        if val == 't':
            print("At the", state,
                  "the rocket received the Orbit Insertion signal and proceeded to the On Orbit Operations Condition.")
            simulation('On Orbit Operations', string)
        elif val == 'u':
            print("At the", state,
                  "the rocket received the Abort Once Around (AOA) signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "On Orbit Operations":
        if val == 'v':
            print("At the", state,
                  "the rocket received the Deorbit signal and proceeded to the Boostback Burn Condition.")
            simulation('Boostback Burn', string)
        elif val == 'w':
            playVideo('Videos/Abort to Orbit.mp4')
            print("At the", state,
                  "the rocket received the Abort to Orbit (ATO) signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == 'Boostback Burn':
        if val == 'x':
            playVideo('Videos/Reentry to Earth.mp4')
            print("At the", state,
                  "the rocket received the Reentry signal and proceeded to the Entry Burn Condition.")
            simulation('Entry Burn', string)
        elif val == 'y':
            print("At the", state,
                  "the rocket received the Contingency Abort signal and proceeded to the Abort Condition.")
            simulation('Abort', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Entry Burn":
        if val == 'z':
            playVideo('Videos/Landing.mp4')
            print("At the", state,
                  "the rocket received the Landing signal and proceeded to the Splashdown Condition.")
            simulation('Splashdown', string)
        else:
            print("At the", state,
                  "the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.")
            simulation('Stall', string)
    elif state.title() == "Splashdown":
        print("At the", state, "the rocket has safety landed.")
    elif state.title() == "Abort":
        print("Welcome to the Abort Condition, where no matter the input, you're stuck here.")
        # simulation('Abort', string)
    elif state.title() == "Stall":
        print("Welcome to the Stall Condition, rocket won't move.")
        # main_window.destroy()


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
