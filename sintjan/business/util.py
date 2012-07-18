from datetime import date
from google.appengine.api import users


def parseint(value, fallback=-1):
    try:
        return int(value)
    except:
        return fallback
    
    
def parseBool(theStr):
    return theStr[0].upper() == "T"


# Convenient method to show a date in dutch    
def strdate(year,month,day):
    # reconstruct the date
    tmp = date(year,month, day);
    days = ["Maandag","Dinsdag", "Woensdag", "Donderdag","Vrijdag", "Zaterdag","Zondag"]
    months = ["januari", "februari","maart", "april", "mei","juni", "juli", "augustus", "september","oktober", "november", "december"]
    return strday(tmp.isoweekday()) + " " + str(day) + " " + strmonth(month) + " " + str(year);   


def strday(isoweekday):
    days = ["Maandag","Dinsdag", "Woensdag", "Donderdag","Vrijdag", "Zaterdag","Zondag"]    
    return days[isoweekday-1]


def strmonth(month):
    months = ["januari", "februari","maart", "april", "mei","juni", "juli", "augustus", "september","oktober", "november", "december"]
    return months[month-1]


def isAdmin():
    user = users.get_current_user();
    
    if user: 
        arr = user.email().split("@");
                          
        if len(arr) == 2 and arr[1] == "sintjan-lommel.be":
            return True
        elif user.email() == "maarten.huijsmans@gmail.com":
            return True
        elif user.email() == "test@example.com":
            return True


def formatUrlTitle(title):
    tmp = title
    tmp = tmp.replace('/','')
    tmp = tmp.replace('"','')
    tmp = tmp.replace("'",'')
    tmp = tmp.replace('.','-')
    tmp = tmp.replace(' ',"-")
    tmp = tmp.replace('!','')
    tmp = tmp.replace(',','')
    return tmp
    
    
def foobar():
    return "Foobar"


