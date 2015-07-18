import urllib
import webbrowser as web
url = "http://www.google.de"
content = urllib.urlopen(url).read()
open("mein.html","wb").write(content)
web.open_new_tab('mein.html')
