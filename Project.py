# Names: Shanae Heslop, Kevaughn Pryce, Torrike Whittaker
# ID Numbers: 1905461, 1901891, 1801536
# Date of Submission: March 31, 2022
# Lecturer: Mr. David White
# Title: Implementation of DFA for Space Flight Vehicle Mission

# Imports
import time
import tkinter
from tkinter import *
from tkinter import messagebox
import cv2
from ffpyplayer.player import MediaPlayer
import pygame


# Functions
def parseString():
    string = stringBox.get()  # Retrieves the string entered by the user.
    # Error handling is performed for the string and if everything is alright, them the implementation begins.
    if len(string) == 0:
        messagebox.showerror("No String",
                             "The string entered is empty.",
                             parent=main_frame)
    elif not string.isalpha():
        messagebox.showerror("Alphabet Error",
                             "The string entered contains character(s) that are not a part of the alphabet.",
                             parent=main_frame)
    elif not string.islower():
        messagebox.showerror("Case Error",
                             "The string entered contains uppercase character(s) that are not a part of the alphabet.",
                             parent=main_frame)
    else:
        success_window = Toplevel()
        success_window.title("Simulation Starting...")
        success_window.iconbitmap('favicon.ico')
        success_window.geometry("200x75+500+300")
        success_window.attributes('-toolwindow', True)

        Label(success_window, text="Simulation is about to begin!").pack()
        success_window.after(3000, lambda: success_window.destroy())
        main_window.wm_state('iconic')
        listString = []
        listString[:0] = string
        listString.append('EOS')
        main_window.after(3500, lambda: simulation('Launch Pad', listString))


# This function is used to resize the frame that shows the videos
def rescaleFrame(name):
    return cv2.resize(name, (500, 400), interpolation=cv2.INTER_AREA)


# This function plays the video files
def playVideo(video_path, frame_name, wait_key):
    video = cv2.VideoCapture(video_path)
    audio = MediaPlayer(video_path)

    while True:
        grabbed, frame = video.read()
        audio_frame, val = audio.get_frame()

        if not grabbed:
            break

        rescaled_frame = rescaleFrame(frame)
        cv2.imshow(frame_name, rescaled_frame)

        if cv2.waitKey(wait_key) & 0xFF == ord("q"):
            break

        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame

    video.release()
    cv2.destroyAllWindows()


# This function plays the audio
def playAudio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(open(audio_path, "rb"))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


