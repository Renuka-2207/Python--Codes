# Function to read Input_Details.txt file

def readInputDetails(filePath):
	details = {}
	try:
		with open(filePath, 'r') as file:
			for line in file:
				# Split each line into key-value pairs using ':-' as delimiter
				parts = line.strip().split(':-')
				if len(parts) == 2:
					key = parts[0].strip()
					value = parts[1].strip()
					# Ensure that key and value are not empty
					if key and value:
						details[key] = value
					else:
						print("Warning!: Empty key or value found in input file.")
						if not key:
							print("Missing key in input file.")
						if not value:
							print(f"Missing value for key '{key}' in input file.")
				else:
					print(f"Error: Invalid line format in input file: '{line.strip()}'")
					return None
	except FileNotFoundError:
		print(f"Error: Input details file '{file_path}' not found.")
		return None
	except Exception as e:
		print(f"Error while reading input file: {e}")
		return None
	
	return details

