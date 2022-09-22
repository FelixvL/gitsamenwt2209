# Johnny Liang 11185163


import random
import numpy as np
import math
from matplotlib import pyplot as plt

def throw_two_dice():

    # two die, randomly thrown, returning a number between 1 and 6
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    dice_sum = dice1 + dice2
    return dice_sum

def simulate_monopoly(starting_money_p1, starting_money_p2):

    possessions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0]

    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                0, 320, 200, 0, 350, 0, 400]

    # Keep track of each player's position and possession count
    possession_count_p1 = 0

    possession_count_p2 = 0

    position_p1 = 0

    position_p2 = 0

    # game continues as long as not all properties have been bought
    while possession_count_p1 + possession_count_p2 < 28:

        # player 1 and 2 throw the die
        steps_p1 = throw_two_dice()
        steps_p2 = throw_two_dice()

        # player 1 moves around the board
        if position_p1 + steps_p1 <= 39:
            position_p1 += steps_p1
        else:
            position_p1 = (position_p1 + steps_p1) % 40
            starting_money_p1 += 200

        # player 1 lands on a position and checks if he/she can buy
        if board_values[position_p1] != 0 and possessions[position_p1] == 0 and starting_money_p1 >= board_values[position_p1]:
            possessions[position_p1] = 1
            starting_money_p1 -= board_values[position_p1]
            possession_count_p1 += 1

        # player 2 moves around the board
        if position_p2 + steps_p2 <= 39:
            position_p2 += steps_p2
        else:
            position_p2 = (position_p2 + steps_p2) % 40
            starting_money_p2 += 200

        # player 2 lands on a position and checks if he/she can buy
        if board_values[position_p2] != 0 and possessions[position_p2] == 0 and starting_money_p2 >= board_values[position_p2]:
            possessions[position_p2] = 1
            starting_money_p2 -= board_values[position_p2]
            possession_count_p2 += 1

        delta = possession_count_p1 - possession_count_p2

    return delta

# function simulates monopoly games and gives average difference of possessions per game
def simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2):

    difference_per_game = []

    # keep track of the difference of property owned for each game
    for game in range(0, total_games):
        difference = simulate_monopoly(starting_money_p1, starting_money_p2)

        difference_per_game.append(difference)

    difference_game = sum(difference_per_game)/len(difference_per_game)

    return difference_game

# 
def equilibrium():

    extra = 0

    while extra < 200:

        # starting point playing 10k games and even starting money
        total_games = 10000
        starting_money_p1 = 1500
        starting_money_p2 = 1500

        starting_money_p2 += extra

        diff = simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2)

        print(f"Starting money {[starting_money_p1, starting_money_p2]}: player 1 on average {diff} more streets (player 2 {extra} euros extra)")

        # add 50 to extra so next 10k games player 2 will have +50 starting money compared to player 1
        extra += 50

        print("Monopoly simulator: 2 players. On average, if player 2 receives 100 euros more starting money, both players collect an equal number of streets")

    return extra

equilibrium()
