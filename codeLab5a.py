import random


# deck = []


def print_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()


def user_input():
    while True:
        player_money = int(input("Starting player money: "))
        if player_money < 0 or player_money > 10000:
            print("Invalid amount. Must be from 0 to 10,000")
        else:
            break
    #  Check for valid Bet amounts
    while True:
        print("")
        bet_amount = input("Bet amount: ")
        print()
        if bet_amount == "x":
            break
        bet_amount = int(bet_amount)
        if bet_amount < 5:
            print("The minimum bet is 5")
            continue
        if bet_amount > 1000:
            print("The maximum is bet is 1,000")
            continue
        #  check for enough money
        while True:
            bet_amount = int(bet_amount)
            if bet_amount > player_money:
                print("You don't have enough money to make that bet.")
                bet_amount = input("Bet amount: ")
            else:
                #                print("Move on")
                return player_money, bet_amount

            break
        break


def card_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
    suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [[value + ' of ' + suit, value] for suit in suites for value in values]
    random.shuffle(deck)
    for i in range(len(deck)):
        if deck[i][1] == "Queen":
            deck[i][1] = 10
        elif deck[i][1] == "King":
            deck[i][1] = 10
        elif deck[i][1] == "Jack":
            deck[i][1] = 10
        elif deck[i][1] == "Ace":
            deck[i][1] = 11
    return deck


def deal_card(deck):
    card = deck.pop(0)
    return card


def blackjack_rules(dealer_cards_total, players_cards_total,
                    player_money, bet_amount, dealer_cards,
                    player_cards):
    #    print("dealer_cards_total ", dealer_cards_total)
    #    print("player_cards_total ", players_cards_total)

    #  player busts
    if players_cards_total > 21:
        print("YOUR CARDS: ")
        for cards in player_cards:
            print(cards)

        print("Bummer, your busted!, you loose")
        print("Player money =", player_money - bet_amount)
        play_again()
        exit()







    #  dealer wins
    elif dealer_cards_total > players_cards_total:
        print("Dealer Won!")
        print("Player money ", player_money - bet_amount)
        print()
    #      play_again()
    #      exit()

    return


def play_again():
    play = input("Play again? (y/n:) ")
    if play == "y":
        print("debug")
    elif play == "n":
        print("Bye")
        print()
        print("Come again soon!")
        print()
        exit()


def hit_or_stand(deck, player_cards, players_cards_total,
                 dealer_cards, dealer_cards_total, player_money,
                 bet_amount, cards):
    print()
    response = input("Hit or Stand? (h/s): ")
    print()
    if response == "s":

        while True:

            card = deal_card_dealer(deck)
            dealer_cards.append(card[0])
            print("DEALER'S CARDS: ")
            for cards in dealer_cards:
                print(cards)
            dealer_cards_total = dealer_cards_total + int(card[1])

            # dealer looses to player
            if dealer_cards_total < players_cards_total:
                print("Dealer lost!")
                print("Player money", player_money + bet_amount)
                print()
                #       play_again()
                #      exit()

            # dealer busts
            elif dealer_cards_total > 21:
                print("Yay! Dealer busted, you win!")
                print("Player money = ", player_money + bet_amount)
                print()
                play_again()
                exit()

            print()
            print("YOUR POINTS:     ", players_cards_total)
            print("DEALER'S POINTS: ", dealer_cards_total)
            print()

            blackjack_rules(dealer_cards_total, players_cards_total,
                            player_money, bet_amount, dealer_cards,
                            player_cards)
            continue

    #         print("Yay! Dealer busted, you win!")

    if response == "h":
        card = deal_card(deck)
        player_cards.append(card[0])
        players_cards_total = players_cards_total + int(card[1])

        blackjack_rules(dealer_cards_total, players_cards_total,
                        player_money, bet_amount, dealer_cards,
                        player_cards)

        hit_or_stand(deck, player_cards, players_cards_total,
                     dealer_cards, dealer_cards_total,
                     player_money, bet_amount, card)

        print()
        print("YOUR POINTS:     ", players_cards_total)
        print("DEALER'S POINTS: ", dealer_cards_total)
        print()
        for cards in player_cards:
            print(cards)


    else:
        print('DONE')


def deal_card_dealer(deck):
    card = deal_card(deck)
    #   print("card =", card)
    return card


def main():
    dealer_cards = []
    dealer_cards_total = 0
    player_cards = []
    player_cards_total = 0
    #   player_cards.append()

    print_header()
    player_money, bet_amount = user_input()
    #    print("player money =", player_money)
    print("DEALER'S SHOW CARD:")

    deck = card_deck()
    card = deal_card(deck)
    dealer_cards.append(card[0])
    print(dealer_cards[0])
    print()
    dealer_cards_total = int(card[1])

    print("YOUR CARDS:")
    card = deal_card(deck)
    player_cards.append(card[0])
    player_cards_total = int(card[1])
    card = deal_card(deck)
    player_cards_total = player_cards_total + int(card[1])
    player_cards.append(card[0])
    for cards in player_cards:
        print(cards)

    hit_or_stand(deck, player_cards, player_cards_total,
                 dealer_cards, dealer_cards_total, player_money,
                 bet_amount, card)

    blackjack_rules(dealer_cards_total, players_cards_total,
                    player_money, bet_amount, dealer_cards,
                    player_cards)

    main()


if __name__ == "__main__":
    main()
