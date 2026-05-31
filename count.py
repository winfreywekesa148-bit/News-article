# counts the number of times a specified word appears in a news article
def count_word_in_article(article, word):
        
    # Split the article into words
    words = article.split()
    
    # Count the occurrences of the specified word
    count = words.count(word)

    return count
    
