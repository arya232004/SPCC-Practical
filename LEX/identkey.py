import re

code="""
int main(){
    int x=10;
    if (x> 5){
        return x;
    }else{
        return 0;
    }
}
"""

def lex(code):
    tokens=[]
    keywords=['int','main','return','if','else']
    reg_key=r'[a-zA-Z_][a-zA-Z0-9_]*'
    reg_ident=r'\b(?:'+'|'.join(keywords)+r')\b'
    mix_pattern=f'({reg_ident})|({reg_key})'
    
    for match in re.finditer(mix_pattern,code):
        keyword,identifier=match.groups()
        if keyword:
            tokens.append(('KEYWORD',keyword))
        elif identifier:
            tokens.append(('IDENTIFIER',identifier))
    return tokens
    
    
tokens=lex(code)
print(tokens)