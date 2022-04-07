print("Hello World")
counties=['Arapahoe','Denver','Jefferson']
if counties[1]=='Denver':
    print(counties[1])
if "El Paso" in counties:
    print('El Paso is in the list of counties.')
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties and "El Paso" in counties:
    print('Arapahoe and El Paso are in the list of counties')
else:
    print('Arapahoe or El Paso is not in the list of counties')

if "Arapahoe" in counties or "El Paso" in counties:
    print('Arapahoe or El Paso is in the list of counties')
else:
    print('Arapahoe and El Paso are not in the list of counties')

x=0
while x <=5:
    print(x)
    x=x+1

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

print("--break--")

for bulbs in counties_dict:
    print(bulbs)

print("--break--")

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")

print('--break--')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print('--break--')

for county_dict in voting_data:  

     print(county_dict.values())

for dict in voting_data:
    print(f"{dict['county']} county has {dict['registered_voters']:,} registered voters")

