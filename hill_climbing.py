from common import *

# find state where a neighboring queen is not on the same row or diagonal
def findNeighbors(state):
    neighbors = []
    size = int(len(state) / 2)

    for _ in range(size):
        neighbors.append(chooseNewState(state))
    
    return neighbors

def best_neighbor(neighbors):
    bestNeighborState = neighbors[0]
    bestNeighborStateError = numberOfIntersections(bestNeighborState)

    for neighbor in neighbors:
        count = numberOfIntersections(neighbor)

        if count < bestNeighborStateError:
            bestNeighborState = neighbor
            bestNeighborStateError = count

    return bestNeighborState, bestNeighborStateError

def hill_climbing(state):
    currentState = state
    currentStateError = numberOfIntersections(currentState)

    tempStateArray = findNeighbors(currentState)

    bestNeighborState = tempStateArray[0]
    bestNeighborStateError = numberOfIntersections(bestNeighborState)

    START_TIME = time.time()

    file = open("hill_climbing_32x32", "w")

    while currentStateError < bestNeighborStateError:
        neighbors = findNeighbors(bestNeighborState)
        tuple = best_neighbor(neighbors)
        bestNeighborState = tuple[0]
        bestNeighborStateError = tuple[1]
        print("NewStatError count: ", bestNeighborStateError)
        text = "NewStatError count: " + str(bestNeighborStateError)
        file.write(text + "\n")

    END_TIME = time.time()

    print("time span: ", (END_TIME - START_TIME))

    return bestNeighborState, bestNeighborStateError

def main():
    newState = hill_climbing(state32x32)
    printChessBoard(newState[0])

if __name__ == '__main__':
    main()