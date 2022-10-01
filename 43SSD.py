from itertools import permutations

def is_substring(n):
    nstr = str(n)
    if int(nstr[7:10]) % 17 == 0 and int(nstr[6:9]) % 13 == 0 and int(nstr[5:8]) % 11 == 0 and int(nstr[4:7]) % 7 == 0 and int(nstr[3:6]) % 5 == 0 and int(nstr[2:5]) % 3 == 0 and int(nstr[1:4]) % 2 == 0:
        print(n)
        return True
    return False

def main():
    NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    combs = (list(permutations(NUMS)))
    sum = 0
    for i in combs:
        t = int("".join(list(map(str, list(i)))))
        if is_substring(t) is True:
            sum += t
    print(sum)


if __name__ == "__main__":
    main()
