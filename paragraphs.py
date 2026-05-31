# count number paragraphs 
def count_paragraphs(str):
    # Split the string into paragraphs based on newline characters
    paragraphs = str.split('\n\n')
    
    # Count the number of paragraphs
    num_paragraphs = len(paragraphs)
    
    return num_paragraphs
