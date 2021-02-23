password_legnth = int(input('How long would you like your password to be?'))
nLower = int(input(' How many lowercase?'))
nUpper = int(input('How many upper case?'))
nDigits = int(input('How many digits?'))
nSpecial = int(1)
password_count = (nLower + nUpper + nDigits + nSpecial)
if password_count != password_legnth:
    print('password_length and password_count do not match up, try again')
else:
    import random
    Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y','z']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    special = ['!','@','#','$','%','*','=','!']
    Uppercase_slice = Uppercase[0:27]
    Lowercase_slice = Lowercase[0:27]
    digits_slice = digits[0:10]
    special_slice = special[0:7]
    def pick_some(n,s):
        dunes = (random.sample(s,n))
        return dunes


    myt = [pick_some(nLower,Lowercase),  pick_some(nUpper, Uppercase) , pick_some(nDigits, digits) , pick_some
        (1, special)]

    def putTogether(my_list):
        listo= []

        for u in range(len(myt)):
            for i in range(len(myt[u])):
                listo.append(myt[u][i])
        string = ""
        string += "".join(listo)
        shuffle(string)
        return string


    def shuffle(puzzle):
        cube = ""
        for i in range(len(puzzle)):
            y = random.randrange(len(puzzle))
            cube = cube + puzzle[y]
            puzzle = puzzle[:y] +puzzle[y+1:]
        return cube


    final_result = putTogether(myt)
    final_list = [shuffle (final_result)]

    while len(final_list) < 4:
        if final_result not in final_list:
            final_list.append(shuffle(final_result))

    for e in final_list:
        print(e)













