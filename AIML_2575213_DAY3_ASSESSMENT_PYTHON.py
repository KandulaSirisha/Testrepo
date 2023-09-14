#!/usr/bin/env python
# coding: utf-8

# # File Handling

# # 1.Write a python function that copies a file reading and writing up to 50 characters at a time.

# In[56]:


def fun():
    file1=open('file1.txt','r')
    file2=open('file2.txt','w')
    read_write_file=file1.read(50)
    print(read_write_file)
    file2.write(read_write_file)
    file1.close()
    file2.close()  
fun()


# # 2.Print all numbers present in the text file and print the number of blank spaces in that file.

# In[51]:


file=open('file2.txt', "r")
number_count = 0
blank_space_count = 0
for line in file:
    for character in line:
        if character.isdigit():
            print(character, end=" ")
            number_count += 1
        elif character.isspace():
            blank_space_count += 1
print()
print("Number of numbers:", number_count)
print("Number of blank spaces:", blank_space_count)


# # 3.Write a function called sed that takes as arguments a pattern string,a replacement string,and two filenames;it should read the first file and write the contents into the second file(creating it if necessary).If the pattern string appears anywhere in the file,it should be replaced with the replacement string.If an error occurs while opening,reading,writing,or closing files,your problem should catch the exception,print an error message,and exit.

# In[77]:


