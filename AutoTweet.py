#modules being imported
import twitter
import datetime
import urllib2

#finding and opening the Chrome Database for the history
file = open("/Users/jmorgan13/Library/Application Support/Google/Chrome/Default/Current Session")
data = file.read()

#using rfind to search for the end of the http url
urlStart = str(data).rfind("http")
urlEnd = str(data).find(chr(0), urlStart)
url = data[urlStart:urlEnd]

#open url
response = urllib2.urlopen(url)
web = response.read()
print (web)

#find the title page from start to end
findPageTitle = web.find("<title>")
findPageTitleEnd = web.find("</title>")

title = web [findPageTitle:findPageTitleEnd]
title = title.replace("<title>", "")
print(title)

#twitter credentials 
api = twitter.Api(consumer_key="Q64bTmPxvwMdc316c1ltdISBa",consumer_secret="OSpBG5wllJVovXWBDkx0s7s0p40o4sBDyifZYulCD84XLspe1f",                                  access_token_key="256981328-2btHERPIxsoEQqOunm531ZdM8qI0l3g3JZJxloFM",access_token_secret="MofFdtukeCmrXBxYWYEM8SfqGTNsyn8IwoC02ArfWxzrr")

#recieves the time
timestamp = datetime.datetime.utcnow()

#posts tweet to twitter
response = api.PostUpdate("I have looked at " + title + url + str(timestamp))


print("Status updated to: " + response.text)