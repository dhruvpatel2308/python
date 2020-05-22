dict={"a":10,"b":20,"c":30}
print(len(dict))
for i in dict:
    print(i)
for i in dict:
    print(dict[i])
for i in dict.keys():
    print(i)
for i,v in dict.items():
    print(i,v)
for i in dict.values():
    print(i)
print(dict)
dict["d"]=40
print(dict)
dict.pop("b")
print(dict)
dict.popitem()
print(dict)