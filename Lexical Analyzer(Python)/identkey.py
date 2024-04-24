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
    reg_id=r'[a-zA-Z_][a-zA-Z0-9_]*'
    key=['return','int','main','else','if']
    reg_key=r'\b(?:'+'|'.join(key)+r')\b'
    mix_pattern=f'({reg_key})|({reg_id})'
    
    for match in re.finditer(mix_pattern,code):
        k,id=match.groups()
        if k:
            tokens.append(('keyword',k))
        else:
            tokens.append(('Identifier',id))
    return tokens
    
    
tokens=lex(code)
print(tokens)