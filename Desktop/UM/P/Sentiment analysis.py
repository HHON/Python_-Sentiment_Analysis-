def strip_punctuation(s):
    for char in s:
        for char in punctuation_chars:
            s = s.replace(char, '')
    return(s)            

def get_neg(st):
    c = 0 
    words = st.split() 
    for word in words:
        word = strip_punctuation(word)
        if word in negative_words:
             c += 1
    
    return(c)


def get_pos(st):
    c = 0 
    words = st.split() 
    for word in words:
        word = strip_punctuation(word)
        if word in positive_words:
             c += 1
    
    return(c)


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
            
infile = open('project_twitter_data.csv','r')
outfile = open('resulting_data.csv','w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')   
# print(infile.readlines())
for lines in infile.readlines()[1:]:
    lines = lines.strip()
    #print(lines)
    words = lines.split(',')
    #print(words)
    p = get_pos(words[0])
    n = get_neg(words[0])
    net = get_pos(words[0]) - get_neg(words[0])
    row = "{},{},{},{},{}".format(words[1],words[2],p,n,net)
    #print(row)
    outfile.write(row)
    outfile.write('\n')
outfile.close()    


a = open('resulting_data.csv','r')
a.readlines()
