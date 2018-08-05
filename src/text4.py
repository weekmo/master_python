def clean_text(text): #create a Function to clean texts
    new_text=[] #New Array
    for word in text:
        new_text.append(''.join([letter for letter in word if letter.isalpha() or letter.isdigit()]).lower()) #Clean text
    return "".join(new_text) #Join and return text
def edit_distance(text1,text2): #create a Function to edit distance between texts
    text1 = clean_text(text1) #Clean Text using clean_text() Function
    text2 = clean_text(text2) #Clean Text using clean_text() Function
    matrix = {} #create new Dictionary
    text1_length = len(text1)+1 #Get text length +1
    text2_length = len(text2)+1 #Get text length  +1
    for i in range(text1_length):
        matrix[i, 0] = i #Fill the first direction of Dictionary
    for j in range(text2_length):
        matrix[0, j] = j #Fill the second direction of Dictionary

    for j in range(1,text2_length):
        for i in range(1,text1_length):
            if text1[i-1] == text2[j-1]:
                matrix[i, j] = matrix[i-1, j-1] #Fill the dictionary as a matrix
            else:
                matrix[i, j] = min(matrix[i-1, j], matrix[i, j-1], matrix[i-1, j-1]) + 1

    return matrix[text1_length-1, text2_length-1] # Return the result


print(edit_distance("Source code is hard to write, nevertheless Python makes it easy to read!",
         "Sauce code was heard to writhe, nevertheleast Python makes it supercalifragilisticexpialidociousto reap!"))