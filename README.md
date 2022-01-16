While scanning a book the odd labelled pages are stored linearly in a different folder and even labelled pages are stored separately in different folder. This page files needs to be clubbed in a single folder to make the data meaningful. The folder containing all the odd as well as even pages store files randomly depending upon the file names. To make the storage of pages linear this script is used.   

Renaming scanned files:
_______________________

Prerequisite: -

The folders containing scanned files must be named as 'even' and 'odd' respectively.

Execution: -

1. Paste the script into the folder containing the 'even' and 'odd' folders.
2. Execute the script:
   -> python rename.py
3. The script will ask details regarding the book. Enter it.
4. After entering the details, the script will rename the files aligning them page wise and the files will be stored in a folder named as 'sorted_files',
