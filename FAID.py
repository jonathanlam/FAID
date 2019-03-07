def nextDay(date):
    """
    Takes a date of the format dd/mm
    and returns the date of the day after
    in the format of a string "dd/mm".
    This does not take into account leap years,
    as the dates do not contain years.
    This is used when a worker is working night shift
    and their shift goes into the next day.
    """
    date = date.split("/")
    day = int(date[0])
    month = int(date[1])
    new_month = month

    if month in [9, 4, 6, 11]:
        if day == 30:
            tmr_day = 1
            new_month += 1
        else:
            tmr_day = day+1
    elif month == 2:
        if day == 28:
            tmr_day = 1
            new_month += 1
        else:
            tmr_day = day+1
    else:
        if day == 31:
            tmr_day = 1
            new_month += 1
        else:
            tmr_day = day+1

    if month == 12 and day == 31:
        new_month = 1
        tmr_day = 1

    tmr = ("%d/%d" % (tmr_day, new_month))
    return tmr

def time_to_dic(shift_raw, date, name, id):
    start_time = shift_raw.split("-")[0]
    end_time = shift_raw.split("-")[1]
    if end_time > start_time:
        shift = {"id": id, "name": name, "date_start": date, "time_start": start_time, "date_end": date, "time_end": end_time}
    else:
        shift = {"id": id, "name": name, "date_start": date, "time_start": start_time, "date_end": nextDay(date), "time_end": end_time}
    return shift

def process_line(line, id):
    line = line.split(",")

    id = len(results) + 1
    name = ''.join([i for i in line[10] if not i.isdigit()]).strip()
    worker = []

    for i in range(1,8): #1 to 7 inclusive
        if re.match(r"[0-9]{4}-[0-9]{4}", line[i]):
            worker.append(time_to_dic(line[i], dates[i-1], name, id))

    return worker


def toMonth (num):
    dic = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun",
           "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
    return dic[num]

def formatShift(shift):
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    year = datetime.datetime.now().year
    ds = shift["date_start"].split("/")
    de = shift["date_end"].split("/")
    st = shift["time_start"]
    et = shift["time_end"]
    answer = str(shift["name"]) + ","
    format_start = str(ds[0]) + " " + months[int(ds[1])-1] + " " + str(year) + " " +  st[0:2] + ":" + st[2:4]
    format_end = de[0] + " " + months[int(de[1])-1] + " " + str(year)   + " " +  et[0:2] + ":" + et[2:4]
    return answer + format_start + ",0," + format_start + ","+ format_end + ",0," + format_end + ",Full,0,Moderate\n"

import re
import datetime


input_file=open("roster_input.csv","r")
results = []

# Move down the file until you reach the dates row
a = input_file.readline()
while ("Qualification" not in a):
    a = input_file.readline()

# Build a list of dates
a = a.split(",")
dates = []
for item in a:
    if re.match(r"[a-zA-Z]{3} [0-9]+\/[0-9]+", item):
        item = item.split(" ")
        dates.append(item[1])

line = input_file.readline()

i = 1
##############
while ("Qualification" not in line):
    if not line:
        break
    if bool(re.search(r"[0-9]{4}-[0-9]{4}", line)):
        if "Assist" in line:
            i+=1
        else:
            worker_data = process_line(line, i)
            i+=1
            #print(worker_data)
            results.extend(worker_data)
    line = input_file.readline()


output_file = open("Clyde.rtq","a")
for shift in results:
    formatted = formatShift(shift)
    output_file.write(str(formatted))

##################
line = input_file.readline()
results = [] # results
while ("Qualification" not in line):
    if not line:
        break
    if bool(re.search(r"[0-9]{4}-[0-9]{4}", line)):
        if "Assist" in line:
            i+=1
        else:
            worker_data = process_line(line, i)
            i+=1
            #print(worker_data)
            results.extend(worker_data)
    line = input_file.readline()


output_file = open("CBD.rtq","a")
for shift in results:
    formatted = formatShift(shift)
    output_file.write(str(formatted))

##################
line = input_file.readline()
results = [] # results
while ("Qualification" not in line):
    if not line:
        break
    if bool(re.search(r"[0-9]{4}-[0-9]{4}", line)):
        if "Assist" in line:
            i+=1
        else:
            worker_data = process_line(line, i)
            i+=1
            #print(worker_data)
            results.extend(worker_data)
    line = input_file.readline()


output_file = open("Hornsby.rtq","a")
for shift in results:
    formatted = formatShift(shift)
    output_file.write(str(formatted))


##################
line = input_file.readline()
results = [] # results
while ("Qualification" not in line):
    if not line:
        break
    if bool(re.search(r"[0-9]{4}-[0-9]{4}", line)):
        if "Assist" in line:
            i+=1
        else:
            worker_data = process_line(line, i)
            i+=1
            #print(worker_data)
            results.extend(worker_data)
    line = input_file.readline()


output_file = open("Blacktown.rtq","a")
for shift in results:
    formatted = formatShift(shift)
    output_file.write(str(formatted))

##################
line = input_file.readline()
results = [] # results
while ("Qualification" not in line):
    if not line:
        break
    if bool(re.search(r"[0-9]{4}-[0-9]{4}", line)):
        if "Assist" in line:
            i+=1
        else:
            worker_data = process_line(line, i)
            i+=1
            #print(worker_data)
            results.extend(worker_data)
    line = input_file.readline()


output_file = open("Glenfield.rtq","a")
for shift in results:
    formatted = formatShift(shift)
    output_file.write(str(formatted))