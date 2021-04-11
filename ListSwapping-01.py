Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:22:44) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mylist=[1,2,3,4,5,6,7,8,9,10]
>>> i=j=0
>>> for j in range(5):
	temp=[i]
	temp=mylist[i]
	mylist.pop(i)
	mylist.append(temp)
	print(mylist)

	
1
[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
2
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
3
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
4
[5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
5
[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
>>> 