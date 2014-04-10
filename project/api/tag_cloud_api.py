urllib
urllib2
import urllib2
data = {}
data['source'] = 'text'
data['text'] = 'ToCloud is an online website that allows visual representation of some text as a bunch of words based on a weight associated to each word. Using ToCloud on a blog, news website will allow users to find about topics that are being discussed.'
data['language'] = 'English'
data['topTags'] = 50
data['minFreq'] = 1
data['showFreq'] = no
data['showFreq'] = 'no'
data['doStemming'] = 'yes'
data['lettercase'] = 'lowercase'
data['stoplist'] = ''
url_data = urllib.urlencode(data)
url_data
handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)
request = urllib2.Request(url, data=data)
url = 'http://tagcrowd.com/'
request = urllib2.Request(url, data=data)
request.add_header("Content-Type",'application/json')
request.get_method="POST"
c = opener.open(request)
request.get_method=lambda :"POST"
c = opener.open(request)
request = urllib2.Request(url, data=url_data)
c = opener.open(request)
c.code
res =c.read()
soup = BeautifulSoup(res)
BeautifulSoup.BeautifulSoup(res)
res = _
res.text
soup.title
res.title
import lxml
from lxml import etree
parser = etree.HTMLParser()
res
res.find('textarea')
res.find('textarea').text
text = res.find('textarea').text
urllib
import urllib
import HTMLParser
h = HTMLParser.HTMLParse()
h = HTMLParser.HTMLParser()
h.unescape(text)
text = _
text.replace('\n','')
text.replace('\t','')
text = _
text.replace('\n','')