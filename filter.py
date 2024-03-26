users = [{'name':'ahmad' , 'skill':'php'},
         {'name':'NIKI' , 'skill':'python'},
         {'name':'rez' , 'skill':''},
         {'name':'behroz' , 'skill':''}]  

## return users that miss skill
##result = filter(lambda user:len(user['skill'])==0 , users)
result = filter(lambda user:not user['skill'] , users)

print(list(result))  




## want to display just name users that miss skill
result2 = map(lambda user:user['name'],filter(lambda user:not user['skill'] , users))
print(list(result2))



#another way
result3 = [user['name'] for user in users if not user['skill']]
print(result3)