import os

class makedirs:
	def make(out, month, days, year, folders):
		day = 0
		path = os.path.abspath(os.path.join(os.curdir, out))
		days = int(days)
		first = []
		while int(day) < days:
			day = int(day)
			day += 1
			if day < 10:
				day = '0' + str(day)
			else:
				day = str(day)
			full_path = f"{path}/{month}.{day}.{year}"
			for i in range(len(folders)):
				if isinstance(folders[i], list):
					second = folders[i]
				else:
					first += [folders[i]]
			for i in range(len(first)):
				for j in range(len(second)):
					full_path = f"{full_path}/{first[i]}/{second[j]}"
					if not os.path.exists(full_path):
						os.makedirs(full_path)
					full_path = f"{path}/{month}.{day}.{year}"
			first = []