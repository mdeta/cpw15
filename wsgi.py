#@+leo-ver=5-thin
#@+node:2015.20141215184040.1815: * @file wsgi.py
#@@language python
#@@tabwidth -4

#@+<<decorations>>
#@+node:2015.20141215184040.1816: ** <<decorations>>
import cherrypy
import os
#@-<<decorations>>

#@+<<secretNumber>>
#@+node:2015.20141215184040.1817: ** <<secretNumber>>
secretNumber = '123'
#@-<<secretNumber>>

#@+others
#@+node:2015.20141215184040.1818: ** class Guess
class Guess(object):
    #@+others
    #@+node:2015.20141215184040.1819: *3* def index
    @cherrypy.expose
    def index(self):
        return "welcome"
    #@+node:2015.20141215184040.1820: *3* def form
    @cherrypy.expose
    def form(self):
        return """
        <form action="check">
        <input type="text" value="enter password" name="password">
        <input type="submit" value="Send">
        </form>
        """
    #@+node:2015.20141215184040.1821: *3* def check
    @cherrypy.expose
    def check(self, password):
        if password == secretNumber:
            return "you pass it"
        else:
            return "try it again"
    #@-others
#@+node:2015.20141215184040.1822: ** run eviron
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 在 openshift
    application = cherrypy.Application(Guess())
else:
    # 在其他環境下執行
    cherrypy.quickstart(Guess())
#@-others
#@-leo
