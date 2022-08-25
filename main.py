def introduction():
    print('Hello! Welcome to a simple tic tac toe game made with python!')
    print('The game is simple, place either X or O on a tile by entering the tile number')
    print('Tile numbers go from 1 to 9 going from the top left to the bottom right')
    print('Do you wish to play single-player, multi-player or view the scoreboard?')

def whiteSpaceCount(list):
    count = 0
    for i in range(0,9):
        if list[i] == ' ':
            count += 1
    return count

def getPlayerName(playerNum):
    return input(f'Player {playerNum} enter your name: ')

def spotValidation(board,spot):
    try:
        spot = int(spot) - 1
    except:
        return False

    if spot < 0 or spot > 8:
        return False
    elif board[spot] != ' ':
        return False
    return True
    

def main():
    introduction()
    choice = input('Enter S, M or V: ')
    
    board = [' '] * 9
    sign = None
    spot = None

    if choice == 'S' or choice == 'M':
        player1 = getPlayerName(1)
        player2 = None

        while True:
            player2 = getPlayerName(2) if choice == 'M' else 'Computer'
            if player2 == player1:
                print('Players must have different names!')
            else:
                break

        sign = 'X'
        while True:
            if sign == 'X':
                spot = input(f'{player1} choose where to place your X: ')
            else:
                spot = input(f'{player2} choose where to place your O: ')

            print(spotValidation(board,spot))
            sign = 'X' if sign == 'O' else 'O'

            if whiteSpaceCount(board) == 0:
                print("It's a tie!")
            
    elif choice == 'V':
        print('Scoreboard')
    else:
        print('Error incorrect input. Game terminated.')

if __name__ == '__main__':
    main()