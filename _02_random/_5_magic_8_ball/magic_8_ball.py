import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(title="Question", prompt="What question would you like to ask the Magic 8 Ball?")
    # Make a variable and initialize it to a random number between 0 and 3
    randnumb = random.randint(0, 3)
    # If the random number is 0
    if randnumb == 0:
        print("Yes")
        # tell the user "Yes"

    # If the random number is 1
    if randnumb == 1:
        print("No")
        # tell the user "No"

    # If the random number is 2
    if randnumb == 2:
        print("Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if randnumb == 3:
        print("Figure it out yourself")
        # write your own answer
