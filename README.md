# RISK
A Python script to calculate winning probabilities in the board game Risk.

![Alt Text](samples/surface.png?raw=True "Probability Surface")

The script outputs a table containing the probabilities of the attacker gaining territory,
given specific numbers of attackers and defenders involved in a conflict.

In addition to being useful for decision-making while in game, this project is also a nice
application of dynamic programming. It is able to accurately and very quickly compute
results for conflicts involving hundreds of units (although the graph will not be
able to present this data nicely).


# Installation

Clone from git using: ```git clone https://github.com/IanYHWu/RISK.git```


# Usage

An example table for conflicts involving up to 20 units on each side is available in the
samples file. The corresponding probability surface is also available in the same folder.

![Alt Text](samples/table_2020.png?raw=True "Probability Matrix for up to 20 vs. 20")

The main script ```risk.py``` is contained in the ```src``` folder. To run the 
script, call ```python risk.py``` from the command line.

The ```basic_rolls.py``` file is used to estimate the probabilities of each side winning 
a "basic" conflict - one involving a small and unique combination of troops that can be 
resolved with a single set of dice throws. This does not need to be run directly, as the
results are already contained in the main file.
