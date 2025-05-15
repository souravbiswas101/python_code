data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

cleaned_ages = []

for item in data_list:
    if isinstance (item, int):
        cleaned_ages.append(item)

print(cleaned_ages)