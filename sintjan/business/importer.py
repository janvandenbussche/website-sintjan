#!/usr/bin/python
# -*- coding: utf-8 -*-

# the header is to force that the file is interpreted as UTF-8
import yaml
import csv
from datetime import datetime, date, time
from google.appengine.ext import db
from sintjan.business.model import Guestbook, News, Calendar
from sintjan.business import util


'''
Delete all Guestbook entries if import failed
'''
def deleteGuestbook():
    query = Guestbook.all()
    entries = query.fetch(500)
    db.delete(entries)
    # This could bulk delete 500 entities a time
   
   
    
'''
Delete all News entries if import failed
'''    
def deleteNews():
    query = News.all()
    entries = query.fetch(500)
    db.delete(entries)



def deleteCalendar():
    query = Calendar.all()
    entries = query.fetch(500)
    db.delete(entries)


'''
    1 = datum
    2 = naam
    3 = email
    4 = place
    7 = msg
    8 = ip

    1|Woensdag 4 September 2002|Els Van Ransbeeck|Lommel||||Een pracht van een website.<br>Hiermee wil ik de maker ervan feliciteren met zijn werk.|
    1183|Zaterdag 14 november 2009 om 19:16|j.a.j|db|pijnven straat||http://www.sintjan-lommel.be/|ik siet liever bij jullie op school ( echt ik meen het)|84.195.85.109|
    24|Vrijdag 10 Oktober 2003 om 17:36|Eddy|eddy.reniers@pandora.be|Scherpenheuvel||http://tuukka.madoka.be/school/|Bedankt voor de prachtige site.<br />Dit is een voorbeeld van profesionalisme en motivatie van zowel de ontwerper als de initiatief nemer(s).<br />Dit stelt me gerust te weten dat mijn kind school loopt bij een modern en gemotiveerd team, dat openstaat voor moderne technieken.<br />Stilstaan is achteruitgaan: dit begrijpt men maar al te goed op de basisschool Sint-Jan.<br />Ik hoop dat men deze mooie instelling kan overbrengen op mijn zoon Niels.<br />Nogmaals  een gemeend Proficiat!|

'''
def importGuestbook(out, file):
    #file = open('import/data.txt')
    file = open('import/' + file)

    for line in file:
        arr = line.split("|")
        out.write(arr[1] + ", " + arr[2] + ", " + arr[3] + ", " + arr[4] + ", " + arr[7] + ", " + arr[8] + "\n");
        datetime = parseDate(out, arr[1])
        
        gb = Guestbook()
        gb.name = unicode(arr[2], errors='ignore')
        gb.canonical = unicode(arr[2], errors='ignore').lower()
        gb.email = unicode(arr[3], errors='ignore')
        gb.date = datetime
        gb.msg = unicode(arr[7], errors='ignore')
        gb.ip = unicode(arr[8])
        gb.place = unicode(arr[4], errors='ignore')
        
        gb.put()  
        #out.write(line)


    
    
'''
Woensdag 4 September 2002
Vrijdag 10 Oktober 2003 om 17:36

>>> from datetime import datetime, date, time
>>> # Using datetime.combine()
>>> d = date(2005, 7, 14)
>>> t = time(12, 30)
>>> datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)
'''       
def parseDate(out, dateStr):
    
    tmp = dateStr.split(" ")
    length = len(tmp)
    
    #Woensdag, 4, September, 2002, 
    #out.write(tmp[0] + ", " + tmp[1] + ", " + tmp[2] +  ", " + tmp[3] + ", " + "\n" )
    #out.write(str(parseMonth(tmp[2])) + ", " + tmp[2] + "\n")
      
    if length == 4:
        dt = datetime(int(tmp[3]), parseMonth(tmp[2]), int(tmp[1]))

    elif length == 6:
        tmp2 = tmp[5].split(":")
        dt = datetime(int(tmp[3]), parseMonth(tmp[2]), int(tmp[1]), int(tmp2[0]), int(tmp2[1]))

    return dt 
        

def parseMonth(month):
    
    if month.lower() == "januari":
        return 1
    elif month.lower() == "februari":
        return 2
    elif month.lower() == "maart":
        return 3
    elif month.lower() == "april":
        return 4
    elif month.lower() == "mei":
        return 5
    elif month.lower() == "juni":
        return 6
    elif month.lower() == "juli":
        return 7
    elif month.lower() == "augustus":
        return 8
    elif month.lower() == "september":
        return 9
    elif month.lower() == "oktober":
        return 10
    elif month.lower() == "november":
        return 11
    elif month.lower() == "december":
        return 12

    return -1












