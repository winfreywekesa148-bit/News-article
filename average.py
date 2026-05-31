#calculate the average of word length
def calculate_average_word_length(str):
    #split the string into words
    words = str.split()

    if not words:
        return 0
    
    total_length = sum(len(word) for word in words)
    
    average_length = total_length / len(words) if words else 0
    
    return average_length

