# First, import the logo from art.py
from art import logo

import os
import random

def clear():
    """Clears the console"""# Note this is the proper use of a Docstring, to inform other programmers of what something does
    command = 'clear'
    # If statement to check to see what OS the computer is running. The "clear" command in windows is "cls", so if the computer is running Windows it changes the command so it works
    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command) 

def deal_card():
    # Create the docstring
    """Returns a random card from the deck"""
    # Royalty are all 10
    # Ace as 11
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Use the random module with the choice method passing in the cards list and set it to a variable
    card = random.choice(cards)
    # Use the return keyword to return the card variable
    return card

# print(deal_card())

def calculate_score(cards): #Note this "cards" arguement is seperate from the cards variable in the above function because of Scope
    """Take a list of cards and returns the score calculated from the cards"""
    # Create an if statement to check to see if a player has a Black Jack Hand (2 card, an ace and 10)
    if sum(cards) == 21 and len(cards) == 2: #num sum() and len() are both built in Python Functions
        # Return 0 to represent our BlackJack hand, we will use this instead of 21 to differentiate it from the normal score of 21
        return 0
    # Create an if statement that says if 11 is in the cards list, and the sum is less than 21 change 11 to 1 so as to not bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # return the sum of the cards after all the above if statements have been checked
    return sum(cards)

def compare(user_score, computer_score):
    """Pass in both the user's score and the computer's as arguments"""
    # Use if/elif./else statements for each outcome
    # Draw 
    if user_score == computer_score:
        return "Draw" 
    # Computer has BlackJack
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    # User has Blackjack
    elif user_score == 0:
        return "Win with a Blackjack! Wooo!"
    # User Bust
    elif user_score > 21:
        return "You went over. You lose :("
    # Computer Busts
    elif computer_score > 21:
        return "Opponent went over. You win!"
    # User win
    elif user_score > computer_score:
        return "You win! :D"
    # Computer win
    else:
        return "You LOSE booo"

    # Create Game Function- function run to start the game
def playgame():
    # Print Logo in the Terminal
    print(logo)

    # Create empty lists for 
    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2): #underscore indicates an un-needed variable
        # Use the append method with each empty list and pass in our deal_card function
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # Our loop will run only twice, and each time our deal_card() function will output a random card. The append() metho will then add that card to the appropriate lists

    # Create a while loop to "play the game" this is also known as a game loop

    while not is_game_over:
    # We use the "not" keyword to indicate this loo

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Using print statements and f-strings, have the current score of the user and the first card of the computer's hand display
        # Note in BlackJack you can always see the first card dealt to your opponent but not the second one
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        # is_game_over = True

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True #Ends the game loop
        else: 
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")

    print(compare(user_score, computer_score))

# Final loop that takes the user's input to start or leave the program
while input("Want to play Blackjack? Type 'y' to start, hit enter to leave: "):
    # use clear() function we created to clear all old output and hides the command line from view
    clear()
    # Start the game over
    playgame()

# playgame()