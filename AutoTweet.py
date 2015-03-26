
import twitter
import datetime


api = twitter.Api(consumer_key="Q64bTmPxvwMdc316c1ltdISBa",consumer_secret="OSpBG5wllJVovXWBDkx0s7s0p40o4sBDyifZYulCD84XLspe1f",                                  access_token_key="256981328-2btHERPIxsoEQqOunm531ZdM8qI0l3g3JZJxloFM",access_token_secret="MofFdtukeCmrXBxYWYEM8SfqGTNsyn8IwoC02ArfWxzrr")


timestamp = datetime.datetime.utcnow()


response = api.PostUpdate("Tierney get off my twitter!!" + str(timestamp))


print("Status updated to: " + response.text)