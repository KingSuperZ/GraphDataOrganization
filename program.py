"""Takes an edge list and gets all combinations of nuumbers into one edge list
and it makes another list that respectively shows which values interact or not
based on the original data"""
data = [[1,3],[2,4],[3,5],[-1,1],[0,2],[-2,0]] # Original Data (Edge List)

keys = [] # Creates a list to store the keys which are every unique number in the dataset
values = [] # Creates a list to store the values for each key based on the original data

# This block of code uses X to makes the lists keys and values as follows
# keys:   [1, 3, 2, 4, 3, 5, -1, 1, 0, 2, -2, 0]
# values: [3, 1, 4, 2, 5, 3, 1, -1, 2, 0, 0, -2]
# The keys are all of the item from X in order and the values is the same thing
# except the numbers from each list in X are reversed.
for i in range(len(data)):
    keys.append(data[i][0]) # Adds the x coordinates to the keys list from before
    values.append(data[i][1])
    keys.append(data[i][1]) # Adds the y coordinates to the keys list from before
    values.append(data[i][0])

# This block of code take the values from the list keys to create a dictonary
# with the list being the keys and the values being empty lists
# posDict: {1: [], 3: [], 2: [], 4: [], 5: [], -1: [], 0: [], -2: []}
posDict = {}
for i in range(len(keys)):
    posDict[keys[i]] = []

# This block of code uses the values list and adds to the dictionary posDict by
# adding the values to each key depending on the interactions listed in X
# posDict: {1: [3, -1], 3: [1, 5], 2: [4, 0], 4: [2], 5: [3], -1: [1], 0: [2, -2], -2: [0]}
for i in range(len(values)):
    posDict[keys[i]].append(values[i])
print(posDict)

# This block of code uses the list posDict to subtract all of the included value
# from all of the existing values so that every combination of keys and values will
# be included except for the ones in posDict
# negDict: {1: [0, 1, 2, 4, 5, -2], 3: [0, 2, 3, 4, -1, -2], 2: [1, 2, 3, 5, -1, -2], 4: [0, 1, 3, 4, 5, -2, -1], 5: [0, 1, 2, 4, 5, -2, -1], -1: [0, 2, 3, 4, 5, -2, -1], 0: [0, 1, 3, 4, 5, -1], -2: [1, 2, 3, 4, 5, -2, -1]}
negDict = posDict.copy()
dict_keys = list(posDict.keys())
for i in negDict:
    negDict[dict_keys[i]] = list(set(dict_keys)-set(negDict[dict_keys[i]]))
print(negDict)        

# This code block converts the dictionary posDict to a list of lists that contain
# the different interactions
posList = []
dict_keys = posDict.keys()
for key in posDict:
    for value in posDict[key]:
        tempList = [key,value]
        posList.append(tempList)

# This code block converts the dictionary negDict to a list of lists that contain
# the values that don't interact
negList = []
dict_keys = negDict.keys()
for key in negDict:
    for value in negDict[key]:
        tempList = [key,value]
        negList.append(tempList)

# This code block makes a list the contains a mix of the two lists posList and negList
X = []
for i in posList:
    X.append(i)
for i in negList:
    X.append(i)
print(X)

# This code block makes a list containing zeros that allign with the list X to
# show whether a certain set a of values interact or not.
zeros = [0]*len(negList)
ones = [1]*len(posList)
y = []
for i in ones:
    y.append(i)
for i in zeros:
    y.append(i)
print(y)
