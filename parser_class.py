# Randy Vollrath

# Answer 1

# A class called HeadingParser that is a subclass of the
# HTMLParser class. It finds and collects the contents of all
# the headings in an HTML file fed to it. The parser identifies
# when a heading tag has been encountered and sets a boolean
# var in the class to indicate that.

from html.parser import HTMLParser
from urllib.request import urlopen

class HeaderParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.header = list()
        self.h= False
        
    def handle_starttag(self,tag,attrs):
        if tag in ['h1','h2','h3','h4','h5','h6']:
        #if tag[:1]=='h':    ??? Would this work instead???
            self.h = True
    
    def handle_endtag(self,tag):
        if tag in ['h1','h2','h3','h4','h5','h6']:
            self.h = False
    
    def handle_data(self,data):
        if self.h == True:
            c=data.strip()
            self.header.append(c)

    def getheadings(self):
        # returns the list of headings
        newLst = []
        for items in self.header:
            if items == '':
                pass
            else:
                newLst.append(items)
        return newLst


# Takes a url, opens it, feeds the html to a heading parser and
# returns the obtained headings

def testHP(url):
    content=urlopen(url).read().decode()
    h = HeaderParser()
    h.feed(content)
    return h.getheadings()

if __name__ == '__main__':
    import doctest
    print(doctest.testfile('lab8TEST.py'))
