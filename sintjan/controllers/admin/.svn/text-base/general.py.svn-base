import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from sintjan.business.settings import RequestContext
from sintjan.controllers import util


class AdminPage(webapp.RequestHandler):
    def get(self):
        try:
            if util.checkAuth(self, False):
                values = {'context':RequestContext()}
                self.response.out.write(template.render('templates/admin/index.html',values))
        except:
            logging.error("shit seg")
            


        
        
        