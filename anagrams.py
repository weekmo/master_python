f = "words.txt"


# Anagrams more that at least 6
def anagram(file_name):
    s1 = {i.rstrip('\n') for i in open(file_name, 'r')}
    s2 = {"".join(sorted(i)) for i in s1}
    anagram = {}
    for i in s1:
        j = "".join(sorted(i))
        if j in s2:
            if j in anagram:
                anagram[j].append(i)
            else:
                anagram[j] = [i]
    return {k: v for k, v in anagram.items() if len(v) > 5}


# Sort anagrams depends on the length of the list
def print_sorted_anagrams(ana):
    sort = sorted(ana.values(), key=lambda x: len(x), reverse=True)
    for i in sort:
        print('\t',i)


# Bingo Ex3.c
def bingo(ana):
    sort = sorted(ana.values(), key=lambda x: len(x), reverse=True)
    for i in sort:
        if len(i[0]) == 8:
            print('\t',i)
            break

print("Anagrams:")
print_sorted_anagrams(anagram(f))
print("Bingo")
bingo(anagram(f))
