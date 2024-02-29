###################################
#   Lous List HW Assignment
###################################

#This code was written in the Fall Semester of 2017 for the CS 1110 course at the University of Virginia

import urllib.request

def instructors(department):
    list1 = []
    if department == 'CS':
        key = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/CS')
        bytes1 = key.read()
        text = bytes1.decode('utf-8')
        rows = text.strip().split('\n')
        data = rows[:]
        for row in data:
            cells = row.split(',')
            for i in cells:
                columns = i.split('|')
                if columns[4] not in list1 and columns[4][-1] != '1':
                    list1.append(columns[4])
        list2 = sorted(list1)
        return list2
    elif department == 'ECE':
        key = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/ECE')
        bytes1 = key.read()
        text = bytes1.decode('utf-8')
        rows = text.strip().split('\n')
        data = rows[:]
        for row in data:
            cells = row.split(',')
            for i in cells:
                columns = i.split('|')
                if columns[4] not in list1 and columns[4][-1] != '1':
                    list1.append(columns[4])
        list2 = sorted(list1)
        return list2
    
print(instructors("CS"))
