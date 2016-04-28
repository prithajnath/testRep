import csv
with open('gitnames.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

#print your_list[1]

for i in range(len(your_list)):

    print your_list[i][3]
