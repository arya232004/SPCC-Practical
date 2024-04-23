import re

code="""
int main(){
    int x=10;
    if (x>5){
        return x+5;
    }
    else{
        return x-5;
    }
}
"""

def lex(code):
    tokens=[]
    reg_op=r'[-+*/%<>=!^&]'
    
    for match in re.finditer(reg_op,code):
        op=match.group()
        
        if op:
            tokens.append(("OPERATOR",op))
            
    return tokens

token=lex(code)
print(token)