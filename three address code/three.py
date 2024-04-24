def gen_token(id):
    return 't'+str(id)

def three(code):
    li=code.split()
    operand_st=[]
    operator_st=[]
    count=0
    code=[]
    
    for token in li:
        if token in ['+','-','*','/','^']:
            operator_st.append(token)
        elif token == '(':
            operator_st.append(token)
        elif token == ')':
            while operator_st[-1]!='(':
                op=operator_st.pop()
                arg2=operand_st.pop()
                arg1=operand_st.pop()
                
                result=gen_token(count)
                count+=1
                operand_st.append(result)
                code.append((op,arg2,arg1,result))
                
            operator_st.pop()
        else:
            operand_st.append(token)
    
    while operator_st:
        op=operator_st.pop()
        arg2=operand_st.pop()
        arg1=operand_st.pop()
        
        result=gen_token(count)
        count+=1
        
        operand_st.append(result)
        code.append((op,arg2,arg1,result))
    
    return code 

def display(code):
    for c in code:
        print(c)


exp='(a + b) * c (d - e)' 
print(display(three(exp)))               