'''
"70";"Danny Huijsmans";"danny@sintjan-lommel.be";"Terug uit Zinal!";"2005-02-24";"<p>De zesdeklassers keerden woensdagavond 23 februari 2005 terug uit een droom die 10 dagen duurde: hun <strong>sneeuwklassen in het mooie Zwitserland.</strong><br/>Het verslag met de foto's kan bezocht worden tot de volgende sneeuwklassen.</p><p><strong>Dankjewel meester Tom en juf Lieve voor zoveel inzet en overgave!<br/>Dankjewel moni Isabelle en Veerle voor de ondersteuning!<br/>Dankjewel staff-leden Marc (co�rdinator), Geert en Andrea (hogeschool), Martin,meester Danny en de medische staff met Jos en Han:\" Man, man, man...het was SUPER!\"<br/>Dankjewel directeur en personeel van het hotel...heerlijk mooi en lekker!<br/>En dankjewel kinderen, jullie waren formidabel!!!!</strong></p>";"admin";NULL;"true"
10,Danny,danny@sintjan-lommel.be,Wij doen ook mee!,2004-01-26,<p><img src=\DSC00534.jpg\" alt=\"\" /></p>",admin,NULL,true
 389,Danny Huijsmans,danny@sintjan-lommel.be,Onze eerste werkdag in Rhode,2011-05-09,<p>Het hotel ontwaakt omstreeks 7.30 uur plaatselijke tijd. De kinderen nog niet gehoord...wakker maken, douche in en naar het ontbijt!</p><p>De meisjes waren vroeg wakker, de wekker stond<strong> op 6 uur</strong> en de jongens kwamen later uit hun pijp. Maarten is in het kleine bed gaan liggen omdat Noah<strong> alle kussen </strong>had afgepakt!</p><p>Na een <strong> stevig ontbijt</strong>  in het restaurant trokken we met het busje naar de school waar de directeur ons de naam van de school uitlegde.<br/>Daarna bezochten we het 5de en 6de leerjaar en het <strong> klikte meteen tussen de kinderen</strong> . Ze gingen zelf samen <strong> Gaelic football</strong>  spelen op de speelplaats.<br/>In de turnzaal werden de kinderen vergast op <strong> Ierse liederen, gedichtjes</strong>  en zelfs een lied gezongen door één van de kinderen die de<strong>  tweede prijs</strong>  behaalde op een zangwedstrijd voor scholen in gans Ierland.<br/>Na enkele lekkere sandwiches op school en een bezoekje aan de overige klassen reden we naar een park waar er voor kinderen een deel van de<strong>  Ierse geschiedenis</strong>  werd verteld, zagen we hoe mensen vroeger leefden en konden we van dichtbij zien hoe hier massaal <strong> turf</strong>  wordt gewonnen om elektriciteit van te maken.</p><p>Na een drankje reden we door naar een <strong> Chinees restaurant</strong>  waar de kinderen konden genieten van een berg kroepoek, een lekkere maaltijd met ribbekens of kip curry.<br/>Ze genoten er van.</p><p>Na 35 km kwamen we terug in het hotel waar we wilden gaan zwemmen maar daar waren we net te laat voor terug.</p><p>Dus speelden ze nog een gezellige kwis in de foyer van het hotel, deze eindigde op een gelijkspel!</p> <p>Dan was het tijd om een kattenwasje te doen en zalig <strong> onder de wol</strong>  te kruipen.</p>,admin,NULL,true

'''
def importNews(out):
    #file = open('import/nieuws.yml')
    #map = yaml.load(file)
    #file.close()

    csvReader = csv.reader(open('import/nieuws.csv'), delimiter=';')
    
    for entry in csvReader:
        out.write(",".join(entry) + "\n")
        
        news = News()
        colnum = 0
        
        for col in entry:
            #out.write(str(colnum) + "-" + col + ",")
            
            if colnum == 1:
                news.name = unicode(col, errors='ignore')
            elif colnum == 2:
                news.email = unicode(col, errors='ignore')
            elif colnum == 3:
                news.title = unicode(col, errors='ignore')
            elif colnum == 4:
                news.date = newsParseDate(out, col)
            elif colnum == 5:
                news.msg = unicode(col, errors='ignore')
            elif colnum == 8:
                news.visible = util.parseBool(col)
            
            colnum += 1
            
        # store it!!!
        if news.msg != "" and news.msg != None and news.name != "" and news.name != None and news.title != "" and news.title != None:
            news.put()
            
        #out.write("\n ")


def newsParseDate(out, dateStr):
    # 2004-01-26
    
    try:
        #out.write("NAMAAM = " + dateStr)
        arr = dateStr.split("-") 
        return datetime(int(arr[0]), int(arr[1]), int(arr[2]))
    except:
        return datetime(2002,1,1)
    




'''
3135,2011-08-26,NULL,Personeelsfeest 19 uur,,admin
'''
def importCalendar(out, file):
    csvReader = csv.reader(open('import/' + file), delimiter=";")
    
    for entry in csvReader:
        out.write(",".join(entry) + "\n")

        cal = Calendar()
        colnum = 0
        
        for col in entry:
            if colnum == 1:
                cal.date = newsParseDate(out, col)
            elif colnum == 3:
                cal.title = unicode(col, errors='ignore')
            elif colnum == 4:
                cal.msg = unicode(col, errors='ignore')
            
            colnum += 1
        
        if cal.date != None and cal.title != None and cal.msg != None:
            cal.put() 




