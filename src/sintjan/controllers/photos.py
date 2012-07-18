from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from sintjan.business.settings import RequestContext

from sintjan.business import util 
from sintjan.business.model import AppSetting

import gdata.photos.service
import gdata.media
import gdata.geo



'''
Basic API Code for an album
http://code.google.com/apis/picasaweb/docs/1.0/developers_guide_python.html#ListAlbums

Fetching the album thumb
http://stackoverflow.com/questions/4597726/youtube-python-get-thumbnail

Api reference
http://gdata-python-client.googlecode.com/svn/trunk/pydocs/gdata.html
'''
class IndexPage(webapp.RequestHandler):
    def get(self):
        
        #gd_client = self.getGoogleClient()
        gd_client = self.getGoogleClientSecure()
       
        array = []
       
        albums = gd_client.GetUserFeed(user="basisschoolsintjan")
        
        for album in albums.entry:
            #http://gdata-python-client.googlecode.com/svn/trunk/pydocs/gdata.photos.html#AlbumData
            thumbnail = album.media.thumbnail[0].url
            array.append({
                          'img':thumbnail,
                          'url':album.GetHtmlLink().href,
                          'title':album.title.text,
                          'num':album.numphotos.text,
                          'caption':self.getSummie(album.summary.text),
                          'date':self.getDate(album.timestamp.datetime())
                          })
       
        values = {'context':RequestContext(),'menuItem':'fotos','items':array}
        self.response.out.write(template.render('templates/photos/index.html',values))
        
        
    def getSummie(self,text):
        if text == None:
            return "";
        else:
            return text
        
    def getDate(self,timestamp):
        return util.strdate(timestamp.year, timestamp.month, timestamp.day)
        return timestamp
    
    
    def getGoogleClient(self):
        gd_client = gdata.photos.service.PhotosService()
        gd_client.ssl = False
        return gd_client
    
    
    def getGoogleClientSecure(self):
        gd_client = gdata.photos.service.PhotosService()
        gd_client.ssl = True
        gd_client.email = self.getSettingValue('user').value
        gd_client.password = self.getSettingValue('password').value
        gd_client.source = 'exampleCo-exampleApp-1'
        gd_client.ProgrammaticLogin()
        return gd_client

    def getSettingValue(self, nameStr):
        return db.GqlQuery("SELECT * FROM AppSetting WHERE name = :name LIMIT 1", name=nameStr)[0]

