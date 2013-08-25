#!/usr/bin/python2
from lxml import etree
from sys import argv
import urllib2

def getPic(pageURL):
    parser = etree.HTMLParser()
    print "There are " + str(len(pageURL)) + " pictures"
    for i in pageURL:
        time.sleep(3)
        tree = etree.parse(i.attrib['href'], parser)
        r2 = tree.xpath("//*[@id='i3']/a/img")
        req = urllib2.Request(r2[0].attrib['src'])
        req.add_header('Referer', 'http://g.e-hentai.org/')
        r = urllib2.urlopen(req)
        f = open(r2[0].attrib['src'].split('/')[-1], "wb")
        f.write(r.read())
        f.close

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

#check page number first [ptds] twice
r = tree.xpath("//*[@class='ptt']") #get the top page index
#page index start from 1, end of ">"(next page), last page is at the last two, r[0].xpath('./tr/td/a')[-2]
lastPage = int(r[0].xpath('./tr/td/a')[-2].text) #0 - lastPage
print lastPage
for page in range(0, lastPage, 1):
    print "page: " + str(page)
    if page == 0:
        #run parse normal
        getPic(tree.xpath("//*[@class='gdtm']/div/a"))
        continue
    #url is argv[1] + "?p=" + page
    tree = etree.parse(argv[1] + "?p=" + str(page), parser)
    getPic(tree.xpath("//*[@class='gdtm']/div/a"))

#result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
#print (result)

#get meta data

#get album name h1[@id=gn]

#get picture
'''r = tree.xpath("//*[@class='gdtm']/div/a") #get the pic's page URL
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
    f = open(r2[0].attrib['src'].split('/')[-1] + ".jpg", "wb") #save the img, r2[0].attrib['src'].split('/')[-1] is the name of picture(problem)
    f.write(r.read()) #write out the img
    f.close'''
