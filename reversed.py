def reversed_list(x):
    empty_list=[]
    x = x[::-1]
    for i in x:
        if type(i) is list:
            i=i[::-1]
            empty_list.append(i)
    return empty_list
x = [[1, 2], [3, 4], [5, 6, 7]]
reversed_list(x)
        
