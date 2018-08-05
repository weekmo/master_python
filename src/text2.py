#function for cleaning the text
def text_cleaner(dirty_texts):
    text_list=[]
    for word in dirty_texts:
        # disregard the case of letters, any punctuation or whitespace
        text_list.append(''.join([letter for letter in word if letter.isalpha() or letter.isdigit()]).lower())
    #return clean text
    return "".join(text_list)
#function for distance ditermination
def edit_distance(s,t):
    #clean text
    s=text_cleaner(s)
    t=text_cleaner(t)
    #increase the text length
    s = ' ' + s
    t = ' ' + t
    d = {}
    #Getting the text length
    S = len(s)
    T = len(t)
    #filling matrix
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1
    return d[S-1, T-1]


print(edit_distance("Source code is hard to write, nevertheless Python makes it easy to read!",
                    "Sauce code was heard to writhe, nevertheleast Python makes it supercalifragilisticexpialidociousto reap!"))