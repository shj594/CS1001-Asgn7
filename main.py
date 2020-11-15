import random

EXIT = "q"
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
LIZARD = "lizard"
SPOCK = "spock"

# must return True if the first throw wins or tie; False otherwise
def compare(first_throw, second_throw):
    # TODO: implement; use get_message to determine the rules
    return True

def get_message(winning_throw, losing_throw):
    if winning_throw == losing_throw:
        return "It's a tie!"
    if winning_throw == SCISSORS and losing_throw == PAPER:
        return SCISSORS + " cuts " + PAPER
    if winning_throw == PAPER and losing_throw == ROCK:
        return PAPER + " covers " + ROCK
    if winning_throw == ROCK and losing_throw == SCISSORS:
        return ROCK + " crushes " + SCISSORS
    if winning_throw == SCISSORS and losing_throw == LIZARD:
        return SCISSORS + " decapitates " + LIZARD
    if winning_throw == LIZARD and losing_throw == SPOCK:
        return LIZARD + " poisons " + SPOCK
    if winning_throw == SPOCK and losing_throw == SCISSORS:
        return SPOCK + " smashes " + SCISSORS
    if winning_throw == SPOCK and losing_throw == ROCK:
        return SPOCK + " vaporizes " + ROCK
    if winning_throw == ROCK and losing_throw == LIZARD:
        return ROCK + " crushes " + LIZARD
    if winning_throw == LIZARD and losing_throw == PAPER:
        return LIZARD + " eats " + PAPER
    if winning_throw == PAPER and losing_throw == SPOCK:
        return PAPER + " disproves " + SPOCK
    return "N/A"

def main():
    # prompt with exit instructions
    print("\nYou can enter q at any time to exit!\n")

    while True:
        # prompt for first throw; retrieve user input
        first_throw = input("Type rock, paper, scissors, lizard, or spock: ")
        first_throw = first_throw.strip().lower()

        # check for exit
        if first_throw == EXIT:
            break
        
        # prompt for second throw; retrieve user input
        second_throw = input("Type rock, paper, scissors, lizard, spock or hit ENTER: ")
        second_throw = second_throw.strip().lower()

        # check for exit
        if second_throw == EXIT:
            break
        
        # check for random throw; randomly generate throw if needed
        if second_throw == "":
            possible = [ ROCK, PAPER, SCISSORS, LIZARD, SPOCK ]
            second_throw = possible[int(len(possible)*random.random())]
        
        # compare the two throws
        first_throw_wins = compare(first_throw, second_throw)

        # print result
        if first_throw_wins:
            print(get_message(first_throw, second_throw))
        else:
            print(get_message(second_throw, first_throw))

    return

if __name__ == "__main__":
    main()