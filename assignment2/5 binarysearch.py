import bisect
l1=[1,2,2,2,3,3,3,3,4,4,5,6,7,8,9]
print(bisect.bisect_left(l1,2))
print(bisect.bisect_left(l1,3,5,9))
print(bisect.bisect_right(l1,4,0,8))
print(bisect.bisect_right(l1,3))