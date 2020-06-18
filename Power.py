def power (n,e):
    '''this is the function for the exponenet of a number'''
    product = n
    for i in range(1,e):
        product+= n
        n=product
    return product
