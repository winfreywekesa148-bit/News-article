#count number of sentences 
def count_sentences(str):
    # Split the string into sentences based on punctuation marks
    sentences = str.split('.')
    
    # Count the number of sentences
    num_sentences = len(sentences)
    
    return num_sentences