# This function is the core of the implementation as it is the representation of the DFA constructed.
def simulation(state, string):
    val = string.pop(0)
    if state.title() == "Launch Pad":
        if val == 'a':
            state_window = Toplevel()
            state_window.title("Lift Off")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Launch Signal at T minus 0 and proceeded to the Lift Off Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            main_window.after(3000, lambda: playAudio("Audios/Launch_Pad.wav"))
            state_window.after(8000, lambda: state_window.destroy())
            main_window.after(9000, lambda: playVideo('Videos/Rocket Liftoff.mp4', 'Lift Off', 12))
            main_window.after(52500, lambda: simulation('Lift Off', string))
        elif val == 'b':
            state_window = Toplevel()
            state_window.title("Delay Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the lightning observed with 10 nautical miles signal and proceeded to the Delay Launch Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/Rocket and Lightning.mp4', 'Lightning', 9))
            main_window.after(34500, lambda: simulation('Delay Launch', string))
        elif val == 'd':
            state_window = Toplevel()
            state_window.title("Delay Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the field mill instrument readings within 5 nautical miles exceed ±1,500 volts signal and proceeded to the Delay Launch Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Delay Launch', string))
        elif val == 'f':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the 162-foot level exceeds 30 mph signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'g':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the upper-level conditions are detected containing wind sheer signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'h':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the attached thunderstorm anvil cloud is detected within 10 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'i':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the detached thunderstorm anvil cloud is detected within 10 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'j':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the thunderstorm debris cloud is detected within 3 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'k':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the disturbed cloud extending into freezing temperatures is detected within 5 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'l':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the cloud layer greater than 4,500 feet thick extending into freezing temperatures is detected signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'm':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the cumulus clouds extending into freezing temperatures are detected within 10 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'n':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the cumulus cloud is detected which formed because of or is directly attached to smoke plume signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Delay Launch":
        if val == 'c':
            state_window = Toplevel()
            state_window.title("Launch Pad")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="At the " + state +
                  " the rocket received the 30 minutes has passed signal and proceeded to the Launch Pad Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Launch Pad', string))
        elif val == 'e':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the thunderstorm producing lightning is detected within 10 nautical miles signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Lift Off":
        if val == 'o':
            state_window = Toplevel()
            state_window.title("Powered Ascent")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the SRB Separation signal and proceeded to the Powered Ascent Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/SRB Separation.mp4', 'SRB Separation', 9))
            main_window.after(28500, lambda: simulation('Powered Ascent', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Powered Ascent":
        if val == 'p':
            state_window = Toplevel()
            state_window.title("Ignition")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Main Engine Cut Off (MECO) signal and proceeded to the Ignition Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/MECO.mp4', 'MECO', 20))
            main_window.after(36500, lambda: simulation('Ignition', string))
        elif val == 'q':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Return to Launch Site (RTLS) signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Ignition":
        if val == 'r':
            state_window = Toplevel()
            state_window.title("Stage Separation")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the ET Separation signal and proceeded to the Stage Separation Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/ET Separation.mp4', 'ET Separation', 9))
            main_window.after(19500, lambda: simulation('Stage Separation', string))
        elif val == 's':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Transoceanic Abort Landing (TAL) signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Stage Separation":
        if val == 't':
            state_window = Toplevel()
            state_window.title("On Orbit Operations")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="At the " + state +
                  " the rocket received the Orbit Insertion signal and proceeded to the On Orbit Operations Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('On Orbit Operations', string))
        elif val == 'u':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Abort Once Around (AOA) signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "On Orbit Operations":
        if val == 'v':
            state_window = Toplevel()
            state_window.title("Boostback Burn")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="At the " + state +
                       " the rocket received the Deorbit signal and proceeded to the Boostback Burn Condition..").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Boostback Burn', string))
        elif val == 'w':
            state_window = Toplevel()
            state_window.title("Abort to Orbit --> Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Abort to Orbit (ATO) signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/Abort to Orbit.mp4', 'Abort to Orbit', 9))
            main_window.after(34500, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == 'Boostback Burn':
        if val == 'x':
            state_window = Toplevel()
            state_window.title("Entry Burn")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Reentry signal and proceeded to the Entry Burn Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/Reentry to Earth.mp4', 'Reentry to Earth', 16))
            main_window.after(19500, lambda: simulation('Entry Burn', string))
        elif val == 'y':
            state_window = Toplevel()
            state_window.title("Abort Launch")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Contingency Abort signal and proceeded to the Abort Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: simulation('Abort', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Entry Burn":
        if val == 'z':
            state_window = Toplevel()
            state_window.title("Splashdown")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received the Landing signal and proceeded to the Splashdown Condition.").pack()
            playAudio("Audios/Right_Path.wav")
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: playVideo('Videos/Landing.mp4', 'Landing', 9))
            main_window.after(19500, lambda: simulation('Splashdown', string))
        elif val == 'EOS':
            state_window = Toplevel()
            state_window.title("Premature Abort")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window,
                  text="Due to the length of the string entered, the launch will be prematurely aborted in the " + state + " condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(4000, lambda: main_window.destroy())
        else:
            state_window = Toplevel()
            state_window.title("Stall State")
            state_window.iconbitmap('favicon.ico')
            state_window.geometry("600x75+500+300")
            state_window.attributes('-toolwindow', True)
            Label(state_window, text="At the " + state +
                                     " the rocket received a signal that it couldn't accept and proceeded to the Stall State Condition.").pack()
            state_window.after(3000, lambda: state_window.destroy())
            main_window.after(3500, lambda: playAudio("Audios/Error_Alert.wav"))
            main_window.after(9000, lambda: simulation('Stall', string))
    elif state.title() == "Splashdown":
        state_window = Toplevel()
        state_window.title("Splashdown")
        state_window.iconbitmap('favicon.ico')
        state_window.geometry("600x75+500+300")
        state_window.attributes('-toolwindow', True)
        Label(state_window, text="At the " + state + " the rocket has safety landed.").pack()
        playAudio("Audios/Right_Path.wav")
        state_window.after(3000, lambda: state_window.destroy())
        main_window.after(4000, lambda: main_window.destroy())
    elif state.title() == "Abort":
        state_window = Toplevel()
        state_window.title("In Abort Launch")
        state_window.iconbitmap('favicon.ico')
        state_window.geometry("600x75+500+300")
        state_window.attributes('-toolwindow', True)
        Label(state_window, text="Welcome to the Abort Condition, where no matter the input, you're stuck here.").pack()
        state_window.after(3000, lambda: state_window.destroy())
        main_window.after(4000, lambda: main_window.destroy())
    elif state.title() == "Stall":
        state_window = Toplevel()
        state_window.title("Stall State")
        state_window.iconbitmap('favicon.ico')
        state_window.geometry("600x75+500+300")
        state_window.attributes('-toolwindow', True)
        Label(state_window, text="Welcome to the Stall Condition, the rocket won't move.").pack()
        state_window.after(3000, lambda: state_window.destroy())
        main_window.after(4000, lambda: main_window.destroy())


# Main Window
main_window = Tk()
main_window.title("Rocket Simulation")
main_window.iconbitmap('favicon.ico')
main_window.configure(bg="#fff")
main_window.geometry("700x400")

# Greeting
label = tkinter.Label(main_window, text="Welcome, please enter a string to begin simulation")
label.config(font=('arial bold', 18), bg='white')
label.grid(column=0, row=0)

# Main Frame
main_frame = LabelFrame(main_window, text="String Input", padx=40, pady=40, borderwidth=5)
main_frame.grid(row=1, column=0, padx=(80, 20), pady=100)

# Label
Label(main_frame, text="Enter a valid input string").grid(row=0, column=0)

# Textbox
stringBox = Entry(main_frame, width=50, borderwidth=5)
stringBox.grid(row=0, column=1)

# Button
Button(main_frame, text="Submit", command=parseString).grid(row=1, column=1, columnspan=2)

mainloop()
