#Erik Dunlap
#A Game of Rock, Paper, Scissors

import random

def main():
    answer= removeNonLetters(list(input('Do you want to play Rock, Paper, Scissors? (yes or no): ').lower()))
    while True:
        if answer== ['y', 'e', 's'] or answer== ['y']:
            break
        elif answer== ['n', 'o'] or answer== ['n']:
            answer= removeNonLetters(list(input('Please try again\n').lower()))
        else:
            answer= removeNonLetters(list(input('Huh what? can you say it again\n').lower()))
    while True:
        numberToPlay= getValidInt('How many wins do we play to?\n')
        wins= 0
        losses= 0
        ties= 0
        allRockChance= random.randint(1, 100)
        while not (wins == numberToPlay or losses == numberToPlay):
            print('Ready. Set. Throw!')
            playerPosition= getPlayerHandPosition('Your Hand Position: ')
            aiPosition= getAiHandPosition(allRockChance)
            result= whoWins(playerPosition, aiPosition)
            if result== 'Win':
                wins+= 1
            elif result== 'Lose':
                losses+= 1
            elif result== 'Tie':
                ties+= 1
            print(f'Wins:{wins:>3}   Losses:{losses:>3}   Ties:{ties:>3}')
        if wins > losses:
            print('You\'ve won the whole thing!')
        else:
            print('YAY! I\'VE WON')
        playAgain= removeNonLetters(list(input('Do you want to play Rock, Paper, Scissors again? (yes or no): ').lower()))
        while True:
            if playAgain== ['y', 'e', 's'] or playAgain== ['y']:
                again= 'Yes'
                break
            elif playAgain== ['n', 'o'] or playAgain== ['n']:
                again= 'No'
                break
            else:
                playAgain= removeNonLetters(list(input('Huh what? can you say it again?\n').lower()))
        if again== 'No':
            break
    print('Thank you for playing')
    
def getValidInt(msg):
    '''Gets a Integer above zero'''
    while True:
        try:
            validInt= int(input(msg))
            if validInt < 0:
                print('I can\'t play negative times\n')
            elif validInt == 0:
                print('You said you would play!\n')
            else:
                return validInt
        except ValueError:
            print('Sorry, I only hear numbers\n')
    

def getPlayerHandPosition(msg):
    """Takes a list of inputs and returns a string"""
    userInput= removeNonLetters(list(input(msg).lower()))
    if userInput== ['r', 'o', 'c', 'k'] or userInput== ['r']:
        position= 'Rock'
        return position
    elif userInput== ['p', 'a', 'p', 'e', 'r'] or userInput== ['p']:
        position= 'Paper'
        return position
    elif userInput== ['s', 'c', 'i', 's', 's', 'o', 'r', 's'] or userInput== ['s']:
        position= 'Scissors'
        return position
    else:
        return 'Invalid'

def removeNonLetters(word):
    """Removes non letters from a list"""
    word2= word.copy()
    for item in word2:
        item2= item.lower()
        if not 'a' <= item2 <= 'z':
            word.remove(item2)
    return word 

def getAiHandPosition(allRockChance):
    '''Code for how the AI acts'''
    if allRockChance== 100:
        return 'Rock'
    number= random.randint(1, 3)
    if number== 1:
        return 'Rock'
    elif number== 2:
        return 'Paper'
    else:
        return 'Scissors'

def whoWins(playerPosition, aiPosition):
    """Checks who wins Rock, Paper, Scissors"""
    if playerPosition== 'Rock' and aiPosition=='Rock':
        print(f'{playerPosition} vs {aiPosition}')
        print('Ohhh, a Tie')
        return 'Tie'
    elif playerPosition== 'Rock' and aiPosition=='Paper':
        print(f'{playerPosition} vs {aiPosition}')
        print('Yes! I won this round')
        return 'Lose'
    elif playerPosition== 'Rock' and aiPosition=='Scissors':
        print(f'{playerPosition} vs {aiPosition}')
        print('Oh No! You won this round')
        return 'Win'
    elif playerPosition== 'Paper' and aiPosition=='Rock':
        print(f'{playerPosition} vs {aiPosition}')
        print('Oh No! You won this round')
        return 'Win'
    elif playerPosition== 'Paper' and aiPosition=='Paper':
        print(f'{playerPosition} vs {aiPosition}')
        print('Ohhh, a Tie')
        return 'Tie'
    elif playerPosition== 'Paper' and aiPosition=='Scissors':
        print(f'{playerPosition} vs {aiPosition}')
        print('Yes! I won this round')
        return 'Lose'
    elif playerPosition== 'Scissors' and aiPosition=='Rock':
        print(f'{playerPosition} vs {aiPosition}')
        print('Yes! I won this round')
        return 'Lose'
    elif playerPosition== 'Scissors' and aiPosition=='Paper':
        print(f'{playerPosition} vs {aiPosition}')
        print('Oh No! You won this round')
        return 'Win'
    elif playerPosition== 'Scissors' and aiPosition=='Scissors':
        print(f'{playerPosition} vs {aiPosition}')
        print('Ohhh, a Tie')
        return 'Tie'
    else:
        print(f'{playerPosition} vs {aiPosition}')
        print('That isn\'t a valid move')
    

main()
        
