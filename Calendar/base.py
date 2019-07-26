for i in range(int(input("Enter the number of dates: "))):
    date,month,year = map(int,input().split())
    leap = False

    extra_days_month = [3,0,3,2,3,2,3,3,2,3,2,3]
    days_dict = {'0':'Sunday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday'}

    def leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if leap_year(year):
        leap = True

    extra_days = 0
    for i in range(year-(year%400) + 1,year):
        if leap_year(i):
            extra_days +=2
        else:
            extra_days +=1

    for i in range(0,month-1):
        if i == 1 and leap == True:
            extra_days = extra_days + extra_days_month[i] + 1
        else:
            extra_days = extra_days + extra_days_month[i]

    extra_days = extra_days + (date)%7
    extra_days = extra_days%7
    print(days_dict[str(extra_days)])
