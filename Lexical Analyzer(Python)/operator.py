import re 

code ="""
int main(){
    int x=5;
    if(x > 5){
        return x+5;
    }
    else{
        return x-5;
    }
}
"""

def operator(code):
    tokens=[]
    pattern=r'[-+*/%^&=]'
    for match in re.finditer(pattern,code):
        op=match.group()
        if op:
            tokens.append(('OPERATOR',op))
    return tokens

op=operator(code)
print(op)