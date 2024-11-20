print("SV Nguyen Dinh Hai")
print(" MSSv 235752021610028")
print("#########################")
import tkinter as tk
import random

# List of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 120  # Thay đổi thời gian chơi thành 120 giây

# Function to start the game
def startGame(event):
    global timeleft, score
    if timeleft == 120:  # Game is just starting
        countdown()  # Start the countdown timer
    nextColour()  # Choose the next colour

# Function to choose and display the next colour
def nextColour():
    global score
    if timeleft > 0:
        e.focus_set()  # Make the text entry box active
        # If the colour typed matches the colour of the text
        if e.get().lower() == colours[0].lower():
            score += 2  # Cộng 2 điểm nếu đoán đúng
        else:
            score -= 1  # Trừ 1 điểm nếu đoán sai
        e.delete(0, tk.END)  # Clear the text entry box
        random.shuffle(colours)  # Shuffle the colours
        # Update the label with a new colour
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))  # Update score display

# Countdown timer function
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1  # Decrement the timer
        timeLabel.config(text="Time left: " + str(timeleft))  # Update the time left label
        timeLabel.after(1000, countdown)  # Run the countdown function again after 1 second
    else:
        timeLabel.config(text="Time's up!")  # Time's up when the timer hits zero
        scoreLabel.config(text="Final Score: " + str(score))  # Display final score
        e.config(state=tk.DISABLED)  # Disable the text entry after time is up

# Driver Code
root = tk.Tk()
root.title("COLORGAME")
root.geometry("375x300")  # Set window size

# Instructions Label
instructions = tk.Label(root, text="Type in the colour of the words, and not the word text!",
                        font=('Helvetica', 12))
instructions.pack()

# Score Label
scoreLabel = tk.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Time left Label
timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Label to display the colours
label = tk.Label(root, font=('Helvetica', 60))
label.pack()

# Text Entry box for typing in the colour
e = tk.Entry(root)
e.pack()
e.focus_set()

# Run the 'startGame' function when the Enter key is pressed
root.bind('<Return>', startGame)

# Start the GUI
root.mainloop()
