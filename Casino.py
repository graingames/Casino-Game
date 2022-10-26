import random, os

# Layout [[card1 info], [card2 info], ...]
# Layout of card1 info -> [id, card_category & card in category (eg 0-2), name]
cards = [[0, "Ace Of Hearts"],[1, "Two Of Hearts"],[2, "Three Of Hearts"],[3, "Four Of Hearts"],[4, "Five Of Hearts"],[5, "Six Of Hearts"],[6, "Seven Of Hearts"],[7, "Eight Of Hearts"],[8, "Nine Of Hearts"],[9, "Ten Of Hearts"],[10, "Jack Of Hearts"],[11, "Queen Of Hearts"],[12, "King Of Hearts"],[13, "Ace Of Spades"],[14, "Two Of Spades"],[15, "Three Of Spades"],[16, "Four Of Spades"],[17, "Five Of Spades"],[18, "Six Of Spades"],[19, "Seven Of Spades"],[20, "Eight Of Spades"],[21, "Nine Of Spades"],[22, "Ten Of Spades"],[23, "Jack Of Spades"],[24, "Queen Of Spades"],[25, "King Of Spades"],[26, "Ace Of Diamonds"],[27, "Two Of Diamonds"],[28, "Three Of Diamonds"],[29, "Four Of Diamonds"],[30, "Five Of Diamonds"],[31, "Six Of Diamonds"],[32, "Seven Of Diamonds"],[33, "Eight Of Diamonds"],[34, "Nine Of Diamonds"],[35, "Ten Of Diamonds"],[36, "Jack Of Diamonds"],[37, "Queen Of Diamonds"],[38, "King Of Diamonds"],[39, "ace Of Clubs"],[40, "Two Of Clubs"],[41, "Three Of Clubs"],[42, "Four Of Clubs"],[43, "Five Of Clubs"],[44, "Six Of Clubs"],[45, "Seven Of Clubs"],[46, "Eight Of Clubs"],[47, "Nine Of Clubs"],[48, "Ten Of Clubs"],[49, "Jack Of Clubs"],[50, "Queen Of Clubs"],[51, "King Of Clubs"]]

def get_blackjack_value(card):
    card_val = card[0] % 13
    if card_val == 0: return -1
    elif card_val <= 9: return card_val + 1
    elif card_val>= 10: return 10

def convert(tokens):
    print("The exchange rate is 100 sakrese for £1 (GBP).")  
    if input("Are you still sure you want to exchange?(y/n) ").lower() == "y":
        x = float(input("How many £ do you want to convert? "))
        tokens += x * 100
        return tokens

def transaction(tokens, bet):
    while True:
        if tokens - bet <= -1:
            print("You don't have enough sakrese!")
            x = input("Do you want to get more sakrese? (y/n) ").lower()
            if x == "y": 
                tokens = convert(tokens)
            elif x == "n":
                return "n", tokens
        elif bet >= 1000:
            print("Sorry the limit is 1000 sakrese.")
            return "n", tokens
        else: return "y",tokens - bet

def blackjack_ai(score, card, player_score):
    card_value = get_blackjack_value(card)
    if card_value == -1: 
        if score + 11 < 22: 
            input(f"The dealer got {card[1]} and chose it to be worth 11! ")
            card_value = 11
        else: 
            input(f"The dealer got {card[1]} and chose it to be worth 1! ")
            card_value = 1
    else: input(f"The dealer got {card[1]}, worth {card_value}!")
    score += card_value
    print(f"The dealers score is {score}")
    if score > 22: 
        input(f"The dealer busted!")
        return -1, card_value
    if score < player_score:
        input(f"The dealer hits!") 
        return True, card_value
    elif score == player_score and score + 6 < 22: 
        input(f"The dealer hits!") 
        return True, card_value
    elif score > player_score: return None, card_value
    else: 
        input("It is a draw!")
        return False, card_value

def player_move(score, card):
    card_value = get_blackjack_value(card)
    if card_value == -1:
        if input(f"You got {card[1]}!\nWhat do you want it to be, 1 or 11? ") == "1": card_value = 1
        else: card_value = 11
    score += card_value
    if score > 21: 
        input(f"You got {card[1]} (worth {card_value}) you ended up busted!")
        return -1, card_value
    else:
        inp = input(f"You got {card[1]} worth {card_value} which has brought your score to {score}!\nDo you want to hit or stand? ").lower()
        if inp == "hit": return True, card_value
        else: return False, card_value

