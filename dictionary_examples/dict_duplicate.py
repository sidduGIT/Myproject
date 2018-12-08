dict1={'c': 4, 'd': 1, 'h': 7, 'j': 9, 'f': 10,'i':1,'l':7,'k':4}
print("dict before removing duplicates",dict1)
dict2={}
for k,v in dict1.items():
    if v not in dict2.values():
        dict2[k]=v
print("dict after removing duplicates",dict2)

len1=print(len(dict2))

student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   }
}

#student_data = {1:'Sara',2:'David',3:'Sara',4:'Surya'}
result={}
for k,v in student_data.items():
    #print(k,v)
    if v not in result.values():
        result[k]=v
print(result)
