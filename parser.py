#!/usr/bin/python2
from lxml import etree
from sys import argv
import urllib2

if len(argv) == 1:
    print "arguments too less"
    exit()
elif len(argv) > 2: #support multi-index?
    print "arguments too more"
    exit()

if argv[1].find('http://g.e-hentai.org/g/') == -1:
    print "Insert the legal URL"
    exit()

parser = etree.HTMLParser()
tree = etree.parse(argv[1], parser) #get the index

#check page number first


#result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
#print (result)
r = tree.xpath("//*[@class='gdtm']/div/a") #get the pic's page URL
counter = 1
for i in r:
    tree = etree.parse(i.attrib['href'], parser) #to the pic's page
    r2 = tree.xpath("//*[@id='i3']/a/img") #get the pic's real URL
    #print r2[0].attrib['src'] #print pic's URL
    req = urllib2.Request(r2[0].attrib['src']) #set the download url
    req.add_header('Referer', 'http://g.e-hentai.org/') #add refer
    r = urllib2.urlopen(req) #download the img
    #to do
    #add progress bar for urllib2, reference: http://goo.gl/EFFqvE
    #or use urlgrabber
    f = open(str(counter) + ".jpg", "wb") #save the img
    f.write(r.read()) #write out the img
    f.close
    counter += 1
