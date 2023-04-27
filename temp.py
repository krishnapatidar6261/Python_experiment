'''
list1=[1,2,3,4,5,6,7]
#index[0,1,2,3,4,5,6]

print(list1[2])
        #start
print(list1[2:4])
         #start: stop
print(list1[0:6:2])
      #start: stop: step

list1=[1,2,3]
print(list1)
n =list1 * 2
print(n)

print(5 in list1)
print(sum(list1))
print(len(list1))
print(list1)

list1.append(12)
print(list1)
list1.insert(2,13)
print(list1)

for i in list1:
    if(i%2==0):
        print(i)

list1.append(12)
print(list1)
'''
list1=[1,2,2,3,5,5,3,4]


b=[]
for i in list1:
    if i not in b :
       b.append(i)
print(b)



