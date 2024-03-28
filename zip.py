list1 = [1,5,6,8,9]
list2 = [5,5,6,8,2]

print(list(zip(list1,list2)))
print(dict(zip(list1,list2)))



list3 = [(5,6),(7,8),(85,96)]
print(list(zip(*list3)))


students = ['ali', 'mohammad', 'reza']
midterm1 = [80,20,90]
midterm2 = [50,10,60]
midterm3 = [85,65,47]

bestscore = [num for num in zip(midterm1,midterm2,midterm3)]
print(bestscore)