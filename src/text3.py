from collections import Counter  # Import libraries
import string


# Create a function to count words
def word_counter(file_name="sherlock.txt"):
    new_dic = {}  # New dictionary
    try:  # catch exceptions
        if file_name == "": file_name = "sherlock.txt"  # Make 'sherlock.txt' as a defult file
        file = open(file_name, 'r')  # Open file
        counter = Counter()  # Create a counter
        for lines in file:
            line = ' '.join(word.strip(string.punctuation) for word in lines.split() if
                            not word.isdigit()).lower()  # clean the text
            if line.startswith("o"):  # Get only lines start with 'o'
                for word in line.split():
                    if word in new_dic:  # Fill the dictionary
                        new_dic[word] += 1
                    else:
                        new_dic[word] = 1
        counter.update(new_dic)  # Update the counter
        for k, v in counter.most_common():
            print(k + "=" + str(v), end=", ")
            # print(counter.most_common()) #Print sorted counter
    except FileNotFoundError:  # Catch the File Not Found Error
        print("Please put the right filename and directory!")


if __name__ == '__main__':
    file_name = input("Please enter file name!")
    word_counter(file_name)
