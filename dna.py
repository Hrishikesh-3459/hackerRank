import csv


def frequent(words):
    count = 0
    lis_counts = []
    i = 0
    while (i<len(reads)):
        if (reads[i:i+len(words)] == words):
            count += 1
            i += len(words)
        else:
            i += 1
            lis_counts.append(count)
            count = 0
            

    return(max(lis_counts))




filename = '/Users/hrishikesh/Downloads/small.csv'
with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)

files = '/Users/hrishikesh/Downloads/4.txt' 
with open(files) as fil:
    reads = fil.read()

k = 1
for i in data[1:]:
    if (int(i[1]) == frequent(data[0][k]) and int(i[2]) == frequent(data[0][k+1]) and int(i[3]) == frequent(data[0][k+2])):
        print(i[0])


