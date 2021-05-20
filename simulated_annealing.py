# Course CS3642
# Student name: Steven Crowther
# Student ID: 000745923
# Assignment #: 2
# Due Date 4/16/2021

import random
import numpy
import math

from common import *
"""

state = [[1, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1]]

# counts the number of queens in all the diagonals
def numberOfQueensInDiagonal(currentState):
    array = []
    
    # converts currentState to diagonal subarrays and appends to array
    for i in range(-7, 8, 1):
        array.append(numpy.diagonal(currentState, i))
    
    count = numberOfQueensInRow(array)

    # resets array
    array = []

    # reverse each row of array and appends to array
    for row in currentState:
        array.append(row[::-1])
    
    count += numberOfQueensInRow(array)

    return count

# counts the number of queens in all rows
def numberOfQueensInRow(currentState):
    count = 0
    
    for row in currentState:
        row_count = 0

        for column in row:
            if column == 1:
                row_count += 1

        if row_count > 1:
            count += 1

    if count > 0:
        return count
    else:
        return 0

# calculated collective intersections
def numberOfIntersections(currentState):
    count = numberOfQueensInDiagonal(currentState)
    count += numberOfQueensInRow(currentState)
    return count

# generate new State of board
def chooseNewState(currentState):
    rowNumber = random.randint(0, 7)
    # 1 means up and 0 means down
    direction = random.randint(0, 1)

    if (rowNumber == 0 and direction == 1) or (rowNumber == 7 and direction == 0):
        return currentState
    else: # goes through each column of row to flip "queen" with correspending cells
        for column in range(len(currentState[rowNumber])):
            if currentState[rowNumber][column] == 1:
                if direction == 1:
                    currentState[rowNumber][column] = 0
                    currentState[rowNumber - 1][column] = 1
                else:
                    currentState[rowNumber][column] = 0
                    currentState[rowNumber + 1][column] = 1
        return currentState
  
# prints board
def printChessBoard(state):
    for row in range(len(state)):
        print("|", end="")
        for columm in range(len(state[row])):
            if state[row][columm] == 1:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print()
        print("---------------------------------")
"""
def simulated_annealing(state):
    currentTemp = 1
    print("Start Temp: ", currentTemp)
    minimumTemp = 0.001
    alpha = 0.99
    currentState = state
    currentStateErrors = numberOfIntersections(currentState)
    newState = None
    newStateErrors = 0
    iterations = 4

    start_time = time.time()
    file = open("simulated_annealing_16x16", "w")
    while currentTemp > minimumTemp:
        for i in range(0, iterations):
            newState = chooseNewState(currentState)
            errorCount = numberOfIntersections(newState)
            print("Current state error count :", errorCount)
            text = "Current state error count :" + str(errorCount) + "\n"
            file.write(text)
            if errorCount == 0:
                return currentState
        
        # calulate probility of success
        if math.pow(math.e, ((newStateErrors - currentStateErrors) / currentTemp)) >= random.uniform(0, 1):
            currentState = newState
            currentStateErrors = newStateErrors
        currentTemp *= alpha
    
    end_time = time.time()
    print("time span: %f", (end_time - start_time))
    return currentState

def main():
    solution = simulated_annealing(state16x16)
    printChessBoard(solution)

if __name__ == '__main__':
    main()