"""
A script to calculate the probabilities for each outcome of the basic rolls - (1, 1), (2, 1), (3, 1), (2, 2), (3, 2). 

29/08/20
"""

import random

def attacker(p):
    """Rolls the dice for the attacker"""

    attacker_rolls = []
    for i in range(0,p):
        roll = random.randint(1,6)
        attacker_rolls.append(roll)

    return attacker_rolls


def defender(q):
    """Rolls the dice for the defender"""

    defender_rolls = []
    for i in range(0,q):
        roll = random.randint(1,6)
        defender_rolls.append(roll)

    return defender_rolls


def play(p, q):
    """Plays out an individual battle (i.e. both players "throw the dice"). Returns the number of kills for the attacker (attack_score) and defender (defend_score)"""

    # roll the dice
    attacker_rolls = attacker(p)
    defender_rolls = defender(q)

    # sort the dice, for comparison
    sorted_attack = sorted(attacker_rolls, reverse = True)
    sorted_defend = sorted(defender_rolls, reverse = True)

    attack_score = 0
    defend_score = 0

    conflict_size = min(p,q)

    # skirmish - compare dice, accounting for conflict size
    for i in range(0,conflict_size):
        if sorted_attack[i] > sorted_defend[i]:
            attack_score += 1
        else:
            defend_score += 1

    return attack_score, defend_score


def compute_odds(N):
    """Computes the odds of the basic rolls. Computes N simulations per basic roll"""

    # last of basic matchups
    matchup_list = [(1,1), (2,1), (3,1), (1,2), (2,2), (3,2)]
    results_list = []

    for matchup in matchup_list:
        # for matchups where one side only has one unit, there are only two outcomes
        if min(matchup) == 1:
            result = [0, 0]
            # simulate N times
            for trial in range(0, N):
                # simulate a battle, record the score
                attack_score, defend_score = play(*matchup)
                if attack_score == 1:
                    result[0] += 1
                else:
                    result[1] += 1
            # using the summed scores, compute probabilities
            for val in range(0, 2):
                result[val] = float(result[val])/N
        # for matchups where both sides have more than 1 unit, there are three outcomes
        else:
            result = [0, 0, 0]
            for trial in range(0, N):
                attack_score, defend_score = play(*matchup)
                # attacker gets two kills...
                if attack_score == 2:
                    result[0] += 1
                # defender gets two kills...
                elif defend_score == 2:
                    result[2] += 1
                # one kill each
                else:
                    result[1] += 1
            for val in range(0, 3):
                result[val] = float(result[val])/N
        results_list.append(result)

    return results_list


if __name__ == '__main__':
    # N gives the number of simulations performed
    results_list = compute_odds(N = 1000000)
    print(results_list)











