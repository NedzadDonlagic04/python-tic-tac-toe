# Importing needed modules
import os
import json

# Function used to create a json file with a boiler plate given to it
def createJSON(jsonDefault, jsonName):
    with open(jsonName, 'w') as scoreBoard:
        json.dump(jsonDefault, scoreBoard)

# Function used to get the contents of the json file
def getJSONContent(jsonName):
    content = None
    try:
        with open(jsonName, 'r') as scoreBoard:
            content = json.load(scoreBoard)
    except:
        return False
    return content

# Functions used to validate the json file
def validateJSON(keys, jsonName):
    data = getJSONContent(jsonName)

    if not data:
        return False

    dataKeys = list(data.keys())
    if len(dataKeys) != 2:
        return False
    elif dataKeys[0] != keys[0] or dataKeys[1] != keys[1]:
        return False
    return True

# Functions used to update the json file contents
def updateJSON(jsonName, content):
    with open(jsonName, 'w') as scoreBoard:
        json.dump(content, scoreBoard)

# Functions used to make to sure the json file used is valid (either by deleting it and re creating it with
# a valid boilerplate) and to then add the winning players score to the board
def updateScoreBoard(winner, outputCheck=False):
    jsonName = 'scoreBoard.json'
    jsonDefault = {
        "playerNames":[],
        "playerScore":[]
    }
    keys = list(jsonDefault.keys())

    if not os.path.exists(jsonName):
        createJSON(jsonDefault, jsonName)
    else:
        if not validateJSON(keys, jsonName):
            createJSON(jsonDefault, jsonName)

    content = getJSONContent(jsonName)

    if len(content['playerNames']) != len(content['playerScore']):
        createJSON(jsonDefault, jsonName)

    if not outputCheck:
        content = getJSONContent(jsonName)

        newPlayer = True

        for i in range(0, len(content['playerNames'])):
            if content['playerNames'][i] == winner:
                if isinstance(content['playerScore'][i], int):
                    content['playerScore'][i] += 1
                else:
                    content['playerScore'][i] = 1
                newPlayer = False
        
        if newPlayer:
            content['playerNames'].extend([winner])
            content['playerScore'].extend([1])
        
        updateJSON(jsonName, dict(content))

# Function used to sort the list of tuples
def sortContent(contentList):
    size = len(contentList)

    for i in range(0, size):
        swapped = False
        for j in range(0, size-i-1):
            if contentList[j][1] < contentList[j+1][1]:
                temp = contentList[j]
                contentList[j] = contentList[j+1]
                contentList[j+1] = temp
                swapped = True
        if not swapped:
            break

# Function used to show the scoreboard
def showScoreBoard():
    updateScoreBoard('JoJo', True)

    jsonName = 'scoreBoard.json'
    content = getJSONContent(jsonName)
    contentList = list(zip(content['playerNames'], content['playerScore']))

    sortContent(contentList)

    print('Scoreboard:')
    for i in range(0, len(contentList)):
        print(f'  {i+1}.{contentList[i][0]} \t- Wins: {contentList[i][1]}')