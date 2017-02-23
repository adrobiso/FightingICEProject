# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

roundCount = 0
p1winCount = 0
p2winCount = 0
tieCount = 0

for filename in os.listdir("./point"):
    if filename.endswith(".PLOG"):
        with open("./point/" + filename, "r") as file:
            for line in file:
                round = line.split(",")
                roundCount = roundCount + 1
                if (int(round[1]) > int(round[2])):
                    p1winCount = p1winCount + 1
                elif (int(round[1]) == int(round[2])):
                    tieCount = tieCount + 1
                else:
                    p2winCount = p2winCount + 1
                        
        
print("rounds: %d\np1 wins: %d\np2 wins: %d\nties: %d" % (roundCount, p1winCount, p2winCount, tieCount))
input()