def blackjack(tokens):
    if input("The age old game of blackjack it is. I expect you to know the rules, after all it is the most famous casino game.\nShould we now begin?(y/n) ").lower() == "n": return tokens
    bet = float(input(f"How much are we betting (you have {tokens})? "))
    x, tokens = transaction(tokens, bet)
    if x == "n": return tokens
    # Randomise cards
    cards_copy = cards.copy()
    random.shuffle(cards_copy)
    player_sum = 0
    dealer_sum = 0
    # Shows Dealer's reavealed card
    current_card = cards_copy.pop()
    card_value = get_blackjack_value(current_card)
    if card_value == -1: card_value = 11
    input(f"The dealer's exposed card is {current_card[1]} worth {card_value}")
    dealer_sum += card_value
    # Gets the player 2 cards
    current_card = cards_copy.pop()
    card_value = get_blackjack_value(current_card)
    if card_value == -1: card_value = 11
    input(f"You got {current_card[1]} worth {card_value}")
    player_sum += card_value
    current_card = cards_copy.pop()
    card_value = get_blackjack_value(current_card)
    if card_value == -1:
        if input(f"You got {current_card[1]}!\nWhat do you want it to be, 1 or 11? ") == "1": card_value = 1
        else: card_value = 11
    player_sum += card_value
    inp = input(f"You got {current_card[1]} worth {card_value}.\nIn total you got {player_sum}, hit or stand? ").lower()
    # Actual player choice
    if inp == "hit":
        while True:
            current_card = cards_copy.pop()
            result, card_value = player_move(player_sum, current_card)
            player_sum += card_value
            if result == -1: 
                input(f"The dealer wins and you lose {bet} Sakrese but you still have {tokens} left.")
                return round(tokens)
            elif result == False:
                input(f"You got a total of {player_sum} points!\n It is now the dealers turn.")
                break
    while True:
        current_card = cards_copy.pop()
        result, card_value = blackjack_ai(dealer_sum, current_card, player_sum)
        dealer_sum += card_value
        if result == -1: 
            tokens += bet*2
            input(f"You win and you earned {bet}, now you have {tokens} Sakrese!")
            return round(tokens)
        elif result == False:
            tokens += bet
            input(f"It was a draw and you will get all of your money back.")
            return round(tokens)
        elif result == None:
            input(f"The dealer sadly won even though you got {player_sum}.\nAtleast you still have {tokens} Sakrese.")
            return round(tokens)

def ht(tokens):
    x = input("Coin toss, good choice.\nLet me tell you the rules\n- You will get to chose heads or tails before the coin toss.\n- Afterwards if you win you get 145% of you bet back!\n- If you lose you still get 50% of your bet back!\nIs that fair?(y/n) ").lower()
    if x == "y":
        ans = random.randint(0,1)
        bet = float(input(f"How much are we betting (you have {tokens})? "))
        x, tokens = transaction(tokens, bet)
        if x == "n": return tokens
        input("Heads or tails(h/t): ")
        bet *= 1.45
        if ans==1:
            print("You won!")
            tokens += bet 
            print(f"That means you have won {bet} Sakrese!\nYou now have {tokens} Sakrese!")
        else: 
            tokens += bet
            print("You lost...")
            print(f"You still have {tokens} Sakrese.\nMaybe next time.")
        input("")
        return round(tokens)
    else: return tokens

def pate_win_check(card1 , card2):
    card1 = card1[1][:4]
    card2 = card2[1][:4]
    if card1 == card2: return True
    return False

def pate(tokens):
    if input("The rules are simple.\nWhen you or your oponent have to place a card you must chose a random card in your deck that you and they haven't seen. You place a card on a stack, your oponent places a card on the stack, you place a card on the stack, your oponent places a card on the stack and so on untill someone places a card whith the same value as the previous card. When that happens the person who placed the final card takes all the cards in the stack. The person who gets less than 10 cards first loses. You win get 145% of your bet back. Values for the cards are standard.\nShould we begin (y/n)?\n").lower() == "y":
        os.system("cls")
        player_cards = cards[:26]
        ai_cards = cards[26:]
        input("You and your oponent have been dished out 26 cards each.")
        while len(player_cards) > 9 and len(ai_cards) > 9:
            random.shuffle(player_cards)
            random.shuffle(ai_cards)
            stack = []
            prev_card = "zzzzz"
            while True:
                placed_card = ai_cards.pop()
                stack.append(placed_card)
                input(f"It was your oponents turn and they placed {placed_card[1]}")
                if pate_win_check(placed_card, prev_card): 
                    for item in enumerate(stack): ai_cards.append(item)
                    input(f"Your oponent won {len(stack)} cards and now the have {len(ai_cards)} versus your {len(player_cards)}!")
                    break
                prev_card = placed_card
                stack.append(placed_card)
                input("Press enter to place a card.")
                placed_card = player_cards.pop()
                input(f"You placed {placed_card[1]}")
                if pate_win_check(placed_card, prev_card): 
                    for item in enumerate(stack): player_cards.append(item)
                    input(f"You won {len(stack)} cards and now you have {len(player_cards)} versus their {len(ai_cards)}!")
                    break

pate(1000)

"""
tokens = 1000
while True:
    os.system("cls")
    inp = input("What do you want to play?\nHeads and tails (1) or blackjack (2): ")
    if inp == "1": tokens = ht(tokens)
    elif inp == "2": tokens = blackjack(tokens)
"""
