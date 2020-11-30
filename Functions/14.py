actors = [
  {'name':'Jonny Depp', 'gender':'male','age':41},
  {'name':'Keanu Reeves', 'gender':'male','age':52},
  {'name':'Angelina Jolie', 'gender':'female','age':45} ]
print("Original list of dictionaries :")
print(actors)
sorted_actors = sorted(actors, key = lambda x: x['name'])
print("\nSorting the List of dictionaries :")
print(sorted_actors)
