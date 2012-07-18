import logging
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.dist import use_library
#use_library('django', '0.96')
use_library('django', '1.2')

from sintjan.controllers import guestbook, news, general, photos
from sintjan.controllers.admin import general as a_general, news as a_news, calendar as a_calendar, pages as a_pages, importer as a_importer



# loading the mappings
mappings = [
            ('/', news.HomePage),
            ('/news/more', news.MorePage),
            ('/home', general.RedirectHomePage),
            ('/home/', general.RedirectHomePage),
            ('/home/sitemap', general.SitemapPage),
            
            ('/fotos/', photos.IndexPage),
            
            ('/prikbord/', guestbook.IndexPage),
            ('/prikbord/more', guestbook.MorePage),
            ('/prikbord/filter', guestbook.FilterPage),
            ('/prikbord/voegtoe', guestbook.AddPage),

            ('/([^\\.]*).a([0-9]*).html', news.DetailPage),
            ('/([^\\.]*).c([0-9]*).html', news.DetailCalendarPage),

            ('/admin', a_general.AdminPage),
            ('/admin/news/edit', a_news.EditPage),
            ('/admin/news/all', a_news.AllPage),
            ('/admin/news/more', a_news.MorePage),
            ('/admin/cal/edit', a_calendar.EditPage),
            ('/admin/cal/all', a_calendar.AllPage),
            ('/admin/cal/more', a_calendar.MorePage),
            ('/admin/page/edit', a_pages.EditPage),
            ('/admin/page/all', a_pages.AllPage),

            ('/admin/import/guestbook', a_importer.ImportGuestbookPage),
            ('/admin/import/del/guestbook', a_importer.DeleteGuestbookPage),
            ('/admin/import/news', a_importer.ImportNewsPage),
            ('/admin/import/cal', a_importer.ImportCalendarPage),
            ('/admin/import/del/cal', a_importer.DeleteCalendarPage),

            ('/.*', general.CatchallPage),
            ]


# initialize the app with the mappings
application = webapp.WSGIApplication(mappings,debug=True)


# load the custom tags ...
webapp.template.register_template_library('templatetags.sj_tags')


# THE NIFTY HACK
# force to use 0.96 because 1.2 doesnt properly include subtemplates
# http://code.google.com/appengine/docs/python/tools/libraries.html#Django
#
# https://code.djangoproject.com/wiki/AutoEscaping
# http://stackoverflow.com/questions/5144138/django-include-templates-problem-from-0-96-to-1-2
# Monkey patching
try:
    # Bypass Django's safe_join for template paths since App Engine sandboxes the
    # filesystem anyway, and safe_join won't allow relative includes because
    # webapp.template always sets the template's parent directory as the "root",
    # rather than the app's real root directory.
    from django.utils import _os
    _os.safe_join = os.path.join
except ImportError:
    pass  # App is using a version of Django that doesn't use safe_join, it's OK.




def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()





