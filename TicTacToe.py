theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

boardKeys = []
for key in theBoard:
    boardKeys.append(key)
# print(boardKeys)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("-+-+-")


# printBoard(theBoard)


# setting up the player's turn
# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It is the turn of player," + turn + ".specify the place you want to go")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("The location is already filled chose another location")
            continue
        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGameOver boy\n")
                print("player " +turn + " won the game")
                break
        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over\n")
            print("The game is a tie!...buddy")
        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to restart the game ? (y/n)")
    # Now we will ask if player wants to restart the game or not.
    if restart == 'y' or restart == 'Y':
        for key in boardKeys:
            theBoard[key] = ' '
        game()


if __name__ == "__main__":
    game()
