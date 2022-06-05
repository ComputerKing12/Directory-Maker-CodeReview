import csv

dir1 = []
dir2 = []

class parse:
	def parseCSV(file):
		with open(file) as csvfile:
			dirs = []
			dirs2 = []
			reader = csv.DictReader(csvfile)
			for row in reader:
				dir1.append(row['Dir1'])
				dir2.append(row['Dir2'])
			for i in range(len(dir1)):
				dirs2 += [dir2[i]]
				for element in dirs2:
					if element == '':
						dirs2.remove(element)
				dirs = dirs + [dir1[i], dirs2]
			return dirs