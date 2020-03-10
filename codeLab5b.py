import random


# deck = []

def card_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
    suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [[value + ' of ' + suit, value]
            for suit in suites
            for value in values]
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


def bet():
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


def deal_card(deck):
    card = deck.pop(0)
    #   print(card)
    return card


def deal_dealer():
    player_cards = deal_card(card_deck())
    print(player_cards)
    return


def deal_player():
    dealer_cards = deal_card(card_deck())
    print(dealer_cards)
    return


def player_show():

    return


def hit_or_stand():
    return


def main():
    dealer_cards = []
    dealer_cards_total = 0
    player_cards = []
    player_cards_total = 0

    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    #    print(card_deck())

    


if __name__ == "__main__":
    main()

# nothing
