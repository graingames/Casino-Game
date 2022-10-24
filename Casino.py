import random
card_identifier = [i for i in range(52)]
cards = ['0-0', '1-0', '2-0', '3-0', '4-0', '5-0', '6-0', '7-0', '8-0', '9-0', '10-0', '11-0', '12-0', '0-1', '1-1', '2-1', '3-1', '4-1', '5-1', '6-1', '7-1', '8-1', '9-1', '10-1', '11-1', '12-1', '0-2', '1-2', '2-2', '3-2', '4-2', '5-2', '6-2', '7-2', '8-2', '9-2', '10-2', '11-2', '12-2', '0-3', '1-3', '2-3', '3-3', '4-3', '5-3', '6-3', '7-3', '8-3', '9-3', '10-3', '11-3', '12-3'] 
cards_names = ['Ace of hearts', 'two of hearts', 'three of hearts', 'four of hearts', 'five of hearts', 'six of hearts', 'seven of hearts', 'eight of hearts', 'nine of hearts', 'ten of hearts', 'jack of hearts', 'queen of hearts', 'king of hearts', 'Ace of spades', 'two of spades', 'three of spades', 'four of spades', 'five of spades', 'six of spades', 'seven of spades', 'eight of spades', 'nine of spades', 'ten of spades', 'jack of spades', 'queen of spades', 'king of spades', 'Ace of diamonds', 'two of diamonds', 'three of diamonds', 'four of diamonds', 'five of diamonds', 'six of diamonds', 'seven of diamonds', 'eight of diamonds', 'nine of diamonds', 'ten of diamonds', 'jack of diamonds', 'queen of diamonds', 'king of diamonds', 'ace of clubs', 'two of clubs', 'three of clubs', 'four of clubs', 'five of clubs', 'six of clubs', 'seven of clubs', 'eight of clubs', 'nine of clubs', 'ten of clubs', 'jack of clubs', 'queen of clubs', 'king of clubs'] 
def convert(tokens):
    print("The exchange rate is 100 sakrese for £1 (GBP).")  
    if input("Are you still sure you want to exchange?(y/n) ").lower() == "y":
        x = float(input("How much do you want to convert? "))
        tokens += x * 100
        return tokens

def transaction(tokens, bet):
    while True:
        if tokens - bet <= -1:
            print("You don't have enough sakrese!")
            x = input("Do you want to get more sakrese?(y/n) ").lower()
            if x == "y": 
                tokens = convert(tokens)
            elif x == "n":
                return "n", tokens
        elif bet >= 5000:
            print("Sorry the limit is 5000 sakrese.")
            return "n", tokens
        else: return "y",tokens - bet



def ht(tokens):
    x = input("Coin toss, good choice.\nLet me tell you the rules\n- You will get to chose heads or tails before the coin toss.\n- Afterwards if you win you get 145% .of you bet back!\n- If you lose you still get 50% .of your bet back!\nIs that fair?(y/n) ").lower()
    if x == "y":
        ans = random.randint(0,1)
        bet = float(input("How much are we betting? "))
        x, tokens = transaction(tokens, bet)
        if x == "n": return tokens
        Choice = input("Heads or tails(h/t): ").lower()
        if Choice=="h":
            if ans==1:
                print("You won!")
                tokens += bet *1.45
                print(f"That means you have got {bet * 1.45} sakrese!\nYou now have {tokens} sakrese!")
            else: 
                tokens = tokens + (bet*0.5)
                print("You lost...")
                print(f"You still have {tokens} sakrese.\nMaybe next time.")
        else: 
            if ans==0:
                print("You won!")
                tokens += bet *1.45
                print(f"That means you have got {bet * 1.45} sakrese!\nYou now have {tokens} sakrese!")
            else:
                tokens = tokens + (bet*0.5)
                print("You lost...")
                print(f"You still have {tokens} sakrese.\nMaybe next time.")
        return tokens
    else: return tokens

def blackjack(tokens):
    if input("The age old game of blackjack it is. I expect you to know the rules, after all it is the most famous casino game.\nShould we now begin?(y/n) ").lower() == "n": return tokens
    bet = float(input("How much are we betting? "))
    x, tokens = transaction(tokens, bet)
    if x == "n": return tokens
    y = random.sample(card_identifier, 52)
    print(y)   
    for i in y:
        cards[i], cards[y[i]] = cards[y[i]], cards[i]
        cards_names[i], cards_names[y[i]] = cards_names[y[i]], cards_names[i]
    print(f"The dealers turned up card is {cards_names[-1]}")

tokens = 1000
blackjack(tokens)
