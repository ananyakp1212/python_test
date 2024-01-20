import re
from collections import Counter
import csv

def extract_count(file_path, comments_column, search_string):
    pattern = rf'{search_string} : \[code\]<I>(.*?)<\/I>\[/code\]'
    groupCount= Counter()
    # Open the input file in csv format and read data
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #get comments from specific column
            comments = row.get(comments_column, '').strip()
            #match the patterns of the comment
            matches = re.findall(pattern, comments)
            #update the count
            groupCount.update(matches)

    return groupCount

def outputFile(output_file_path, groupCount):
    #Results to be stored in output file
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        #Mention the headers
        outfile.write("Group name\tNumber of occurrences\n")

        # Write group names and occurrences
        for group, count in groupCount.items():
            outfile.write(f"{group}\t{count}\n")

    print("Output is been written onto the file:", output_file_path)

# Provide sample inputs as follws
input_file_path = 'input.csv'
output_file_path = 'outputGP.txt'
comments_column_name = 'Additional comments'
search_string = 'Groups'

groups_counter = extract_count(input_file_path, comments_column_name, search_string)
outputFile(output_file_path, groups_counter)
