months = {
	'January': 31,
	'February': '28/29',
	'March': 31,
	'April': 30,
	'May': 31,
	'June': 30,
	'July': 31,
	'August': 31,
	'September': 30,
	'October': 31,
	'November': 30,
	'December': 31
}

class getDate:
	def get(month, year):
		days = 0
		try:
			if month == '1':
				month = 'January'
			elif month == '2':
				month = 'February'
			elif month == '3':
				month = 'March'
			elif month == '4':
				month = 'April'
			elif month == '5':
				month = 'May'
			elif month == '6':
				month = 'June'
			elif month == '7':
				month = 'July'
			elif month == '8':
				month = 'August'
			elif month == '9':
				month = 'September'
			elif month == '10':
				month = 'October'
			elif month == '11':
				month = 'November'
			elif month == '12':
				month = 'December'
		except:
			pass
		if month in months.keys():
			for key, value in months.items():
				if key == month:
					if value == '28/29':
						if int(year) % 4 == 0:
							days = 29
						else:
							days = 28
					else:
						days = value
					months_list = list(months)
					month = months_list.index(key) + 1
			return month, days, year
		else:
			return month