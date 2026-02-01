animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
movies_list = list(animal_movies)

movies_list.append("Dumbo")
movies_list.append("Zootopia")

animal_movies = tuple(movies_list)

print("Updated animal movies:", animal_movies)