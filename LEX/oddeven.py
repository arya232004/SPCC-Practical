import re 

def lex(pattern):
    tokens = []
    number_pattern = r'[0-9]+'
    for match in re.finditer(number_pattern,pattern):
        no=match.group()
        if int(no) % 2 == 0:
            tokens.append(('EVEN',no))
        else:
            tokens.append(('ODD',no))
    
    return tokens

ip = " 12 27 45 46 69 42 7 4"
op = lex(ip)
print(op)
