from google.appengine.ext import webapp
# http://monmonja.com/blog/2008/09/templatetags-on-app-engine/

def mail(str):
    tmp = str;
    
    tmp = tmp.replace("a","&#97;")
    tmp = tmp.replace("b","&#98;")
    tmp = tmp.replace("c","&#99;")
    tmp = tmp.replace("d","&#100;")
    tmp = tmp.replace("e","&#101;")
    tmp = tmp.replace("f","&#102;")
    tmp = tmp.replace("g","&#103;")
    tmp = tmp.replace("h","&#104;")
    tmp = tmp.replace("i","&#105;")
    tmp = tmp.replace("j","&#106;")
    tmp = tmp.replace("k","&#107;")
    tmp = tmp.replace("l","&#108;")
    tmp = tmp.replace("m","&#109;")
    tmp = tmp.replace("n","&#110;")
    tmp = tmp.replace("o","&#111;")
    tmp = tmp.replace("p","&#112;")
    tmp = tmp.replace("q","&#113;")
    tmp = tmp.replace("r","&#114;")
    tmp = tmp.replace("s","&#115;")
    tmp = tmp.replace("t","&#116;")
    tmp = tmp.replace("u","&#117;")
    tmp = tmp.replace("v","&#118;")
    tmp = tmp.replace("w","&#119;")
    tmp = tmp.replace("x","&#120;")
    tmp = tmp.replace("y","&#121;")
    tmp = tmp.replace("z","&#122;")

    '''
    tmp = tmp.replace("A","&#65;")
    tmp = tmp.replace("B","&#66;")
    tmp = tmp.replace("C","&#67;")
    tmp = tmp.replace("D","&#68;")
    tmp = tmp.replace("E","&#69;")
    tmp = tmp.replace("F","&#70;")
    tmp = tmp.replace("G","&#71;")
    tmp = tmp.replace("H","&#72;")
    tmp = tmp.replace("I","&#73;")
    tmp = tmp.replace("J","&#74;")
    tmp = tmp.replace("K","&#75;")
    tmp = tmp.replace("L","&#76;")
    tmp = tmp.replace("M","&#77;")
    tmp = tmp.replace("N","&#78;")
    tmp = tmp.replace("O","&#79;")
    tmp = tmp.replace("P","&#80;")
    tmp = tmp.replace("Q","&#81;")
    tmp = tmp.replace("R","&#82;")
    tmp = tmp.replace("S","&#83;")
    tmp = tmp.replace("T","&#84;")
    tmp = tmp.replace("U","&#85;")
    tmp = tmp.replace("V","&#86;")
    tmp = tmp.replace("W","&#87;")
    tmp = tmp.replace("X","&#88;")
    tmp = tmp.replace("Y","&#89;")
    tmp = tmp.replace("Z","&#90;")
    '''
    
    tmp = tmp.replace("@","&#64;")
    tmp = tmp.replace(".","&#46;")
    tmp = tmp.replace("_","&#95;")
        
    return tmp


def foo(str):
    return "bar = " + str


register = webapp.template.create_template_register()
#register.simple_tag(mailtt)
register.filter("mail", mail)

