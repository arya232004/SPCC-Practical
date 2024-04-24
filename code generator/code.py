def code_gen(exp):
    operators = ['+', '-', '*', '/']
    final = ''  
    exp=exp.replace(' ','')
    for op in operators:
        if op in exp:
            op1, op2 = exp.split(op)
            if op == '+':
                final += f'Add {op1} {op2}'
            elif op == '-':
                final += f'Sub {op1} {op2}'
            elif op == '*':
                final += f'Mul {op1} {op2}'
            elif op == '/':
                final += f'Div {op1} {op2}'

    return final  

exp = 'a + b - c * d'
result = code_gen(exp)
print(result)
