def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    count_s = 0
    count_k = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            # If the starting letter is a consonant, add all substrings
            count_s += len(string) - i
        else:
            # If the starting letter is a vowel, add all substrings
            count_k += len(string) - i

    if count_s > count_k:
        print('Stuart ' + str(count_s))
    elif count_s < count_k:
        print('Kevin ' + str(count_k))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)