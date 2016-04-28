
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "SECRT"

my_array = []

my_array.append(list(key))

my_len = len(key)

i = 0

#print(list(repetitions("SECRET")))


#make new_letters here

for j in range(len(key)):

    letters = letters.translate(None,key[j])

print(letters)


val = 0
for i in range(len(key)):

    my_array.append(list(letters[val:val+my_len]))
    val = my_len + val

print(my_array)

my_column = []
my_string = ""

for k in range(len(key)):

    for l in range(len(my_array)):

        try:
            my_string = my_string + my_array[l][k]
        except IndexError:
            continue                    

    my_column.append(my_string)
    my_string = ""
print(my_column)

sort_string = ""

for x in my_column:
    sort_string = sort_string + x[0]
ref = sorted(list(sort_string))
print(ref)
new_column = []
for y in ref:

    for z in my_column:

        if y in z:
            new_column.append(z)

        else:
            continue



print(new_column)

comp_string = "".join(new_column)
print(comp_string)
print(len(comp_string))