def sed(pattern, replacement, input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        modified_content = content.replace(pattern, replacement)

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print("File processed and saved")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred")
        
pattern = "my"
replacement = "our"   
input_file = 'pattern.txt' 
output_file = 'rep.txt'
sed(pattern, replacement, input_file, output_file)


# # 4. Log File Analysis: You have a log file containing records of user activities on a website. Each line in the file represents a log entry with details like timestamp, user ID, and action performed. Your task is to analyze this log file.
# 
# a. Write Python code to read the log file and extract specific information, such as the number of unique users or the most common action.
# 
# b. How would you handle large log files efficiently without loading the entire file into memory?

# In[151]:


#a. Write Python code to read the log file and extract specific information, such as the number of unique users or the most common action.
from collections import defaultdict

# Initialize variables to store data
unique_users = set()
action_counts = defaultdict(int)
most_common_action = 0
max_action_count = 0

# Specify the path to your log file
log_file_path = "logfile.txt"

# Read the log file line by line
try:
    with open(log_file_path, 'r') as file:
        for line in file:
            # Assuming each log entry has the format: timestamp userid action
            parts = line.strip().split()
            if len(parts) == 3:
                timestamp, userid, action = parts
                unique_users.add(userid)
                action_counts[action] += 1
                if action_counts[action] > max_action_count:
                    most_common_action = action
                    max_action_count = action_counts[action]

    # Print the results
    print("Number of unique users:", len(unique_users))
    print("Most common action:", most_common_action, "with", max_action_count, "occurrences")
except FileNotFoundError:
    print(f"Log file '{log_file_path}' not found.")
except Exception as e:
    print("An error occurred:", str(e))


# In[149]:


#b. How would you handle large log files efficiently without loading the entire file into memory?
def process_large_log_file(log_file_path):
    try:
        with open('logfile.txt', 'r') as file:
            for line in file:
                # Process each line here
                # For example, you can print the line or perform some analysis
                print(line.strip())  # Print the line after removing leading/trailing whitespaces

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
log_file_path = "logfile.txt"  # Replace with the path to your log file
process_large_log_file(log_file_path)


# # 5. Text File Search and Replace: You have a text file with a large amount of text, and you want to search for specific words or phrases and replace them with new content.
# 
# a. Write Python code to search for and replace text within a text file.
# 
# b. How would you handle cases where you need to perform multiple replacements in a single pass?

# In[97]:


#a. Write Python code to search for and replace text within a text file.
def search_and_replace(file, text_or_phrase, replace_with):
    try:
        with open(file, 'r') as read_file:
            content = read_file.read()
        updated_content = content.replace(text_or_phrase, replace_with)
        with open(file, 'w') as write_file:
            write_file.write(updated_content)
        print('\nSearch and replace was completed successfully!')
        
    except FileNotFoundError:
        print('File is not found')
    except Exception as e:
        print(e,'Error')

file = 'file1.txt'
text_or_phrase = 'to'
replace_with = 'WOW'
search_and_replace(file, text_or_phrase, replace_with)


# In[98]:


#b.How would you handle cases where you need to perform multiple replacements in a single pass?
def search_and_replace(file, replacements):
    try:
        with open(file, 'r') as read_file:
            content = read_file.read()

        for search_text, replace_text in replacements:
            content = content.replace(search_text, replace_text)

        with open(file, 'w') as write_file:
            write_file.write(content)
        print('\nSearch and replace of multiple replacements in a single pass was completed successfully in', file)

    except FileNotFoundError:
        print('File is not found')
    except Exception as e:
        print('Error:', e)

file = 'file1.txt'
replacements = [('the', 'THE'),('book', 'Book'),('and', 'AND')]

search_and_replace(file, replacements)


# # 6. Write a Python script that concatenates the contents of multiple text files into a single output file. Allow the user to specify the input files and the output file.

# In[88]:


#for two files
import csv
input1=input("enter 1st file name:")
input2=input("enter 2nd file name:")
# Open the source CSV files
file1 = open(input1, 'r')
file2 = open(input2, 'r')

# Read the contents of the CSV files
csv_reader1 = csv.reader(file1)
csv_reader2 = csv.reader(file2)

# Create a new CSV file for the concatenated data
destination_file = open('concate_two_files.csv', 'w', newline='')
csv_writer = csv.writer(destination_file)

# Write the headers to the destination file
headers = next(csv_reader1)
csv_writer.writerow(headers)

# Write the rows from the first CSV file
for row in csv_reader1:
   csv_writer.writerow(row)

# Write the rows from the second CSV file
for row in csv_reader2:
   csv_writer.writerow(row)
print("concatenated")
# Close all the files
file1.close()
file2.close()
destination_file.close()


# In[96]:


#for multiple files
def concat_files(input_files, output_file):
    with open(output_file, 'w') as output_file:
        for input_file in input_files:
            with open(input_file, "r") as input_file:
                output_file.write(input_file.read())
        print('\nAll input files are concatenated and are stored in output file')
        
inp_files = []
while True:
    inp_file = input('\nEnter the input text file to concatenate or press enter if there are not any : ')
    if inp_file == '':
        break
    inp_files.append(inp_file)
output_file = input('\nEnter the output text file to store the output: ')

concat_files(inp_files, output_file)


# # 7. You are given a text file named input.txt containing a list of words, one word per line. Your task is to create a Python program that reads the contents of input.txt, processes the words, and writes the result to an output file named output.txt.
# 
# a. The program should perform the following operations:
# 
#   i. Read the words from input.txt.
#   ii. For each word in the input file, calculate the length of the word and store it in a dictionary where the word is the key,       and the length is the value.
#   iii. Write the word-length dictionary to output.txt in the following format:
#   iv. Close both input and output files properly.
#   v. Write Python code to accomplish this task. Ensure proper error handling for file operations.

# In[93]:


#i. Read the words from input.txt.
try:
   with open('input.txt','r') as input_file:
       content=input_file.read()
       print(content)
finally:
   input_file.close()


# In[147]:


#ii. For each word in the input file, calculate the length of the word and store it in a dictionary where the word is the key,
#and the length is the value.
word_length_dict = {}
try:
    with open('input.txt','r') as input_file:
        for line in input_file:
            word = line.strip() 
            word_length = len(word) 
            word_length_dict[word] = word_length 
    print('\nPrinting dict with word as key & length as value\n')
    

except FileNotFoundError:
    print('File is not found')
except Exception as e:
    print('Error:', e)


# In[144]:


#iii. Write the word-length dictionary to output.txt in the following format:
file = 'output.txt'
with open(file, 'w') as output_file:
        for word, length in word_length_dict.items():
            output_file.write('{}: {}\n'.format(word, length))
print('\nWord-length dictionary is copied to output.txt\n')


# In[141]:


#iv. Close both input and output files properly.
input_file.close()
output_file.close()


# In[148]:


#v. Write Python code to accomplish this task. Ensure proper error handling for file operations.
file = 'output.txt'
try:
    print('\nWord-length dictionary is copied to output.txt as follows:\n')
    with open(file, 'w') as output_file:
        for word, length in word_length_dict.items():
            output_file.write('{}: {}\n'.format(word, length))
    file = open('output.txt','r')        
    content = file.read()
    print(content)

except FileNotFoundError:
    print('File is not found')
except Exception as e:
    print('Error:', e)


# # 8. Assume that you are developing a student gradebook system for a school. The system should allow teachers to input student grades for various subjects, store the data in files, and provide students with the ability to view their grades.
# 
# Design a Python program that accomplishes the following tasks:
# 
# i. Teachers should be able to input grades for students in different subjects.
# 
# ii. Store the student grade data in separate text files for each subject. iii. Students should be able to view their grades for each subject.
# 
# iv. Implement error handling for file operations, such as file not found or permission issues.

# In[1]:


import os

# Function to input and store student grades for a subject
def input_grades(subject):
    try:
        file_name = f"{subject}.txt"
        with open(file_name, "a") as file:
            student_name = input("Enter student name: ")
            grade = input(f"Enter {subject} grade for {student_name}: ")
            file.write(f"{student_name}: {grade}\n")
        print(f"Grade for {student_name} in {subject} has been recorded.")
    except IOError as e:
        print(f"Error: {e}")

# Function to view student grades for a subject
def view_grades(subject):
    try:
        file_name = f"{subject}.txt"
        if not os.path.exists(file_name):
            print(f"No grades recorded for {subject} yet.")
            return

        with open(file_name, "r") as file:
            print(f"Grades for {subject}:")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Error: {e}")

# Main program loop
while True:
    print("\nStudent Gradebook System")
    print("1. Input Grades")
    print("2. View Grades")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        subject = input("Enter the subject: ")
        input_grades(subject)
    elif choice == "2":
        subject = input("Enter the subject: ")
        view_grades(subject)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("your are exited")


# In[ ]:




