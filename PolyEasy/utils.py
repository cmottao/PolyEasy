#Operations

def add(b,c):
    for i in range(c):
        b.append(0)    
    return b

def equalize(p,q): 
    n = len(p)
    m = len(q)
    if n > m: 
        add(q,n-m)
    elif n < m: 
        add(p,m-n)

def clean_polinomyal(p):
    n = len(p)
    while(n > 1 and p[n-1] == 0): 
        p.pop()
        n -= 1
    return p

def divide_monomyals(p,q):
    n = len(p)
    m = len(q)
    if m > n:
        return [0]
    else:
        r = []
        add(r,n-m)
        r.append(p[n-1]/q[m-1]) 
        return r

#Calculate

def find_operator(expression):
    return expression[expression.find(')')+1]

def split_pol_p(expression):
    index_sep = expression.find(')')+1
    p = expression[1:index_sep-1]
    return p

def split_pol_q(expression):
    index_separator = expression.find(')')+1
    q = expression[index_separator+2:-1]
    return q

def degree(expression):
    if expression.count('x') <= 1:
        return expression.count('x')
    else:
        n = expression.find('x')
        return expression[n+2]

def encod_aux(expression, degree_exp):
    if degree_exp == 0:
        return [float(expression[:])]
    elif degree_exp == 1:
        if expression[-1] == 'x':
            return [float(expression[:-1])]+[0]
        else:
            sep = expression.find('x')
            return [float(expression[:sep])]+[float(expression[sep+1:])]
    else:
        index_sep = expression.find('^'+str(degree_exp))
        if index_sep == -1:
            return [0]+encod_aux(expression[index_sep+2:],degree_exp-1)
        else:
            return [float(expression[:index_sep-1])]+encod_aux(expression[index_sep+2:],degree_exp-1)
        
def encod(expression):
    return list(reversed(encod_aux(expression, int(degree(expression)))))

def decod(expression):
    exp_decod = ''
    for i in range(len(expression)-1,-1,-1):
        if i == 0:
            if expression[i] < 0:
                if expression[i] == int(expression[i]):
                    exp_decod += str(int(expression[i]))
                else:
                    exp_decod += str(expression[i])
            elif expression[i] > 0:
                if expression[i] == int(expression[i]):
                    exp_decod += '+'+str(int(expression[i]))
                else:
                    exp_decod += '+'+str(expression[i])
        elif i == 1:
            if expression[i] < 0:
                if expression[i] == int(expression[i]):
                    exp_decod += str(int(expression[i]))+'x'
                else:
                    exp_decod += str(expression[i])+'x' 
            elif expression[i] > 0:
                if expression[i] == int(expression[i]):
                    exp_decod += '+'+str(int(expression[i]))+'x'
                else:
                    exp_decod += '+'+str(expression[i])+'x'      
        else:
            if expression[i] < 0:
                if expression[i] == int(expression[i]):
                    exp_decod += str(int(expression[i]))+'x^'+str(i)
                else:
                    exp_decod += str(expression[i])+'x^'+str(i)           
            elif expression[i] > 0:
                if expression[i] == int(expression[i]):
                    exp_decod += '+'+str(int(expression[i]))+'x^'+str(i)  
                else:
                    exp_decod += '+'+str(expression[i])+'x^'+str(i)   
    if exp_decod[0] == '+':
        exp_decod = exp_decod[1:]                
    return exp_decod