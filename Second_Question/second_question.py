import pandas as pd

data = pd.read_csv("titles.csv")

def calculate_vowels(title):
	count = 0
	vowels = 'aeiouAEIOU'

	for char in title:
		if char in vowels:
			count += 1

	return count


data['Vowels'] = data.apply(lambda row: calculate_vowels(row['title']), axis=1)
print(data.head())


data.to_csv("output.csv", index = False)