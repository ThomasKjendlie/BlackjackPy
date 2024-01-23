from random import shuffle
dealer_cards = []
player_cards = []
deck = []

for card in range(2, 10):
    deck += [card]*4
deck += [10]*16
deck += [11]*4

shuffle(deck)

def check_last_ace(hand):
    if sum(hand[:len(hand)-1]) >= 11:
        hand[len(hand) - 1] = 1

# dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(deck.pop())
    if dealer_cards[len(dealer_cards) - 1] == 11:
        check_last_ace(dealer_cards)
    if len(dealer_cards) == 2:
        print("dealer has X ," , (dealer_cards[1]))
while sum(dealer_cards) < 17:
    dealer_cards.append(deck.pop())
    if dealer_cards[len(dealer_cards) - 1] == 11:
        check_last_ace(dealer_cards)

# player_cards
while len(player_cards) != 2:
    player_cards.append(deck.pop())
    if player_cards[len(player_cards) - 1] == 11:
        check_last_ace(player_cards)
    if len(player_cards) == 2:
        print("you have:" , (player_cards))

while sum(player_cards) < 21:
    action = str(input("do you want to draw or stay?:"))
    if action == "draw":
        player_cards.append(deck.pop())
        if player_cards[len(player_cards) - 1] == 11:
            check_last_ace(player_cards)
        print("you have a total of" , str(sum(player_cards)) , "with these cards" , player_cards)
    elif action == "stay":
        print("dealer has a total of" , str(sum(dealer_cards)) , "with these cards" , dealer_cards)
        print("you have a total of" , str(sum(player_cards)) , "with these cards" , player_cards)
        break


if sum(player_cards) > sum(dealer_cards) and sum(player_cards) < 21:
    print("you win!")
elif sum(player_cards) > 21:
    print("you busted, dealer wins!")
elif sum(player_cards) == sum(dealer_cards):
    print("draw!")
elif sum(dealer_cards) == 21:
        print("Dealer has Blackjack!, you lose!")
elif sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) < 21:
    print("you lose! , dealer wins!")
elif sum(player_cards) == 21:
    print("Blackjack!, you win!")
elif sum(dealer_cards) > 21:
    print("dealer busted, you win!")
