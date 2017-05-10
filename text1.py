#import libraries
from collections import Counter
import string
# Creating Function for word count
def w_count(f_name):
    dic1={}
    #try to catch ther errors
    try:
        if f_name =="":
            #Overwrite the file name if it is empty
            f_name = "sherlock.txt"
        #open the file
        f = open(f_name, 'r')
        #Count words
        coun = Counter()
        #readlines from file
        for sentence in f.readlines():
            #remove punctuation from text
            sentence = ' '.join(word.strip(string.punctuation) for word in sentence.split() if not word.isdigit()).lower()
            #all lines that start with “o”
            if sentence.startswith("o"):
                for word in sentence.split():
                    if word in dic1:
                        dic1[word] +=1
                    else:
                        dic1[word]=1
        #Update Counter
        coun.update(dic1)
        print(coun.most_common())
    #Catch if there is no file found
    except FileNotFoundError:
        print("Wrong input, Please enter right one!")


if __name__ == '__main__':
    file_name = input("Please enter file name!")
    w_count(file_name)
