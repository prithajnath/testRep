x = int(raw_input())

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rem_dep(astring):
     my_set = set(astring)
     new_string = ""
     for i in astring:
          if i in my_set:
               new_string = new_string + i
               my_set = my_set - set(i)

     return new_string

def cipherkey(key):

    key = rem_dep(key)
    my_array = []
    my_array.append(list(key))
    my_len = len(key)
    i = 0
    my_letters = letters

    for j in range(len(key)):

        my_letters = my_letters.translate(None,key[j])
    val = 0
    for i in range(len(key)):

        my_array.append(list(my_letters[val:val+my_len]))
        val = my_len + val
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
    sort_string = ""
    for x in my_column:
        sort_string = sort_string + x[0]
    ref = sorted(list(sort_string))
    new_column = []
    for y in ref:
        for z in my_column:

            if y in z:
                new_column.append(z)

            else:
                continue
    comp_string = "".join(new_column)
    return comp_string

def uncipher(key,text):

    my_string = ""
    letter_list = list(letters)
    ref = list(cipherkey(key))
    for i in text:
        my_string = my_string + letter_list[ref.index(i)]
    return my_string


for k in range(x):
    
    out_list = []
    key = raw_input()
    message = raw_input().split(" ")
    for u in message:
        out_list.append(uncipher(key,u))
    out_string = " ".join(out_list)
    print(out_string)
