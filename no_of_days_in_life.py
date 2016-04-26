
# find numebr of days that a person has lived
# don't include today.
# Algorithm:
# if you were born on Feb 10 1994 and today is April 25 2016 then:
# section 1) quickly add up all the days in complete years you have lived i.e 365 days in each of 1995 upto 2015
# section 2a) count all the days in the birth year dealing with the edge case that the birth and current dates are in the same year
# section 2b) count all the days in the current year
#section 3) leap year stuff! 
## Three concepts:
    #3a) for  all the full years that are leap years add 1.
    #3b) For current year if it is a  leap year and also after Feb 29 add 1
    #3c) For birth year, if that was on/before Feb 28, check if leap year and add 1


def daysBetweenDates(birthyear, birthmonth, birthday, currentyear, currentmonth, today):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
## section 1) calculate  complete years lived and the number of days in those years  i.e ignore bith and current years as partial years,ignore leap years for now

    if currentyear == birthyear or (currentyear - birthyear) ==1:  #edge case - same year or years
         full_years = 0
    else:
        full_years = ((currentyear-1)-(birthyear)) * 365

# section 2 full months
    
## 2a) get days in each full month in birth year plus days in birth month
    
    if currentyear == birthyear: #edge case . Same year. Method is to count all the days up to current day, and then subtract days from start of year up to birthday.
        totaldays = 0
        n = currentmonth
        z = 0
        while z < n-1:
            totaldays = totaldays +daysOfMonths[z]
            z = z+1
        fulltotaldays = totaldays + today-1 #dont count today as a full day . This total is all the days in the year up to today      
        fulldaysbeforebirthday = 0
        daysbeforebirthday = 0
        n = birthmonth
        z = 0 
        while z < n-1:
            daysbeforebirthday = daysbeforebirthday + daysOfMonths[z]
            z = z + 1
        fulldaysbeforebirthday = daysbeforebirthday + birthday-1 #this total is all the days in the year up to birthday
        fulldays = fulltotaldays - fulldaysbeforebirthday        # this total is all the days in the year minus all the days up to birthday
    else:                  #normal case - different birth year and current year
          n = birthmonth   #marchbirthmonth =3 implies P[3]+...+P[11]
          print n
          birth_month_days= daysOfMonths[n-1]-birthday
          full_months_birth_year = 0
          while n < len(daysOfMonths):   
            full_months_birth_year =full_months_birth_year + daysOfMonths[n]
            n=n+1
          fulldays = full_months_birth_year+ birth_month_days     

## 2b) get full months in current year

    if currentyear != birthyear: #if it is, do nothing as 2a already handled this
        n = currentmonth
        z=0
        currentmonthdays = today #jan 16 means 16 days
        full_months_current_year = 0
        while z < n-1: # current month = april means collect jan-march
            full_months_current_year = full_months_current_year + daysOfMonths[z]
            z=z+1
        fulldays = fulldays + currentmonthdays + full_months_current_year #adding total from section 2a

## section 3) leap year stuff! if year is divisible by 4 and then if it is divisble and 100 then it must also be divisible by 400
## Three concepts:
    #3a) for  all the full years that are leap years add 1.
    #3b) For current year if a  leap year and after Feb 29 add 1
    #3c) For your birth year, if that was on/before Feb 28, check if leap year and add 1
 
## 3a) number of leap years excluding birth and current year, there is more elegant python code if- and - or but I want to understand that more first before I use it
    count_of_leap_years = 0
    if currentyear != birthyear:
        year = birthyear + 1
        while year < currentyear:
            if year % 4 == 0:
                if year % 100 != 0:
                    count_of_leap_years = count_of_leap_years + 1 
                    year=year+1
                else:
                    if year % 400 == 0:
                        count_of_leap_years =  count_of_leap_years + 1
                        year=year+1
                    else:
                        year=year+1
            else:
                 year=year+1
## 3b) is this year a leap year? then check if today is ahead of feb 29, if yes, add one to total
    if currentyear != birthyear: # dont want to add for current year and birth year, so account for leap in birht year code below
        if currentyear % 4 == 0:
            if currentyear % 100 != 0:
                leap = "yes"
            else:
                if currentyear % 400 == 0:
                    leap =  " yes"
                else:
                    leap= "no"
        else:
             leap = "no"
         
        addleap_for_this_year = 0 
        if leap == "yes":
            if currentmonth > 2:
                addleap_for_this_year = 1
    else:
         addleap_for_this_year=0
## 3c) is birth year a leap year? then check if today is ahead of feb 29, if yes, add one to total
    
    if birthyear % 4 == 0:
        if birthyear % 100 != 0:
            leap = "yes"
        else:
            if birthyear % 400 == 0:
                leap =  "yes"
            else:
                leap= "no"
    else:
         leap = "no"
    addleap_for_birthyear = 0
    if leap == "yes":
        if birthyear == currentyear: #edge case
                if currentmonth > 2:
                    addleap_for_birthyear = 1
        if currentmonth ==2:
                if today ==29:
                    addleap_for_birthyear = 1
                else:
                    addleap_for_birthyear = 0
        else:                       #standard case
            if birthmonth == 1:
                addleap_for_birthyear = 1
            if birthmonth == 2:
                if birthday < 29:
                    addleap_for_birthyear = 1
## and the final answer is:
    
    
    total_days = (full_years) +  + (fulldays) + (addleap_for_this_year)+ (addleap_for_birthyear) + (count_of_leap_years)
    return (total_days)

## some test cases
def test():
    test_cases = [((2012,1,15,2012,2,28), 44),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1950,1,1,1999,12,31), 18261),
                  ((1965,4,5,1999,03,10), 12392),     
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed",result,answer
        else:
            print "Test with data:", args, "passed",result,answer

test()



