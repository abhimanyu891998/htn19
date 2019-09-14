import csv
import os
import pydicom

#data.csv and all folders should be on same level as script.py
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0
    #https://realpython.com/python-csv/
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        elif line_count == 45:
            break
        else:
            case_id = row[0]
            death = row[34]
            if death = 'Dead':
                death = 1
            else:
                death = 0

            #same code as in app.py
            dicom_array = []
            for filename in os.listdir(case_id): #case_id is the foldername
                if filename.endswith(".dcm"):
                    ds = pydicom.dcmread(os.path.join(foldername, filename))     
                    dicom_array.append((ds, death)) # append tuple
            line_count += 1
