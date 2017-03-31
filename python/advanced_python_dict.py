import pandas as pd

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
