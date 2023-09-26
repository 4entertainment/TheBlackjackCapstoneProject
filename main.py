from art import logo
import random

print(logo)
play_flag = True

while play_flag:
    if 'y' != input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
        play_flag = False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    your_cards = []
    for _ in range(0, 2):
        your_cards.append(random.choice(cards))

    dealer_cards = []
    for _ in range(0, 2):
        dealer_cards.append(random.choice(cards))

    flag = True

    while flag:

        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

        print(f"Computer's first card: {dealer_cards[0]}")

        if sum(your_cards) == 21:
            print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
            print("You win!")
            flag = False
        elif sum(dealer_cards) == 21:
            print(f"Computer's final hand: {your_cards}, final score: {sum(your_cards)}")
            print("Computer win!")
            flag = False
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                your_cards.append(random.choice(cards))
            else:
                if sum(your_cards)>sum(dealer_cards):
                    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
                    print("You win!")
                    flag = False
                else:
                    print(f"Computer's final hand: {your_cards}, final score: {sum(your_cards)}")
                    print("Computer win!")
                    flag = False
