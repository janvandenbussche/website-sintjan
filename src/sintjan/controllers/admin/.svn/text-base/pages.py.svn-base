from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from sintjan.business.settings import RequestContext
from sintjan.business.model import Page, BlockLink
from sintjan.controllers import util
import sintjan.business


class EditPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            page = self.getPageItem(self.request)

            values = {
                'context':RequestContext(),
                'page': page,
                'blockLeft': self.getBlockLinkByRegion('left', page),
                'blockFooter': self.getBlockLinkByRegion('footer', page)
            }

            self.response.out.write(template.render('templates/admin/pageEdit.html', values))

    def post(self):
        if util.checkAuth(self, False):
            page = self.getPageItem(self.request)
            
            page.url = self.request.get('url')
            page.title = self.request.get('title')
            page.content = self.request.get('content')
            page.breadcrumb = self.request.get('breadcrumb')

            if len(page.url)>0 and len(page.title)>0:
                page.put()

                # Creating the left block
                name = self.request.get('blockLeft')

                if len(name)>0:
                    blockLink = self.getBlockLinkByRegion('left', page)
                    blockLink.name = self.request.get('blockLeft')
                    blockLink.put()

                # Creating the footer block
                name = self.request.get('blockFooter')

                if len(name)>0:
                    blockLink = self.getBlockLinkByRegion('footer', page)
                    blockLink.name = self.request.get('blockFooter')
                    blockLink.put()

                self.redirect('/admin/page/all?status=ok', permanent=False)

            else:
                values = {
                    'context':RequestContext(),
                    'page':page,
                    'blockLeft': self.getBlockLinkByRegion('left', page),
                    'blockFooter': self.getBlockLinkByRegion('footer', page),
                    'error':True
                }

                self.response.out.write(template.render('templates/admin/pageEdit.html',values))

    def getPageItem(self, request):
        # POST id
        id = sintjan.business.util.parseint(request.get('id'),0)

        #GET id
        if id<1:
            id = sintjan.business.util.parseint(request.get('pageid'),0)

        if id>0:
            page = Page.get_by_id(id)
        else:
            user = users.get_current_user()

            page = Page()
            page.createdOn = datetime.now()
            page.createdBy = user.user_id()
            page.url = request.get('path')
            page.title = ""
            page.content = ""
            page.breadcrumb = ""
            page.visible = True

        if not page.breadcrumb:
            page.breadcrumb = ""

        return page

    def getBlockLinkByRegion(self, region, page):
        query = BlockLink.gql("WHERE region = :region AND pageId = :pageId", region=region, pageId=page.id())

        if query.count()>0:
            return query[0]
        else:
            blockLink = BlockLink()
            blockLink.region = region
            blockLink.pageId = page.id()
            return blockLink


class AllPage(webapp.RequestHandler):
    def get(self):
        if util.checkAuth(self, False):
            items = db.GqlQuery("SELECT * FROM Page ORDER BY url ASC LIMIT 40")
            values = {'context':RequestContext(),'list':items, 'request':self.request}
            self.response.out.write(template.render('templates/admin/pageAll.html',values))


