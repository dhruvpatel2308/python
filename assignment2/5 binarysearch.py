def b(li,n):
    if n not in li:
        print("not present")
    else:
        s = 0
		e = len(li)-1
		while s <= e:
    		mid = (s + e) // 2
    		if l[mid] == n:
        		print(mid)
        		break
    		elif l[mid] < n:
        		start = mid + 1
    		else:
        		end = mid - 1





l1=[1,2,2,2,2,2,4,4,4,4,5,5,5,6,7,8,9]
print(b(l1,2))