from types import NoneType
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from sintjan.business.settings import RequestContext
from django.template import TemplateDoesNotExist
from sintjan.business.model import Page
from sintjan.business.model import BlockLink


class SitemapPage(webapp.RequestHandler):
    def get(self):
        values = {'context':RequestContext(),'menuItem':'home'}
        self.response.out.write(template.render('templates/home/sitemap.html',values))
  
  
class RedirectHomePage(webapp.RequestHandler):  
    def get(self):
        self.redirect("/", permanent=True)

  
class CatchallPage(webapp.RequestHandler):
    def get(self):
        
        values = {'context':RequestContext()}
        
        try:
            path = self.request.path
             
            if path.endswith('/'):
                str = "templates" + path + "index.html"
            else:
                str = "templates" + path + ".html"

            #values['debug1'] = self.request.path;
            #values['debug2'] = str;
            #values['debug1'] = arr[1]
            
            arr = path.split('/')
            values['menuItem'] = arr[1]
            self.response.out.write(template.render(str,values))
            
        except TemplateDoesNotExist:

            path = self.request.path
            values['path'] = path

            try:
                # Some hardcoding!!!
                if path == '/overons/':
                    path = '/overons/schoolmet5ks'
                elif path == '/overons/jaarthema/':
                    path = '/overons/jaarthema/2012-2013'
                elif path == '/info/':
                    path = '/info/contact'

                # Fetching the page
                page = Page.gql("WHERE url = :url", url = path)[0]

                values['page'] = page
                values['blockLeft'] = self.getBlockLinkByRegion('left', page)
                values['blockFooter'] = self.getBlockLinkByRegion('footer', page)

                if not page.breadcrumb:
                    values['breadcrumbLength'] = 0
                else:
                    values['breadcrumbLength'] = len(page.breadcrumb)

                if path.startswith('/sneeuwklassen'):
                    self.response.out.write(template.render('templates/pagesnow.html', values))
                else:
                    self.response.out.write(template.render('templates/page.html', values))
            except:
                # upsie, een vier nul vier
                # self.response.headers['Content-Type'] = 'text/html'
                #self.response.out.write(template.render('templates/info/contact.html',values))
                self.response.set_status(404)
                self.response.out.write(template.render('templates/404.html',values))

    def getBlockLinkByRegion(self, region, page):
        query = BlockLink.gql("WHERE region = :region AND pageId = :pageId", region=region, pageId=page.id())

        if query.count() > 0:
            return query[0]
        else:
            blockLink = BlockLink()
            blockLink.region = region
            blockLink.pageId = page.id()
            return blockLink


class BananaPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, banaan world ') 




