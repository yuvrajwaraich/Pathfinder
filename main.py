from algo import Algorithms
import pathfinder_gui
import DataStructures


def main():
    choice = pathfinder_gui.options()
    pathfinder_gui.main()
    alg = Algorithms()
    if choice == "BF":
        alg.Breadthfirst()
    elif choice == "DF":
        alg.Depthfirst()
    elif choice == "A*":
        alg.aStar()

if __name__ == "__main__":
    main()
