# counts the number of times a specified word appears in a news article
def count_specific_word(str1, str2):
    #Input
    str1 = input("Enter the news article: ")
    str2 = input("Enter the word to count: ")

    # Split the article into words
    words = str1.split()
    
    # Count the occurrences of the specified word
    count = words.count(str2)

    return count

print(count_specific_word("", "")) 

