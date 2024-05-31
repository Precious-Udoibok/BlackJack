#importing the random module and art.py module
import random
from art import clear,logo 

#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    '''Picks a random card from the list of cards'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score.
def calc_score(cards):
#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead
    if sum(cards) == 21 and len(cards) == 2:
# 0 will represent a blackjack in our game.
        return 0
    
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. 
#You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

 #Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. 
 #If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
 #If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. 
 #If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Its a draw 😙'
    elif computer_score == 0:
        return 'You lose  opponent had a blacjack 😱'
    elif user_score == 0:
        return 'You win with a blacjack 😎'
    elif user_score > 21:
        return 'You lose, You went over 🥺'
    elif computer_score > 21:
        return 'You win, Opponent went over 😇'
    elif user_score > computer_score:
        return 'You Win 😊'
    else:
        return 'You lose 😫'
    
# Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    print(logo) #display the logo from art.py
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

#The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
#Hint 9
#Call calculate_score(). 
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f'Your card {user_cards}, current score {user_score}')
        print(f'Computer first hand {computer_cards[0]}')

#If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            another_card = input('Type y to get another card or type n to pass: ')
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print(f'Your final hand {user_cards}    Current Score {user_score}')
    print(f'Computer final hand {computer_cards}   Computer Final score {computer_score}')
    print(compare(user_score,computer_score))


#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input('Do you want to play a game of blackjack (y/n): ') == 'y'.lower():
    clear()
    play_game()
