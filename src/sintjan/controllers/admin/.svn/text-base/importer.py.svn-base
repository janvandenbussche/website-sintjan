from google.appengine.ext import webapp
from sintjan.business import importer 

  
class ImportGuestbookPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        self.response.out.write('Start importing guestbook\n') 
        importer.importGuestbook(self.response.out, self.request.get('file'))


class DeleteGuestbookPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        self.response.out.write('Deleted 500 guestbook items\n') 
        importer.deleteGuestbook()
        

class ImportNewsPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        self.response.out.write('Start importing news\n') 
        importer.importNews(self.response.out)
        #importer.deleteNews()
        
        
class ImportCalendarPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        self.response.out.write('Start importing calendar\n') 
        importer.importCalendar(self.response.out, self.request.get('file'))


class DeleteCalendarPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        self.response.out.write('Deleted 500 calendar items\n') 
        importer.deleteCalendar()





