grammar={
    'S':['Sx','A'],
    'A':['xA','s']
}

def left(grammar):
    non_terminal=list(grammar.keys())
    
    for n in non_terminal:
        alph_prod=[]
        beta_prd=[]
        prod=grammar[n]
        
        for p in prod:
            if p.startswith(n):
                alph_prod.append(p[1:])
            else:
                beta_prd.append(p)
        
        if len(alph_prod) == 0:
            continue 
        
        new_non_terminal=n+"'"
        grammar[n]=[]
        grammar[n]=[beta+new_non_terminal for beta in beta_prd]
        grammar[new_non_terminal]=[alph+new_non_terminal if alph!='' else 'ε' for alph in alph_prod]+['ε']
        
    return grammar
        

op=left(grammar)
print(op)