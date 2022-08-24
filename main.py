def introduction():
    print('Hello! Welcome to a simple tic tac toe game made with python!')
    print('The game is simple, place either X or O on a tile by entering the tile number')
    print('Tile numbers go from 1 to 9 going from the top left to the bottom right')

def main():
    introduction()
    choice = input('Do you wish to play single player or multi player? Enter 1 or 2: ')
    
    if choice == '1':
        print('Single player!')
    elif choice == '2':
        print('Multi player')
    else:
        print('Error incorrect input. Game terminated.')

    """
    spots = [' '] * 9
    for i in range(0,3):
        print(f' {spots[i]} | {spots[i+1]} | {spots[i+2]} ')
        if i != 2:
            print('------------')
    """

if __name__ == '__main__':
    main()