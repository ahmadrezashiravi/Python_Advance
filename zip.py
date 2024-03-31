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

bestscore = [max(num) for num in zip(midterm1,midterm2,midterm3)]
print(list(zip(students,bestscore)))


person ={person[0]:max(person[1],person[2],person[3]) for person in zip(students,midterm1,midterm2,midterm3)}
print(person)


personnew = zip(students, map(lambda perscore : max(perscore),zip(midterm1,midterm2,midterm3)))
print(dict(personnew))