import glob
import os
import re

def stringSplitByNumbers(x):
    r = re.compile('(\\d+)')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]

def ren_even():
	count = 2

	files = sorted(files, key = stringSplitByNumbers)
	if not os.path.exists("sorted_files"):
		os.mkdir("sorted_files")

	for file in files:
		new_name = "sorted_files/" + name + '_' + format(count, length) +"."+extension
		count += 2
		os.rename(file, new_name)

def ren_odd():
	count = 1
	files1 = sorted(files1, key = stringSplitByNumbers)

	if not os.path.exists("sorted_files"):
		os.mkdir("sorted_files")
	
	for file in files1:
		new_name = "sorted_files/" +  name + '_' + format(count, length) + "."+extension
		count += 2
		os.rename(file, new_name)
	
def main():
    ren_even()
    ren_odd()	
    
if __name__== "__main__":
	
	extension=str(input("Enter the extension of the scanned files: "))
	extension = extension.lower()
	files = glob.glob("even/*." + extension)
	files1 = glob.glob("odd/*." + extension)
	
	if len(files) > 1 and len(files1) > 1:
		name = str(input("Enter the name of the book: "))
		total_pages = str(input("Enter the total number of pages in the book: "))
		length = '0' + str(len(total_pages)) + 'd'
		main()
		print("Check the sorted_files folder to view the renamed files.")

	else:
		if len(files) < 1:
			print("The \'even\' folder does not contain any file with \'"+extension+"\' extension.")
		
		if len(files1) < 1:
			print("The \'odd\' folder does not contain any file with \'"+extension+"\' extension.")