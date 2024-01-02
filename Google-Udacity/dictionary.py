"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""
from itertools import starmap
locations = {'North America': {'USA': ['Mountain View']}}
continents = ['Asia','North America','Africa','Asia']
cities = ['Shanghai','Atlanta','Cairo','Bangalore']
countries = ['China','USA','Egypt','India']
#keep track of updated continents to avoid overwriting continents that do not priorly exist e.g Asia
updated_continents = ['North America']
for continent,country_city in list(locations.items()):
    for con,count,cit in zip(continents,countries,cities):
        if con not in updated_continents:
            locations.update({con:{count:[cit]}})
            updated_continents.append(con)
        else:
            for country,city in list(country_city.items()):
                if country == count:
                    city.append(cit) 
                else:
                    locations[con][count]=[cit]               
# print(locations) uncomment to test


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
asian_cities_and_countries = []
for continent,country_cities in locations.items():
    for country,cities in country_cities.items():
        if continent == "North America":
            american_cities = sorted(cities)
            print("1")
            for city in american_cities:
                print(city)
        elif continent == "Asia":
            asian_cities_and_countries.append((''.join(cities),country))
            asian_cities_and_countries = sorted(asian_cities_and_countries)
print("2")
print('\n'.join(starmap('{} - {}'.format,asian_cities_and_countries)))
            
