

def check_shuffled_deck(deck, half1, half2):

    ret_val = True
    index_half1 = 0
    index_half2 = 0

    for index in range(len(deck)):

        if index_half1 < len(half1) and deck[index] == half1[index_half1]:
            index_half1 = index_half1 + 1
        elif index_half2 < len(half2) and deck[index] == half2[index_half2]:
            index_half2 = index_half2 + 1
        else:
            ret_val = False


    return ret_val



shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

half1 = [1, 2, 3, 4, 6, 9]

half2 = [5, 6, 7, 8, 10]

print(check_shuffled_deck(shuffled_deck, half1, half2))
