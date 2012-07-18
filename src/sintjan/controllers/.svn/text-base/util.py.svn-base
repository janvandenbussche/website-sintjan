from google.appengine.ext.webapp import template
from google.appengine.api import users
from sintjan.business.settings import RequestContext
from sintjan.business import util


'''
Check if the user is authenticated and if it is from the sintjan-lommel.be domain
'''
def checkAuth(handler, redirect=False):
    
    isAdmin = util.isAdmin();
    
    if isAdmin:
        return True
                   
    if not redirect: 
        # if not admin are it doesnt match the @sintjan-lommel.be domain the access will be denied    
        # self.response.out.write("<html><body>Banaan Denied</body></html>")
        values = {'context':RequestContext()}
        handler.response.out.write(template.render('templates/admin/denied.html',values))

    else:
        handler.redirect(users.create_login_url("/admin"), permanent=False)   
        
    return False;
    
    
