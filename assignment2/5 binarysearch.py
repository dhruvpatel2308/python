def b(li,n):
    if n not in li:
        print("not present")
    else:
        return li.index(n)





l1=[1,2,2,2,2,2,4,4,4,4,5,5,5,6,7,8,9]
print(b(l1,2))