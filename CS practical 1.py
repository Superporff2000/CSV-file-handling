
#12th CS practical - 1

import csv
with open(b'C:\Users\Nishi Kumari\Documents\item details.txt') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',')
    print("%10s"%"EMPNO", "%35s"%"EMP NAME", "%15s"%"SALARY")
    print("=================================================================")
    for row in myreader:
        print("%10s"%row[0], "%35s"%row[1], "%15s"%row[2])
