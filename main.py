# Importing needed modules
import gameFunctions as game

# Main function where everything comes together
def main():
    game.introduction()
    choice = input('Enter S, M or V: ')
    
    board = [' '] * 9
    sign = None
    player1 = None
    player2 = 'Computer'

    if choice == 'S':
        player1 = game.getPlayerName(1)

        player = player1
        sign = 'X'
        while True:
            if sign == 'X':
                game.getPlayerMove(board, player, sign)
            else:
                game.getComputerMove(board)
            

            if game.whiteSpaceCount(board) == 0:
                game.boardOutput(board)
                print('It is a tie!')
                break
            elif game.checkWinner(board, sign):
                game.boardOutput(board)
                print(f'Player {player} wins!')
                break

            sign = 'X' if sign == 'O' else 'O'
            player = player1 if player == player2 else player2
    elif choice == 'M':
        player1 = game.getPlayerName(1)
        player2 = game.getPlayerName(2, player1)

        player = player1
        sign = 'X'
        while True:
            game.getPlayerMove(board, player, sign)

            if game.whiteSpaceCount(board) == 0:
                game.boardOutput(board)
                print('It is a tie!')
                break
            elif game.checkWinner(board, sign):
                game.boardOutput(board)
                print(f'Player {player} wins!')
                break

            sign = 'X' if sign == 'O' else 'O'
            player = player1 if player == player2 else player2
    elif choice == 'V':
        print('Scoreboard')
    else:
        print('Error incorrect input. Game terminated.')

# Calling the main function
if __name__ == '__main__':
    main()