from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from sintjan.business.settings import RequestContext
from sintjan.business.model import News
from sintjan.controllers import util
import sintjan.business


class EditPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            values = {
                      'context':RequestContext(),
                      'news':self.getNewsItem(self.request)
                      }
            self.response.out.write(template.render('templates/admin/newsAdd.html',values))
          
                    
    def post(self):
        if util.checkAuth(self, False):  
            user = users.get_current_user()  
            news = self.getNewsItem(self.request)
            
            name = self.request.get('name')
            email = self.request.get('email')
            title = self.request.get('title')
            msg = self.request.get('msg')
            visible = sintjan.business.util.parseBool(self.request.get('visible'))
        
            if len(name)>0 and len(email)>0 and len(title)>0 and len(msg)>0:
                news.name = name
                news.email = email
                news.title = title
                news.msg = msg
                news.visible = visible
                news.user_id = user.user_id()
                
                # the put method creates a new entity if it is not stored yet, it will update it if it exists already
                news.put()
                self.redirect('/admin/news/all?status=ok', permanent=False)
                
            else:     
                values = {
                          'context':RequestContext(),
                          'news':news,
                          'error':True
                          }
                
                self.response.out.write(template.render('templates/admin/newsAdd.html',values))
    
    
    def getNewsItem(self,request):
        # POST id
        id = sintjan.business.util.parseint(request.get('id'),0)
        
        #GET id
        if id<1:
            id = sintjan.business.util.parseint(request.get('newsid'),0)


        if id>0:
            return News.get_by_id(id)
        else:
            user = users.get_current_user()
            news = News()
            news.name = user.nickname()
            news.email = user.email()
            news.title = ""
            news.msg = ""
            news.visible=True
            return news
            
        
    
            
            
            
            
class AllPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            items = db.GqlQuery("SELECT * FROM News ORDER BY date DESC LIMIT 40")
            values = {'context':RequestContext(),'list':items}
            self.response.out.write(template.render('templates/admin/newsAll.html',values))    
            
            
            
            
            
class MorePage(webapp.RequestHandler):       
    def get(self): 
        if util.checkAuth(self, False):
            arr = self.request.get('id').split('-')
            dateObj = datetime(int(arr[0]), int(arr[1]), int(arr[2]))
            
            items = db.GqlQuery("SELECT * FROM News WHERE date < :date ORDER BY date DESC LIMIT 40", date=dateObj)
            values = {'context':RequestContext(),'list':items}
            self.response.out.write(template.render('templates/admin/newsMore.html',values))    
            
            
            
            
            
    