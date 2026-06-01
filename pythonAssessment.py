# counts the number of times a specified word appears in a news article
def count_specific_word(str1, str2):

    #Input
    str1 = input("Enter the news article: ")
    str2 = input("Enter the word to count: ")

    # Split the article into words
    words = str1.split()

    if not words:
        return 0
    
    # Count the occurrences of the specified word
    count = words.count(str2)

    return count

print(count_specific_word("", "")) 

    
#identify the most common word
def identify_most_common_word(str):

    #Input
    str = input("Enter the news article: ")

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

print(identify_most_common_word(""))


#calculate the average of word length
def calculate_average_word_length(str):
    #Input
    str = input("Enter the news article: ")

    #split the string into words
    words = str.split()

    if len(words) == 0:
        return 0
    
    #calculate the total length of all words
    total_length = sum(len(word) for word in words)
    
    #calculate the average word length
    average_length = total_length / len(words) if words else 0
    
    return average_length

print(calculate_average_word_length(f"The average word length is: {calculate_average_word_length('')}"))


# count number paragraphs 
def count_paragraphs(str):
    #input
    str = input("Enter the news article: ")

    # Split the string into paragraphs based on newline characters
    paragraphs = str.split('\n\n')
    
    # Count the number of paragraphs
    num_paragraphs = len(paragraphs)
    
    return num_paragraphs

print(count_paragraphs(""))


#count number of sentences 
def count_sentences(str):
    #input
    str = input("Enter the news article: ")

    # Split the string into sentences based on punctuation marks
    sentences = str.split('.')
    
    # Count the number of sentences
    num_sentences = len(sentences)
    
    return num_sentences

print(count_sentences("")) 

