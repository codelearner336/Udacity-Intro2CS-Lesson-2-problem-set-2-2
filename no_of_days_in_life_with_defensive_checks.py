
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
    #3c) For birth year, if that was on/before Feb 28, check if it was a leap year 

# the second commit adds defenise coding at the front of the program:
    ## Defensive a) year value must not be more than 4 digits
    ## Defensive b) months value must be less than 13 and greater than  0
    ## Defensive c)  days must match daysOfMonth ie months must have correct days including edge case of feb 29 in leap years
    ## Defensive d) dates must be logical
        # Defensive d1)  - the currentdates must be ahead of the birthdates;
    ##Defensive e) birth date must be before current date   
        
# the third commit added a messge in the output and allowed user input.


def daysBetweenDates(birthyear, birthmonth, birthday, currentyear, currentmonth, today):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]





###### Defensive code section   check if dates are valid e.g June 31 is not acceptable, birth year ahead of current year, month 13, year with more than 4 digits
  
## Defensive a) year value must not be more than 4 digits. This is just a choice, not really wrong with year 10000
    
    if birthyear > 9999 or currentyear > 9999:
           return "There is an error in the value of the year you entered: a year can't be more than 4 digits long, otherwise your computer will overheat"

## Defensive b) months value must be less than 13 and greater than  0

    if currentmonth > 12 or  birthmonth > 12:
            return "There is an error in the value of the months you have used: month cant be less than 1 or greater than 12, please check"


## Defensive c)
## days must match daysOfMonth
## but also need to handle leap years having 29 days in feb
## also need to check  if both birthmonth and currentmonth  are vaild e.g. not month 13 or month 0;
        
 # reminder :  daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    n = len(daysOfMonths)
    dummyyear = birthyear
    dummyday = birthday # loop for checking two variable seperately, if birthday is a valid input then next loop checks if today is a good value 
    dummymonth = birthmonth
    force_a_loop = 0
    while force_a_loop < 2: # start loop first time to check birthday has valid input, then secodn iteration to check if today ahs valid input
        z = 0
        m = 1
        while z < n:
            
            if dummymonth == m:
                    if dummyday > daysOfMonths[z]:
                       if dummymonth ==2:   ### defensive c1) check if leap and 29th 
                            isleap =  "no"
                            check29 = "no"
                            if dummyyear % 4 == 0:          #start of code for leap year check
                                if dummyyear % 100 == 0:
                                     if dummyyear % 400 == 0:
                                        isleap="yes"
                                else:
                                    isleap = "yes"
                                
                            if isleap == "yes":            #its a leap year, so now handle up to 29 days being allowed
                                check29 =">29"    
                                if dummymonth == 2:
                                    if dummyday > 29:
                                        check29 = ">29"
                                        return "it's a leap year but you still don't have more than 29 days"
                                    else:
                                        check29 = "29orless"  
                                                               
                            if isleap=="yes":               
                               if check29 != "29orless":
                                return "The value you have entered for days is too darn high even in a leap month"
                       else:
                             return "The value you have entered for days is too darn high"
            m = m+1
            z = z+1
        force_a_loop = force_a_loop + 1
        dummyday = today
        dummymonth = currentmonth
        dummyyear = currentyear

   
# Defensive d) dates must be logical:
    # Defensive d1)  - the currentdates must be ahead of the birthdates; 

    if birthyear > currentyear:
        return "oops, birthyear cant be ahead of current year"
    if birthyear == currentyear:
        if birthmonth > currentmonth:
             return "ouch, birthmonth cant be ahead of current month!"
        else:
            if birthmonth == currentmonth:
               if birthday > today:
                    return "are you from the future - your birthday  cant be ahead of current day!"            

    # defensive d2 ..could add code to warn the user the dates are ahead, but wont pursue (see comment below) 

        #from datetime import datetime
        #now = datetime.now()
        #if currentmonth > now.month:...etc


    # Defensive d3) birthdates must not be in the future  ....will not puruse; the code started as borhtday up to today, but better to have it simply days between
        # two dates , so as long as the dates are logical , all is good.
    


#Defensive e) birth date must be before current date

    if birthyear > currentyear:
        return "There is an error in your year : you were not born in the future...or maybe you were??"
    if birthyear == currentyear:
        if birthmonth > currentmonth:
            return "your birth month -is in the future -  are you a time traveller "
    if birthyear == currentyear:
        if birthmonth == currentmonth:            
            if birthday > today:
                return " Your birhtday is in the future ...back to the future please, the space time continuum needs to be taken seriously!"
            
    


################################# end defensive code section                     

 
    
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
## 3b) is this year a leap year? then check if today is ahead of feb 29, if yes, add one to total., Need to allow that birthyear = currentyear that is not two leapyears
    if currentyear != birthyear: # dont want to add for current year and birth year, so account for leap in birth year code below
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

######  Happy birthday
    import webbrowser
    if birthmonth == currentmonth and birthday == today:
            print  " \nHappy Birthday!!!"
            webbrowser.open ("http://www.freelargeimages.com/wp-content/uploads/2014/11/Happy_Birthday_3400x2217.jpg")   
    
                                
## and the final answer is:
    
    
    total_days = (full_years) +  + (fulldays) + (addleap_for_this_year)+ (addleap_for_birthyear) + (count_of_leap_years)
    return (total_days)

## some test cases
def test():
    print '\n'      # print '\n' added for readibility in the output
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
    
def defensive():
    print '\n'
    test_cases = [(2010,4,31,2010,5,4),     # wrong number of days in birth month 
                  (2010,2,29,2012,3,28),    # feb 29th incorrect
                  (2012,1,1,2012,3,45),     # current day incorrect
                  (2013,6,30,2012,6,30),    # birthyear ahead of current year
                  (2012,9,1,2012,8,8),      #same year, birthmonmth ahear of current month
                  (1950,10,9,1950,10,8),    #birthday ahead of current day
                  (19656,4,5,1999,03,10),   #worng year format birth year  
                  (1900,1,1,19999,12,31),   #wrong year format current year
                  (2200,1,1,2300,1,1),      # future dates ok, as long as logical
                  (2011,2,28,2012,2,29),    # feb 29th ok in current year
                  (2012,2,29,2012,3,1),     #feb 29th ok in birthyear
                  (2012,1,1,2012,1,2)]      # answer = 2

    for (args) in test_cases:
        result = daysBetweenDates(*args)
        if result:
            print (args,result)
    print '\n'
       
    
defensive()
