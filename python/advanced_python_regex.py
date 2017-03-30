import pandas as pd
from collections import defaultdict
import re

faculty = pd.read_csv("faculty.csv", skipinitialspace=True)
faculty['degree'] = faculty['degree'].str.replace('.','')

#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
def num_degrees(faculty):
    all_degrees = ' '.join(list(faculty['degree'])).split(' ')
    #print(all_degrees)

    count_dict = defaultdict(int)    
    for degree in all_degrees:
        count_dict[degree] += 1
    no_degrees =  len(count_dict) -1  
    print ("There are %d different degrees. ('0' is considered as not having a degree)" % no_degrees)
    return count_dict

degree_count_dict = num_degrees(faculty)
print(degree_count_dict)




#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
def num_titles(faculty):
    titles = re.findall(r'\w*\sProfessor',str(faculty['title']))

    if titles:
        title_count_dict = defaultdict(int)
        for title in titles:
            title_count_dict[title] += 1
    
    return(title_count_dict)

title_count_dict = num_titles(faculty)
print(title_count_dict)


#Q3. Search for email addresses and put them in a list. Print the list of email addresses.
#    faculty['email'] can be printed as it is but following is the method using regular expressions

def print_emails(faculty):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+',str(faculty['email']))
    if emails:
        return emails

emails_tobe_printed = print_emails(faculty)
print(emails_tobe_printed)


#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
#    Print the list of unique email domains.

def email_domains(faculty):
    domain_list = []
    email_tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)',str(faculty['email']))
    for tuple in email_tuples:
        domain_list.append(tuple[1])
    print ("There are %d unique email domains." % len(set(domain_list)))    
    return(set(domain_list))

unique_domains = email_domains(faculty)
print(unique_domains)

