"""
Project name: number_guesser
Author: Dhrithik Raj
Date: 21-08-2023
"""

#Importing necessary modules
from tkinter import *   #For GUI
import random           #For generating a random number

#Defining the function which decies what the GUESS function does
def button_click():
    guessed_number = guess.get()
    guess.delete(0, END)
    global number_of_guesses
    number_of_guesses += 1
    if number_of_guesses >= 6:  #You get 6 chances to get the number
        output.delete(0, END)
        guess.insert(0, "your 6 chances are over")
        button.config(state=DISABLED) #After 6 chances, the button is disabled
    if number == int(guessed_number):   #For correct guess
        output.delete(0, END)
        output.insert(0, "is " + str(guessed_number) + "! Very good!")
        button.config(state=DISABLED)
    if number > int(guessed_number): 
        output.delete(0, END)
        result = "is greater than "
        output.insert(0, result + str(guessed_number))
    if number < int(guessed_number):
        output.delete(0, END)
        result = "is lesser than "
        output.insert(0, result + str(guessed_number))


main_window = Tk()  #Creating the main window
main_window.title("Number Guesser") #Giving the window a title

number_of_guesses = 0 #Variable to store the number of guesses
list_of_two_digit_numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
global number
number = random.choice(list_of_two_digit_numbers) #Variable to store mystery number


message = Label(main_window, text="Guess the two-digit mystery number: ", font="arial 18")
message.grid(row=0, column=0)

guess = Entry(main_window, width=35, borderwidth=5)
guess.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

button = Button(main_window, text="Guess", font="Arial 16", padx=40, pady=15, command=button_click)
button.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

instruction = Label(main_window, text="The mystery number: ", font="arial 18")
instruction.grid(row=3, column=0)

output = Entry(main_window, width=35, borderwidth=5)
output.grid(row=4, column=0, columnspan=3, padx=20, pady=10)


main_window.mainloop()
