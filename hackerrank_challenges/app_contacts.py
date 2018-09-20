
class Partial:
    def __init__(self, isComplete):
        self.isComplete = isComplete
        self.children = dict()
        self.count = 1


def add_word(dictionary, word):
    myDict = dictionary
    for i in range(len(word)):
        char = word[i]
        isComplete = i == len(word) - 1
        if myDict is None or char not in myDict:
            myDict[char] = Partial(isComplete)
        else:
            myDict[char].count += 1
        myDict = myDict[char].children


def find(dictionary, word):
    myDict = dictionary
    for i in range(len(word)):
        char = word[i]
        if myDict is None or char not in myDict:
            return 0
        else:
            if i == len(word) - 1:
                return myDict[char].count
        myDict = myDict[char].children

    return 0



def calc_app_contacts(my_dict, op, contact):

        if op == 'add':
            add_word(my_dict, contact)
        else:
            print(find(my_dict, contact))


my_dict = dict()
calc_app_contacts(my_dict, 'add', 'hack')
calc_app_contacts(my_dict, 'add', 'hackerrank')
calc_app_contacts(my_dict, 'find', 'hac')
calc_app_contacts(my_dict, 'find', 'hak')

