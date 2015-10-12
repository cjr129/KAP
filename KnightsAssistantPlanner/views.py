from django.shortcuts import render
from django.http import HttpResponse
import datetime, string, calendar

# Create your views here
def index (request):
    return render(request, 'index.html')

def newsPage (request):
    return render(request, 'newspage.html')

def myHealth (request):
    return render(request, 'myHealth.html')

def CalendarNp(request):
    currentDay = datetime.date.today().strftime("%d")
    year = int(datetime.date.today().strftime("%y"))
    monthNumber = datetime.date.today().strftime("%m")
    month = getMonthProperties(monthNumber,year)[2]
    fstDayOfMonth = int(calendar.monthrange(year,int(monthNumber))[0])
    secondWkSp = 7 - fstDayOfMonth
    daysInMonth = calendar.monthrange(year,int(monthNumber))[1]
    daysInMonth = range(daysInMonth)[secondWkSp:]
    startingPoints = [secondWkSp, secondWkSp+7, secondWkSp+14, secondWkSp+21]
    endingPoints = [secondWkSp+6, secondWkSp+13, secondWkSp+20, secondWkSp+27]
    context_dictionary = {'month':month, 'year':year, 'currentDay':currentDay, 'fstDayOfMonth':range(fstDayOfMonth+1), 'daysInMonth':daysInMonth}
    context_dictionary['leftOver'] = range(secondWkSp)[1:]
    context_dictionary['startingPoints'] = startingPoints
    context_dictionary['endingPoints'] = endingPoints
    return render(request, 'calendar.html', context_dictionary)

def Calendar (request, Date):
    monthNumber = int(string.split(Date, "-")[0])
    year = int(string.split(Date, "-")[1])
    month = getMonthProperties(monthNumber,year)[2]
    fstDayOfMonth = int(calendar.monthrange(year,int(monthNumber))[0])
    secondWkSp = 7 - fstDayOfMonth
    daysInMonth = calendar.monthrange(year,int(monthNumber))[1]
    daysInMonth = range(daysInMonth)[secondWkSp:]
    startingPoints = [secondWkSp, secondWkSp+7, secondWkSp+14, secondWkSp+21]
    endingPoints = [secondWkSp+6, secondWkSp+13, secondWkSp+20, secondWkSp+27]
    context_dictionary = {'month':month, 'year':year, 'fstDayOfMonth':range(fstDayOfMonth+1), 'daysInMonth':daysInMonth}
    context_dictionary['leftOver'] = range(secondWkSp)[1:]
    context_dictionary['startingPoints'] = startingPoints
    context_dictionary['endingPoints'] = endingPoints
    return render(request, 'calendar.html', context_dictionary)

#This function outputs the 1st day of the month
#Number of days for that month and the month itself
#all of which are needed to make the
def getMonthProperties(monthNumber, year):
    if monthNumber == "1":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "January"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "2":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "Feburary"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "3":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "March"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "4":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "April"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "5":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "May"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "6":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "June"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "7":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "July"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "8":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "August"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "9":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "September"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "10":
        fstDayAndNumOfDays = calendar.monthrange(year,10)
        month = "October"
        return fstDayAndNumOfDays + (month,)

    if monthNumber == "11":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "November"
        return(fstDayAndNumOfDays, month)

    if monthNumber == "12":
        fstDayAndNumOfDays = calendar.monthrange(year,monthNumber)
        month = "December"
        return(fstDayAndNumOfDays, month)

    else:
        return "Undefined"


