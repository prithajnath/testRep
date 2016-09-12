def rem_dep(astring):

     my_set = set(astring)

     new_string = ""

     for i in astring:

          if i in my_set:
               new_string = new_string + i
               my_set = my_set - set(i)

     return new_string

key = "MUMPS"
print(rem_dep(key))

          
