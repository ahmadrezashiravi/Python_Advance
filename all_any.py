# for all -> all list have to True
num = [2,4,6,8,10]
print(all([x % 2 == 0 for x in num ]))


num = [2,4,6,8,10,11]
print(all([x % 2 == 0 for x in num ]))

## for any min a True   !  If all of list False return False
num = [2,4,6,8,10,11]
print(any([x % 2 == 0 for x in num ]))

num = [3,5,7,9]
print(any([x % 2 == 0 for x in num ]))


users = [{'name':'m3', 'shop':['pen']},
         {'name':'m2', 'shop':[]},
         {'name':'m1', 'shop':['pen','milk']},
         {'name':'m9', 'shop':[]}]
result = all ([len(user['shop'])==0 for user in users])
print(result)
if result == False:
   print(list(filter(lambda user:not user['shop'] , users  ))) 
   print(list(map(lambda users: users['name'] ,filter(lambda user:not user['shop'] , users  ) ) ) )
