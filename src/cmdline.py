import sys
import os
from .parseCSV import parse
from .makedirs import makedirs
from .getDate import getDate

commands = {
	'-h': 'help',
	'--help': 'help',
	'-v': 'version',
	'--version': 'version',
	'-o': 'output directory',
	'--output': 'output directory',
	'-c': 'path to csv file',
	'--csv': 'path to csv file',
	'-m': 'month',
	'--month': 'month',
	'-y': 'year',
	'--year': 'year',
}

version = '0.0.1'

class cmdline:
	def commands(args_list):
		if len(args_list) < 2:
			print("Available Commands Are:")
			for key, value in commands.items():
				if len(key) <= 6:
					print(f"\t{key}:\t\t{value}")
				else:
					print(f"\t{key}:\t{value}")
			sys.exit(1)
		else:
			if args_list[1] in commands.keys():
				if args_list[1] == '-h' or args_list[1] == '--help':
					print("Available Commands Are:")
					for key, value in commands.items():
						if len(key) <= 6:
							print(f"\t{key}:\t\t{value}")
						else:
							print(f"\t{key}:\t{value}")
					sys.exit(0)
				elif args_list[1] == '-v' or args_list[1] == '--version':
					print(f"Directory Maker {version}")
					sys.exit(0)
				elif args_list[1] == '-c' or args_list[1] == '--csv':
					if len(args_list) < 3:
						print("Please Provide CSV File")
						sys.exit(1)
					else:
						if os.path.isfile(args_list[2]):
							if args_list[3] == '-m' or args_list[1] == '--month':
								if len(args_list) < 5:
									print("Please Provide Month")
									sys.exit(1)
								else:
									if args_list[5] == '-y' or args_list[1] == '--year':
										if len(args_list) < 7:
											print("Please Provide Year")
											sys.exit(1)
										else:
											if args_list[7] == '-o' or args_list[1] == '--output':
												if len(args_list) < 9:
													print("Please Provide Output Directory")
													sys.exit(1)
												else:
													print(f"Creating Directories in the {args_list[8]} directory")
													csv = parse.parseCSV(args_list[2])
													date = getDate.get(args_list[4], args_list[6])
													month, days, year = date
													output = args_list[8]
													makedirs.make(output, month, days, year, csv)
						else:
							print("CSV File Not Found")
							sys.exit(1)
			else:
				print(f"Invalid Command: {args_list[1]}")
				print("Valid Commands Are:")
				for key, value in commands.items():
					if len(key) <= 6:
						print(f"\t{key}:\t\t{value}")
					else:
						print(f"\t{key}:\t{value}")
				sys.exit(1)