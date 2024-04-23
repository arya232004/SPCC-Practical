def gen_temp(temp):
    return 't'+str(temp)

def gen_tac(exp):
    tokens=exp.split()
    operator_st=[]
    operand_st=[]
    temp_counter=0
    code=[]
    
    for token in tokens:
        if token in ['+','-','/','*','%']:
            operator_st.append(token)
        elif token =='(':
            operator_st.append(token)
        elif token ==')':
            while operator_st[-1]!='(':
                op=operator_st.pop()
                arg2=operand_st.pop()
                arg1=operand_st.pop()
                
                result=gen_temp(temp_counter)
                temp_counter+=1
                
                operand_st.append(result)
                code.append((op,arg1,arg2,result))
            operand_st.pop()
        else:
            operand_st.append(token)
            
    while operator_st:
        op=operator_st.pop()
        arg2=operand_st.pop()
        arg1=operand_st.pop()
        
        result=gen_temp(temp_counter)
        temp_counter+=1
        
        operand_st.append(result)
        code.append((op,arg1,arg2,result))
    
    return code
    
def display_code(code):
    for c in code:
        print(c)
              
expression='(a + b) * c - (d / e)'
display_code(gen_tac(expression))
