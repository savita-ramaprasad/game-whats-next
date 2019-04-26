#!/usr/bin/env python


from numpy import random
from sequence import *

def start_game():
    """ Define a sequence object.
    Return:
        seq (Sequence): Returns Sequence object
    """ 
    r = random.randint(1, 6)
    if r == 1:
        seq = GeomSeq()
    elif r == 2:
        seq = ArithmSeq()
    elif r == 3:
        seq = Fibonacci()
    elif r == 4:
        seq = Triangle()
    else:
        seq = Power()

    #num_terms_to_display = 4
    
    print("First %d terms of the sequence:"%(NUM_TERMS_TO_DISPLAY))
    for num in range(1, NUM_TERMS_TO_DISPLAY + 1):
        print(seq.nth_term(num))
    
    return seq

def play_game(seq):
    """ Allow user to play game. 
        
    Raises: ValueError: number entered is non-integer or non-Enter.
    """
    
    points = 50
    points_lost_at_every_turn = 10

    while points != 0:

        print("What's next? Enter your guess. No idea? You can see the \
%dth term (by hiting Enter) and then guess the %dth term"
              %(seq.term_count() + 1, seq.term_count() + 2))

        user_input = input()
        restart_or_quit(user_input)
        while True:
            if user_input != '':
                try:
                    user_input = int(user_input)
                    if seq.verify_ans(int(user_input)) == 1:
                        EOG_msg(points)
                        user_input =input()
                        EOG(user_input)
                    else:
                        EOG_msg(-1)
                        user_input = input()
                        EOG(user_input)
                    break
                except ValueError:
                    print("Please hit enter or enter an integer")
                user_input = input()
                restart_or_quit(user_input)
            else:
                break
        if user_input != '':
            break
        else:
            print("This is term number %d of the series: %d" %
                  (seq.term_count() + 1, seq.next_term()))
            points -= points_lost_at_every_turn
            print("You have %d points" % (points))

    if points == 0:
        EOG_msg(points)
        user_input = input()
        EOG(user_input)


def restart_or_quit(user_input):
    """ Quit game if user input is Q/q. Restart if R/r.
    
        Args: 
            user_input (str): Q/q if user wants to quit game
    """
    if user_input == 'Q' or user_input == 'q':
        quit()
    elif user_input == 'R' or user_input == 'r':
        seq = start_game()
        play_game(seq)


def EOG_msg(points):
    """ Print appropriate msg when game ends.
    
        Args: 
            points (int): Uses points to determine msg.
    """
    if points == 0:
        print("Game over! You have 0 points :(")
    elif points > 0:
        print("You win with %d points!" % (points))
    else:
        print("Game over!")

    print("Press Q/q and enter to quit. Press R/r and enter to play again")

def EOG(user_input):
    """ Quit if Q/q or restart if anything else. """

    if user_input == 'Q' or user_input == 'q':
        quit()
    else:
        seq = start_game()
        play_game(seq)

            
def main():

    rules_of_the_game = """
***********************************
Welcome to the 'What's Next?' game!
***********************************
You will be shown the first four terms of a sequence. You start with
50 points. You have to enter the fifth term of the sequence. If your 
answer is correct you win with 50 points. If you are not sure, you can 
see more terms. For example, you can see the fifth term and then make a
guess for the sixth term. Every time you uncover a term you lose 10 
points. If you give the correct answer at any stage you win with points
that are remaining. The game is over either when you have given the 
answer or have lost all 50 points. To quit the game at any time press Q/q.
You can re-start by pressing R/r. \n \n \n
"""

    print(rules_of_the_game)
    seq = start_game()
    play_game(seq)


if __name__ == "__main__":
    main()
