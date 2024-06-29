def hamming(str):
    str = str.split()
    str1 = str[0]
    str2 = str[1]
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count