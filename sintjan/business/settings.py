import random 
import util
from google.appengine.api import users
from datetime import date

#########################################################
# A random Header for CSS #
#########################################################
headers = ["hoofding.jpg", "hoofding1.jpg","hoofding2.jpg","hoofding3.jpg","hoofding4.jpg","hoofding5.jpg","hoofding6.jpg"]


# object definition of Settings
class RequestContext():
    # analytics = False
    analytics = True
    url = 'http://www.sintjan-lommel.be'
    # url = 'http://sintjanlommel.appspot.com'
    mail_website = 'maarten@sintjan-lommel.be'
    mail_contact = 'contact@sintjan-lommel.be'
    
    def header(self):
        return "/s/img/headers/" + headers[random.randint(0, 6)]
        
    def now(self):
        today = date.today()
        return util.strdate(today.year, today.month, today.day)
    
    def axenroos(self):
        return axenroosHtml()
    
    def logout(self):
        return users.create_logout_url("/")
    
    def login(self):
        return users.create_login_url("/admin")
    
    def authOk(self):
        return util.isAdmin()
    
    def user(self):
        return users.get_current_user()
    
    def contact(self):
        return "contact@sintjan-lommel.be"

#########################################################
# Axenroos
#########################################################

# A list of months, base on their month it an appropriate value will be in the array
# axenroosConfig = []
# axenroosConfig = ["","Leeuw", "Bever","Kameel","Uil","Schildpad","Steenbok","","","Wasbeer","Pauw","Poes","Havik"];
# axenroosConfig = ["","Havik", "Poes","Wasbeer","Steenbok","Kameel","Pauw","","","Bever","Uil","Leeuw","Schildpad"];
axenroosConfig = ["", "Poes", "Kameel", "Uil", "Pauw", "Schildpad", "Wasbeer", "", "",
                  "Leeuw", "Bever", "Steenbok", "Havik"]

# Pointers to the images
axenroosArr = {
    "Leeuw":"leeuw.gif", 
    "Kameel":"kameel.gif", 
    "Bever":"bever.gif", 
    "Poes":"poes.gif", 
    "Pauw":"pauw.gif", 
    "Wasbeer":"wasbeer.gif", 
    "Uil":"uil.gif", 
    "Schildpad":"schildpad.gif", 
    "Havik":"havik.gif", 
    "Steenbok":"steenbok.gif",           
}


def axenroosHtml():
    month = date.today().month
    obj = axenroosConfig[month]
    
    if obj != "":
        photo = "/s/img/axenroos/" + axenroosArr[obj]
        link = "/overons/axenroos/" + obj.lower()
        naam = obj
        return "<a class=\"axenroos\" href=\"" + link + "\"><img src=\"" + photo + "\" alt=\"" + naam + "\" width=\"50\" /></a><p class=\"ax\"><a href=\"" + link + "\">" + naam + "</a>"

    else:
        return "<p class=\"ax\">Het is vakantie</p>"

    


