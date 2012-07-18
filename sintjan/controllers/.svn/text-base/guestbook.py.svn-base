import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from sintjan.business.settings import RequestContext
from sintjan.business.model import Guestbook
from sintjan.business import util


#SELECT * FROM YourModel WHERE __key__ = KEY('YourModel',1)
#items = db.GqlQuery("SELECT * FROM Guestbook WHERE __key__< KEY('Guestbook',3)");
class IndexPage(webapp.RequestHandler):
    def get(self):        
        items = db.GqlQuery("SELECT * FROM Guestbook ORDER BY date DESC LIMIT 15");
        values = {'context':RequestContext(),'menuItem':'prikbord','list':items}
        self.response.out.write(template.render('templates/prikbord/index.html',values))
    
    
    
'''
Select 20 items less the the specified id

# http://code.google.com/appengine/docs/python/datastore/gqlreference.html
# http://stackoverflow.com/questions/5077765/how-to-retrieve-entity-from-key-value-in-gql
items = db.GqlQuery("SELECT * FROM Guestbook WHERE __key__< KEY('Guestbook',:id) ORDER BY __key__ DESC LIMIT 15", id=maxId);
'''    
class MorePage(webapp.RequestHandler):
    def get(self):

        try:
            arr = self.request.get('id').split('-')
            dateObj = datetime(int(arr[0]), int(arr[1]), int(arr[2]))
            
            items = db.GqlQuery("SELECT * FROM Guestbook WHERE date < :date ORDER BY date DESC LIMIT 15", date=dateObj, );
            values = {'context':RequestContext(),'menuItem':'prikbord','list':items}
            self.response.out.write(template.render('templates/prikbord/more.html',values))    
            
        except Exception, e:
            logging.exception(e)
            logging.error("Upsie on loading more")



class FilterPage(webapp.RequestHandler):
    def get(self):
        tmp = self.request.get('name')
        
        if(len(tmp)>1):
            items = db.GqlQuery("SELECT * FROM Guestbook WHERE canonical = :name ORDER BY date DESC", name=tmp.lower())
        else:
            items = []
            
        values = {'context':RequestContext(),'menuItem':'prikbord','list':items,'name':tmp}
        self.response.out.write(template.render('templates/prikbord/byname.html',values))      
            


class AddPage(webapp.RequestHandler):
    def get(self):
        values = {'context':RequestContext(),'menuItem':'prikbord'}
        self.response.out.write(template.render('templates/prikbord/add.html',values))
    
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        msg = self.request.get('msg')
        sum = util.parseint(self.request.get('sum'),-1)

        if sum == 5 and len(name)>0 and len(msg)>0:
            item = Guestbook()
            item.name = name
            item.canonical = name.lower()
            item.email = email
            item.msg = msg
            item.ip = self.request.remote_addr
            item.put()
            self.redirect('/prikbord/?status=ok', permanent=False)
            
        else:
            #values = {'context':RequestContext(),'error':True, 'debug1':sum,'debug2':name,'debug3':msg}
            values = {'context':RequestContext(),'menuItem':'prikbord','error':True,'name':name,'email':email,'msg':msg}
            self.response.out.write(template.render('templates/prikbord/add.html',values))
        
        
   
        
        
        
                
        



        
        
        