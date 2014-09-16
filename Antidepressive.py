import urllib2, webbrowser, random, time
from HTMLParser import HTMLParser

searchTerms = raw_input("Enter search terms: ").replace(' ', '+')
waitPeriod = int(raw_input("Seconds between searches: "))

def checkGoogle():
    global search
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'}
    url = 'https://www.google.com/search?q='+searchTerms+'&biw=1608&bih=881&source=lnms&tbm=isch&sa=X&ei=HpYWVLPFAcOLiwLI4IGIBA&sqi=2&ved=0CAYQ_AUoAQ&dpr=0.9'
    request = urllib2.Request(url, None, header)
    u = urllib2.urlopen(request)
    data = u.read()
    f=open('akito.xml', 'wb')
    f.write(data)
    f.close

imgList = []
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0 
        self.data = []
    def handle_starttag(self, tag, attrs):
        global imgList
        if tag != 'a':
            return
        if self.recording:
            self.recording += 1
        for name, value in attrs:
            if name == 'class' and value == 'rg_l':
                imgList.append(attrs[0][1].split('&imgref', 1)[0].split('?imgurl=', 1)[1])
                break
        else:
            return
        self.recording = 1
    def handle_endtag(self, tag):
        if tag == 'a' and self.recording:
            self.recording -= 1
checkGoogle()
parser = MyHTMLParser()
f=open('akito.xml', 'r')
parser.feed(f.read())
f.close()

def unselectedPictureValue():
    global period
    checkedList = []
    while len(checkedList) < 70:
        randomNum = random.randint(0,99)
        while len([i for i in checkedList if i == randomNum]) > 0:
            randomNum = random.randint(0,99)
        link = imgList[randomNum]
        checkedList.append(randomNum)
        webbrowser.open(link)
        time.sleep(waitPeriod)
unselectedPictureValue()
