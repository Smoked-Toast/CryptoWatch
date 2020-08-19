import csv

def WriteLead(data,name):
    result_file = open(name,'w')
    wr = csv.writer(result_file, lineterminator='\n')
    for item in data:
        wr.writerow(item)

def WriteLead2(data,name):
    result_file = open(name,'w')
    wr = csv.writer(result_file, lineterminator='\n')
    for item in data:
        if item != -1:
            wr.writerow(item)

def WriteLead3(list, filename):
    path = 'Leads\\' 
    with open(filename, 'a+', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list)

#Purpose: convert the CSV file to a list
def Convert(file):
    with open(file, newline='', errors='ignore') as csvfile:
        data = list(csv.reader(csvfile))
        return data

def Convert2(file):
    data = []
    with open(file) as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
        for row in reader:
            data.append(row[0])
    return data

