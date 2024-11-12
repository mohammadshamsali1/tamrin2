import random

def simulate_gambler(initial_balance, bet_amount):
    balance = initial_balance
    while balance > 0:
        result = random.choice(["win", "lose"])
        if result == "win":
            balance += bet_amount
            print(f"Win! Current balance: {balance}")
        else:
            balance -= bet_amount
            print(f"Lose! Current balance: {balance}")
        if balance >= 2 * initial_balance:
            print("Gambler has doubled the initial balance and won!")
            break
    if balance <= 0:
        print("Gambler has gone bankrupt.")
    return balance

def find_optimal_bet(initial_balance, num_trials=1000):
    best_bet = 0
    best_win_rate = 0
    for bet_amount in range(1, initial_balance // 2 + 1):
        wins = 0
        for _ in range(num_trials):
            if simulate_gambler(initial_balance, bet_amount) > 0:
                wins += 1
        win_rate = wins / num_trials
        if win_rate > best_win_rate:
            best_bet = bet_amount
            best_win_rate = win_rate
    return best_bet, best_win_rate

initial_balance = 3
optimal_bet, win_rate = find_optimal_bet(initial_balance)

print(f"The optimal bet amount is {optimal_bet} with a win rate of {win_rate:.2f}")
