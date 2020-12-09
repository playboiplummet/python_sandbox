# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create typle
fruits = ('Apples','Oranges','Grapes')
fruits2 = tuple(('Apples','Oranges','Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print (fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete typle
del fruits2
print (fruits2)

# Get length
print (len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples','Oranges','Mango'}

# Check if in set
print ('Apples' in fruits_set)

# Add duplicate
fruits_set.add('Grape')
fruits_set.add('Apples')
print (fruits_set)

# Remove from set
fruits_set.remove('Grape')
print (fruits_set)



# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)