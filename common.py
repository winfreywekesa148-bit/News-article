#identify the most common word
def identify_most_common_word(str):
   #split the string into words
    words = str.split()
    
    #create a dictionary to store the count of each word
    word_count = {}
    
    #iterate through the list of words
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    #find the most common word and its count
    most_common_word = max(word_count, key=word_count.get)
    count = word_count[most_common_word]
    
    return most_common_word, count
    
