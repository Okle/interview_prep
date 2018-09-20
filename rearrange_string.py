# code

string = 'ACCBA10D2EW30'

ret_string = list()

num_sum = 0
tbl = dict()

for i in range(len(string)):

    if 48 <= ord(string[i]) <= 57:
        num_sum += int(string[i])
    else:
        if string[i] in tbl.keys():
            tbl[string[i]] += 1
        else:
            tbl[string[i]] = 1

az = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
      'W', 'X', 'Y', 'Z']

for i in az:
    count = tbl.get(i)
    if count is not None:
        for j in range(count):
            ret_string.append(i)

ret_string.append(str(num_sum))
str1 = ''.join(ret_string)

print(str1)

