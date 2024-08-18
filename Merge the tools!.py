def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string)//k):
        box = []
        for j in range( i*k, (i*k)+k ):
            if string[j] not in box:
                box.append(string[j])
        print(''.join(box))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)