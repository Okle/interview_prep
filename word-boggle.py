# Given a dictionary, a method to do lookup in dictionary and a M x N board
# where every cell has one character.
# Find all possible words that can be formed by a sequence of adjacent characters.
# Note that we can move to any of 8 adjacent characters,
# but a word should not have multiple instances of same cell.
#
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G','I','Z'},
#                        {'U','E','K'},
#                        {'Q','S','E'}};
#
# Output:  Following words of dictionary are present
#          GEEKS, QUIZ

# code

def func(words, boggle, N, M):

    res = list()
    for word in words:
        visited = [[0]*M]*N
        if findWord(word, boggle, visited, N, M):
            res.append(word)
    return res


def findWord(word, boggle, visited, N, M):

    curr_location = findFirstLetter(word[0], boggle, N, M)
    if curr_location is None:
        return False

    visited[curr_location[0]][curr_location[1]] = 1
    for i in range(1, len(word)):
        curr_location = findLetter(word[i], boggle, visited, curr_location, N, M)
        if curr_location is None:
            return False
    return True


def findFirstLetter(letter, boggle, N, M):

    i = 0
    j = 0
    while i < N:
        while j < M:
            if boggle[i][j] == letter:
                return i, j
            j += 1
        i += 1
    return


def findLetter(letter, boggle, visited, location, N, M):

    row = location[0]
    column = location[1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            r = row + i
            c = column + j
            if 0 <= r < N and 0 <= c < M:
                if visited[r][c] != 1 and boggle[r][c] == letter:
                    visited[r][c] = 1
                    return r, c


def findWord_(word, index, boggle, row, column, N, M):
    if 0 > row >= N or 0 > column >= M:
        return False
    if word[index] == boggle[row][column]:
        return True
    else:
        return False

    isLFound = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            isLFound = findWord(word, index, boggle, row, colomn, N, M)
            if isLFound:
                index += 1
                row += i
                column += j
                findWord(word, index, boggle, row, colomn, N, M)

    if index == len(word) + 1:
        return True
    else:
        return False

# A recursive function to print all words present on boggle
def findWordsUtil(strings_dict, boggle, visited , row, column, string):
    # print(str(row) + str(column))
    # print(visited)
    # Mark current cell as visited and append current character to string
    visited[row][column] = 1
    string.append(boggle[row][column])

    # If string is present in dictionary, then print it
    str1 = ''.join(string)
    if str1 in strings_dict:
        print(str1)

    # Traverse 8 adjacent cells of boggle[i][j]
    for i in range(-1, 2):
        for j in range(-1, 2):
            r = row + i
            c = column + j
            if 0 <= r < M and 0 <= c < N and visited[r][c] == 0:
                findWordsUtil(strings_dict, boggle, visited, r, c, string)

    # Erase current character from string and mark visited
    # of current cell as false
    string = string[:-1]
    visited[row][column] = 0


# Prints all words presented in dictionary
def findWords_rec(strings_dict, boggle, N, M):

    # Mark all characters as not visited
    visited = [[0 for x in range(N)] for y in range(M)]

    # Initialize current string
    string = list()

    # Consider every character and look for all words
    # starting with this character
    for i in range(M):
        for j in range(N):
            findWordsUtil(strings_dict, boggle, visited, i, j, string)


str1 = 'db bcd'
# str1 = 'b'
str2 = 'd d b f e c b c d c'
# str2 = 'b '

strings_dict = set(map(str, str1.split(' ')))
n = len(strings_dict)

N = 5
M = 2

chars_arr = list(map(str, str2.rstrip().split()))
boggle = list()
count = 1
i = 0
while count <= M:
    inner = list()
    for j in range(N):
        inner.append(chars_arr[i + j])
    boggle.append(inner)
    i += N
    count += 1

#print(*func(strings_dict, boggle, N, M))

findWords_rec(strings_dict, boggle, N, M)
