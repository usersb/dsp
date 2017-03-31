import pandas as pd
from collections import OrderedDict

def create_dict(faculty):
    
    names = []
    for name in faculty['name']:
        names.append(name.split()[-1])

    faculty_df = pd.DataFrame(faculty)
    faculty_df['name'] =  names   

    mydict = {}
    for x in range(len(faculty_df)):
        currentid = faculty_df.iloc[x,0]
        degree = faculty_df.iloc[x,1]
        title = faculty_df.iloc[x,2]
        email = faculty_df.iloc[x,3]
        mydict.setdefault(currentid, [])
        mydict[currentid].append([degree, title, email])

    print(mydict)
    return mydict

#mydict.keys()[:3] does not work in python3
#print_n =  {k: mydict[k] for k in mydict.keys()[:3]}    
#print(print_n)
print_n = list(mydict.items())
print(print_n[:3])



def create_tupkey_dict(faculty):
    first_last_name = []
    for name1 in faculty['name']:
        splitname = name1.split()
        if len(splitname) == 3:
            fname = name1.split()[-3]
            lname = name1.split()[-1]
        elif len(splitname) == 2:
            fname = name1.split()[-2]
            lname = name1.split()[-1]
        fl_name = [fname, lname]
        t = tuple(fl_name)
        first_last_name.append(t)


    faculty_tup = faculty
    faculty_tup_df = pd.DataFrame(faculty_tup)
    faculty_tup_df['name'] =  first_last_name   

    tup_dict = {}
    for x in range(len(faculty_tup_df)):
        currentid = faculty_tup_df.iloc[x,0]
        degree = faculty_tup_df.iloc[x,1]
        title = faculty_tup_df.iloc[x,2]
        email = faculty_tup_df.iloc[x,3]
        tup_dict.setdefault(currentid, [])
        tup_dict[currentid].append(degree)
        tup_dict[currentid].append(title)
        tup_dict[currentid].append(email)
    
    print(tup_dict)
    return tup_dict




def order_dict_lname(faculty):
    prof_dict = create_tupkey_dict(faculty)
    ordered_prof_dict = OrderedDict(sorted(prof_dict.items(), key = lambda x: x[0][1]))
    print(ordered_prof_dict)
    return ordered_prof_dict
    
