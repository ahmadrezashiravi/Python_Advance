people = [{'name':'ahmad','family':'shiravi','age':'25'},
         {'name':'niki','family':'mohamadi','age':'10'},
         {'name':'amirali','family':'reza','age':'9'}
         ]

family = map(lambda people:people['family'],people)
print(list(family))
