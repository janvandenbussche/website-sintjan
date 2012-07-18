import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from sintjan.business.settings import RequestContext
from sintjan.business.model import Calendar
from sintjan.controllers import util
import sintjan.business


class EditPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            values = self.getValues()
            values['item'] = self.getItem(self.request)
            self.response.out.write(template.render('templates/admin/calAdd.html',values))
              
    def post(self):
        if util.checkAuth(self, False):
            item = self.getItem(self.request)
            succeeded = False
            
            try:
                title = self.request.get('title')
                msg = self.request.get('msg')
                dateObj = datetime(int(self.request.get('year')),int(self.request.get('month')),int(self.request.get('day')))

                if len(title)>0:
                    item.title = title
                    item.msg = msg
                    item.date = dateObj
                    item.put()
                    succeeded = True
                    

            except:
                logging.error("Upsie, could not parse the date, invalid!")
                # void
                
            if not succeeded:
                values = self.getValues()
                values['item'] = item
                values['error'] = True
                self.response.out.write(template.render('templates/admin/calAdd.html',values))
            else:
                self.redirect('/admin/cal/all?status=ok', permanent=False)
                

                
    def getItem(self,request):
        # POST id
        id = sintjan.business.util.parseint(request.get('id'),0)
        
        #GET id
        if id<1:
            id = sintjan.business.util.parseint(request.get('calid'),0)

        if id>0:
            return Calendar.get_by_id(id)
        else:
            cal = Calendar()
            cal.date = datetime.now()
            cal.title = ""
            cal.msg = ""
            return cal
          
    def getValues(self):
        values = {
                  'context':RequestContext(),
                  'days':range(1,32),
                  'months':range(1,13),
                  'years':range(2004,2020)
                  }
        
        return values
 
 
 
 
 
class AllPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            items = db.GqlQuery("SELECT * FROM Calendar ORDER BY date DESC LIMIT 50")
            values = {'context':RequestContext(),'list':items}
            self.response.out.write(template.render('templates/admin/calAll.html',values))           

            
            
class MorePage(webapp.RequestHandler):       
    def get(self): 
        if util.checkAuth(self, False):
            arr = self.request.get('id').split('-')
            dateObj = datetime(int(arr[0]), int(arr[1]), int(arr[2]))
            
            items = db.GqlQuery("SELECT * FROM Calendar WHERE date < :date ORDER BY date DESC LIMIT 50", date=dateObj)
            values = {'context':RequestContext(),'list':items}
            self.response.out.write(template.render('templates/admin/calMore.html',values))    
            
            
            
            
            
            