# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

roundCount = 0
winCount = 0
tieCount = 0

for filename in os.listdir("./point"):
    if filename.endswith(".PLOG"):
        with open("./point/" + filename, "r") as file:
            for line in file:
                round = line.split(",")
                roundCount = roundCount + 1
                if (int(round[1]) > int(round[2])):
                    winCount = winCount + 1
                elif (int(round[1]) == int(round[2])):
                    tieCount = tieCount + 1
        
print("rounds: %d\nwins: %d\nties: %d" % (roundCount, winCount, tieCount))
input()