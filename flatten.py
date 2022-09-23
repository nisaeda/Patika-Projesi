def flatten(n):
    new_list=[]
    for i in n:
        if type(i) is list:
            flatten(i)
        else:
            newlist.append(i)

input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten(input)
print("flatten: " ,newlist)
