#Author: Ashley Johnson
#Date: 5/3/2021
#Description: Program starts with a puzzle board of non-negative numbers. A token starts on
#leftmost square and on each turn, the token can move left or right equal to the number of
#squares equal to the value of the current square. The token can not move off the board on
#either end. If the token can reach the rightmost square, the puzzle the solvable and the program
#returns true. If the token can not reach the rightmost square, the puzzle can not be solved and
#the program returns false.
import time


def row_puzzle(puzzle_list, current_position=0, tried_set=None):
    """function checks if it is possible to move left or right from current position and
    checks if the move has already been tried. If the move is both possible and has not
    been tried, function moves in that direction and updates tried list to set. """
    tried = []
    if not tried_set:
        tried_set = {}
        tried = []
    else:
        tried = list(tried_set)

    last_position = len(puzzle_list)-1
    if(current_position == last_position):
        possible = True
    else:

        if current_position in tried_set:
            print("has already been to position: {}".format(current_position))
            possible = False
        else:
            tried.append(current_position)
            possible = False

            if puzzle_list[current_position] == 0:
                possible = False

            new_left = current_position - puzzle_list[current_position]
            new_right = current_position + puzzle_list[current_position]
            if new_left > 0 and row_puzzle(puzzle_list,new_left, set(tried)):
                print("we went left from position {}".format(current_position))
                return True
            if new_right < len(puzzle_list) and row_puzzle(puzzle_list, new_right, set(tried)):
                print("we went right from postion {}".format(current_position))
                return True
    print("returning possible = {}".format(possible))
    return possible


def main(argv=None):
    """
    Entry Point
    """
    tile_list = [2, 4, 5, 3, 1, 3, 1, 4, 0]
    if row_puzzle(tile_list):
        print("puzzle is solved")
    else:
        print("puzzle can not be solved")



if __name__ == "__main__":

    main()