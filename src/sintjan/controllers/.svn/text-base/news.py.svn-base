import logging
from datetime import datetime, date, timedelta
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from sintjan.business.settings import RequestContext
from sintjan.business.model import News, Calendar
from sintjan.business import util 


class HomePage(webapp.RequestHandler):
    def get(self):
        items = db.GqlQuery("SELECT * FROM News WHERE visible = :visible ORDER BY date DESC LIMIT 7", visible=True)
        
        try:
            firstId = items[0].id()
        except:
            firstId = -1
             
        values = {'context':RequestContext(),'menuItem':'home','list':items,'calendar':self.renderCalendar(),'firstId':firstId}
        self.response.out.write(template.render('templates/home/index.html',values))

    def renderCalendar(self):
        #items = db.GqlQuery()
        dateNow = date.today()
        weekDay = dateNow.weekday()
        dateMin = dateNow - timedelta(days=weekDay)
        dateMax = dateNow + timedelta(days=(6-weekDay))
        items = db.GqlQuery("SELECT * FROM Calendar WHERE date >= :min AND date <= :max ORDER BY date ASC", min=dateMin, max=dateMax)
        curDay = -1
             
        tmpStr = "<h1>Kalender</h1><div class=\"sjCalendar\"><ul>"  
        for item in items:
            if curDay != item.date.day:
                tmpStr += "</ul><h2>" + util.strdate(item.date.year, item.date.month, item.date.day) + "</h2><ul>"
                curDay = item.date.day
                
            if item.msg != None and item.msg != "": 
                tmpStr += "<li><a href=\"" + item.path() + "\">" + item.title + "</a></li>"
            else:
                tmpStr += "<li>" + item.title + "</li>"   
                 
        tmpStr += "</ul></div>"
        
        tmpStr += "<!-- " + dateMin.strftime("%A %d. %B %Y") + ", " + dateMax.strftime("%A %d. %B %Y") + " -->"
        return tmpStr
      



'''
Select 20 items less the the specified id
''' 
class MorePage(webapp.RequestHandler):
    def get(self):
        
        try:
            arr = self.request.get('id').split('-')
            dateObj = datetime(int(arr[0]), int(arr[1]), int(arr[2]))
           
            #items = db.GqlQuery("SELECT * FROM News WHERE __key__< KEY('News',:id) ORDER BY __key__ DESC LIMIT 7", id=maxId)  
            items = db.GqlQuery("SELECT * FROM News WHERE date < :date AND visible = :visible ORDER BY date DESC LIMIT 7", date=dateObj, visible=True)  
            values = {'context':RequestContext(),'list':items}
            self.response.out.write(template.render('templates/home/more.html',values))
        except Exception, e:
            logging.exception(e)
            logging.error("Upsie on loading more")
            #void 
     
             
class DetailPage(webapp.RequestHandler):
    def get(self, path1, path2): 
        id = util.parseint(path2, -1)
        art = News.get_by_id(id)
               
        if art:
            values = {
                      'context':RequestContext(),
                      'menuItem':'home',
                      'art':art,
                      }
            self.response.out.write(template.render('templates/home/detail.html',values))
            
        else:
            values = {'context':RequestContext()}
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html',values))
    
        
class DetailCalendarPage(webapp.RequestHandler):
    def get(self, path1, path2): 
        id = util.parseint(path2, -1)
        cal = Calendar.get_by_id(id)
               
        if cal:
            values = {
                      'context':RequestContext(),
                      'menuItem':'home',
                      'cal':cal,
                      }
            self.response.out.write(template.render('templates/home/calendar.html',values))
            
        else:
            values = {'context':RequestContext()}
            self.response.set_status(404)
            self.response.out.write(template.render('templates/404.html',values))
   
        
        
