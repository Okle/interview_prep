# code

def uncode_str(string):
    num_stack = list()
    char_stack = list()
    start = 0
    while start < len(string):

        if string[start].isdigit():
            count = int(string[start])
            if string[start + 1].isdigit():
                start += 1
                count = count * 10 + int(string[start])

            num_stack.append(count)
        elif string[start] == '[':
            char_stack.append(string[start])
        elif string[start].isalpha():
            char_stack.append(string[start])
        else:

            p = ''
            char = char_stack.pop()
            while char != '[':
                p = char + p
                char = char_stack.pop()

            count = num_stack.pop()
            p = p * count
            char_stack.append(p)

        start += 1

    return char_stack



decoded_string = "1[b]"
decoded_string = "3[a2[b]]"

print(*uncode_str(decoded_string))



