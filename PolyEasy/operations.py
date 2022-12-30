from utils import add, equalize, clean_polinomyal, divide_monomyals

def add_polinomyals(p,q):
    n = len(p)
    equalize(p,q) 
    r = []
    for i in range(n):
        r.append(p[i]+q[i]) 
    clean_polinomyal(r) 
    return r

def substract_polinomyals(p,q):
    n = len(p)
    equalize(p,q) 
    r = []
    for i in range(n):
        r.append(p[i]-q[i]) 
    clean_polinomyal(r) 
    return r

def multiply_polinomyals(p,q):
    n = len(p)
    m = len(q)
    clean_polinomyal(p) 
    clean_polinomyal(q)
    products = []
    for i in range(n):
        for j in range(m): 
            term = []
            term.append(p[i]*q[j]) 
            term.append(i+j) 
            products.append(term)
    r = []
    max_degree = (n + m)-1 
    for i in range(0,max_degree): 
        s = 0
        for j in range(len(products)):
            if products[j][1] == i: 
                s += products[j][0] 
        r.append(s) 
    return r

def divide_polinomyals(p,q):
    n = len(p)
    m = len(q)
    if m > n: 
        return [0]
    else:
        r = []
        while(n>=m): 
            x = divide_monomyals(p, q) 
            p = substract_polinomyals(p, multiply_polinomyals(x,q)) 
            r = [x[len(x)-1]] + r 
            n = len(p) 
        clean_polinomyal(r) 
        return r 

def remainder_divide_polinomyals(p,q):
    n = len(p)
    m = len(q)
    if m > n: 
        return [0]
    else:
        r = []
        while(n>=m): 
            x = divide_monomyals(p, q) 
            p = substract_polinomyals(p, multiply_polinomyals(x,q)) 
            r = [x[len(x)-1]] + r 
            n = len(p) 
        clean_polinomyal(r) 
        return p 

x = 5
print(int(5)==5)