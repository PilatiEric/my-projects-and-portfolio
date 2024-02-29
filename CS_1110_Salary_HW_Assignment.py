###################################
#   CS 1110 Salary HW Assignment
###################################

#This was written in the Fall semester of 2017 for the CS 1110 course at the University of Virginia

#This code searched through the HTML of a specific website and, with the use of regular expressions,
#found the salary, job title, and pay rank of a UVA employee by entering their name or employee number into the "name" argument.


import re
import urllib.request


def report(name):
    job = []
    pay = []
    rank = []
    job_finder = re.compile(r'Job title: (.+)<br')
    pay_finder = re.compile(r'2016 total gross pay: \$([0-9]{2,3},[0-9]{3})')
    rank_finder = re.compile(r'<tr><td>University of Virginia rank</td><td>([0-9]?,?[0-9]{1,3})')
    # convert name into format to reach url_files
    if "," in name:
        split_name = name.split(", ")
        new_name = split_name[1].lower() + "-" + split_name[0].lower()
    else:
        new_name = name.replace(" ", "-").lower()
    # open url_files page
    try:
        page = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + new_name)
        page2 = page.read().decode('utf-8').strip()
        # find the job title
        for m in job_finder.finditer(page2):
            if m not in job:
                job.append(m.group(1))
            if "&amp;" in job[0]:
                job[0] = job[0].replace('&amp;', '&')
            if "&lt;" in job[0]:
                job[0] = job[0].replace('&lt;', '<')
            if "&gt;" in job[0]:
                job[0] = job[0].replace('&gt;', '>')
        job_name = job[0]
        # find the total pay
        for m in pay_finder.finditer(page2):
            if m not in pay:
                pay.append(m.group(1))
                if "," in pay[0]:
                    pay[0] = pay[0].replace(',', '')
                    total_pay = float(pay[0])
    except:
        job_name = None
        total_pay = float(0)
    # find the pay rank
    try:
        for m in rank_finder.finditer(page2):
            if m not in rank:
                rank.append(m.group(1))
                if "," in rank[0]:
                    rank[0] = rank[0].replace(',', '')
                    school_rank = int(float(rank[0]))
                else:
                    school_rank = int(float(rank[0]))
    except:
        school_rank = int(0)
    return job_name, total_pay, school_rank

print(report('teresa sullivan'))
