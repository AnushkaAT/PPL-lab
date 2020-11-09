#a code showing different exceptions in python

a= 10
b=0
try:
    print(a/b)
except Exception as e:
    print("Exception is: ", e)

#LookupError- IndexError
string= "College"
l= len(string)
l+=1
try:
    print(string[l])
except Exception as e:
    print("Exception is: ", e)
    
#LookupError- KeyError
place= {"Country": "India", "State": "MH", "City": "Pune"}
try:
    loc= place["Town"]
except Exception as e:
    print("Exception is: KeyError", e)
