import re 

def largest(words):
    word=re.findall(r'\b\w+\b',words)
    largest_word=max(word,key=len)
    return largest_word

ip='This is a sample text with several words of different lengths.'
print(largest(ip))