import time

# file name
f = "words.txt"


# Create a list from a text file (Append)
def read_file_app(file_name):
    with open(file_name, 'r') as file:
        words_list = []
        for line in file:
            words_list.append(line.rstrip('\n'))
    return words_list

# Create a list from a text file (Idiom)
def read_file_idiom(file_name):
    with open(file_name, 'r') as file:
        words_list = []
        for line in file:
            words_list += [line.rstrip('\n')]
    return words_list

# Functions performance
def time_counter(file_name):
    start_time = time.time()
    read_file_app(file_name)
    time1 = time.time() - start_time

    start_time = time.time()
    read_file_idiom(file_name)
    return time.time() - start_time, time1
# append takes more time

# Find revers pair and palindrome
def find_rev_palin(file_name):
    s1 = {i.rstrip('\n') for i in open(file_name, 'r')}
    # revers_pair = open("revers_pair.txt", 'w')
    # palindromes = open("palindromes.txt", 'w')
    counter = 0
    counter2 = 0
    for i in s1:
        if i[::-1] in s1:
            if i == i[::-1]:
                # palindromes.write(i + " - " + i[::-1] + "\n")
                counter2 += 1
            # revers_pair.write(i + " - " + i[::-1] + "\n")
            counter += 1
    # revers_pair.write(str(counter) + "\nTotal: " + str(len(s1)))
    # palindromes.write(str(counter2) + "\nTotal: " + str(len(s1)))
    return counter, counter2

total_counter=find_rev_palin(f)
print("Palindromes:",total_counter[1],"\nRevers pairs:",total_counter[0])
