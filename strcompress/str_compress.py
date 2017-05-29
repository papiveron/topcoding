#!/usr/bin/python

counter = 0

#----------Test strings----------
#s = "eeeeeeeeaaaabcaaaaadexxxdddzdzzzz"
#s = "eeeeeeeeaaaabcaaaaadexxxdddzdzzzz"
#s = "eeeeeeeeaaaabcaaaaadexxxdddzdzzzz"
s = "aaaeeeeeeeeaaaadzxzzzzffffrrrr"
#s = "aaa"

def str_compress(s):
    global counter
    # print the string before compression, for debuging purpose, you can remove the statement
    print("Before compression : " + s)
    if (len(s) <= 3):
        return (s)
    (n, i, j) = (4, 0, 1)
    while (n <= len(s)):
        while (i < n and j < len(s) and s [i] == s[j] == s[n - 1]):
            i += 1
            j += 1
            if (i == n - 1 and n < len(s) and s[n - 1] == s[n]):
                n += 1
        if (i == n - 1):
            tmp = str(n - counter) + 'x' + s[i]
            s = s[0:counter] + tmp + s[n:len(s)]
            n = counter + 3
            i = n
            j = n + 1
            n += 4
        else:
            i += 1
            j += 1
            n = i + 4
        counter = i
        # show indices status, for debuging purposes, you can remove the statement
        print ("i : %d, j : %d, counter : %d, n : %d\n" % (i, j, counter, n))
    # print the string after compression, for debuging purpose, you can remove the statement
    print(s)
    return (str) 

str_compress(s)
