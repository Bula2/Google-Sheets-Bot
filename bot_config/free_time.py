from Drive_API import Color_of_Greed, Check_Date

def Date(date, k):

    b=Check_Date(date)
    if b==None:
        return(False)
    list1=b[0]
    list1+="!"
    day=b[1]

    time_list = ["8:00!", "8:30!", "9:00!", "9:30!", "10:00!", "10:30!", "11:00!", "11:30!", "12:00!", "12:30!", "13:00!", "13:30!",
                 "14:00!", "14:30!", "15:00!", "15:30!", "16:00!", "16:30!", "17:00!", "17:30!", "18:00!", "18:30!", "19:00!",
                 "19:30!", "20:00!", "20:30!", "21:00!", "21:30!", "22:00!", "22:30!", "23:00!", "23:30!"]

    mon_bask = "B4:B35"

    mon_foot = "C4:C35"

    tu_bask = "D4:D35"

    tu_foot = "E4:E35"

    wen_bask = "F4:F35"

    wen_foot = "G4:G35"

    thur_bask = "H4:H35"

    thur_foot = "I4:I35"

    fr_bask = "J4:J35"

    fr_foot = "K4:K35"

    sat_bask = "L4:L35"

    sat_foot = "M4:M35"

    sun_bask = "N4:N35"

    sun_foot = "O4:O35"

    list_of_free_time = []

    if day == "понедельник":
        if k == 1:
            a = Color_of_Greed(list1+mon_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+mon_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "вторник":
        if k == 1:
            a = Color_of_Greed(list1+tu_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+tu_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "среда":
        if k == 1:
            a = Color_of_Greed(list1+wen_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+wen_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "четверг":
        if k == 1:
            a = Color_of_Greed(list1+thur_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+thur_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "пятница":
        if k == 1:
            a = Color_of_Greed(list1+fr_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+fr_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "суббота":
        if k == 1:
            a = Color_of_Greed(list1+sat_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+sat_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
    if day == "воскресенье":
        if k == 1:
            a = Color_of_Greed(list1+sun_bask)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])
        elif k == 0:
            a = Color_of_Greed(list1+sun_foot)
            for i in range(len(a)):
                if a[i] == True:
                    list_of_free_time.append(time_list[i])

    return (list_of_free_time)

