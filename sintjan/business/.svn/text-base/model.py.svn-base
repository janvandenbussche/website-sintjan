import util
from google.appengine.ext import db


'''
    Represents an guestbook item
    http://stackoverflow.com/questions/1658163/case-insensitive-where-clause-in-gql-query-for-stringproperty
'''
class Guestbook(db.Model):
    name = db.StringProperty(multiline=True)
    canonical = db.StringProperty(multiline=True)
    email = db.StringProperty(multiline=True)
    place = db.StringProperty(multiline=True)
    msg = db.TextProperty()
    ip = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

    def formatted(self):
        return util.strdate(self.date.year, self.date.month, self.date.day);
    
    def formatDate(self):
        return str(self.date.year) + "-" + str(self.date.month) + "-" + str(self.date.day)
    
    
class News(db.Model):
    name = db.StringProperty(multiline=True)
    email = db.StringProperty(multiline=True)
    user_id = db.StringProperty(multiline=True)
    title = db.StringProperty(multiline=True)
    msg = db.TextProperty()
    visible = db.BooleanProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    def id(self):
        try:
            return self.key().id()
        except:
            return -1
    
    def formatted(self):
        return util.strdate(self.date.year, self.date.month, self.date.day);
    
    def formatDate(self):
        return str(self.date.year) + "-" + str(self.date.month) + "-" + str(self.date.day)
    
    def path(self):
        return "/" + util.formatUrlTitle(self.title) + ".a" + str(self.key().id()) + ".html"
    

class Calendar(db.Model):
    title = db.StringProperty(multiline=True)
    msg =  db.TextProperty() 
    date = db.DateTimeProperty(auto_now_add=False)
    created = db.DateTimeProperty(auto_now_add=True)
    
    def id(self):
        try:
            return self.key().id()
        except:
            return -1

    def formatted(self):
        return util.strdate(self.date.year, self.date.month, self.date.day);
    
    def formatDate(self):
        return str(self.date.year) + "-" + str(self.date.month) + "-" + str(self.date.day)
    
    def path(self):
        return "/" + util.formatUrlTitle(self.title) + ".c" + str(self.key().id()) + ".html"   
      

class AppSetting(db.Model):
    name = db.StringProperty(multiline=False)
    value = db.StringProperty(multiline=False)

    def id(self):
        try:
            return self.key().id()
        except:
            return -1


class Page(db.Model):
    url = db.StringProperty(multiline=False)
    title = db.StringProperty(multiline=True)
    keywords = db.StringProperty(multiline=True)
    description = db.StringProperty(multiline=True)
    breadcrumb = db.TextProperty()
    content = db.TextProperty()
    template = db.StringProperty(multiline=False)
    visible = db.BooleanProperty()
    createdBy = db.StringProperty(multiline=False)
    createdOn = db.DateTimeProperty()
    updatedBy = db.StringProperty(multiline=False)
    updatedOn = db.DateTimeProperty()

    def id(self):
        try:
            return self.key().id()
        except:
            return -1


class Block(db.Model):
    name = db.StringProperty(multiline=False)
    label = db.StringProperty(multiline=False)
    content = db.StringProperty(multiline=True)

    def id(self):
        try:
            return self.key().id()
        except:
            return -1

'''
    Hello
'''
class BlockLink(db.Model):
    pageId = db.IntegerProperty()
    region = db.StringProperty(multiline=False)
    name = db.StringProperty(multiline=False)
    


    




