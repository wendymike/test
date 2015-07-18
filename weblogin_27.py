import webbrowser as web
import time
import os
import random
count = random.randint(3,5)
j = 1
while j < count:
    i = 1
    while i <= 5:
        web.open_new_tab('http://google.de')
        i = i + 1
        time.sleep(0.8)
    else:
        os.system('taskkill /F /IM chrome.exe')
        print j, 'times'
    j = j + 1
