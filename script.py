from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from random import randint
import tweepy, time, sys
import json


CONSUMER_KEY = '6ku8ybz2sqCubq3qtZKmNONNh'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'N69l4mu0TL9zqwLtuKbG2Il3LqAfeHmxsw0VFOxj1mWKQJrX9v'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '357289633-jhKLehdgZLFgoUetUcXk64JH9hfrgKIfrlZPKXFv'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KooJ0QAeYl7G1eDxSoP1g7YVphK1KtYMDStTyicHk8JML'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def translate(t):
	t = t.replace(" house "," hizzle ")
	t = t.replace(" in "," up in ")
	t = t.replace(" the "," da ")
	t = t.replace(" retweet "," hmu ")
	t = t.replace(" agree "," feel ")
	t = t.replace(" you "," ya ")
	t = t.replace(" step "," get ")
	t = t.replace(" change "," changizle ")
	t = t.replace(" for "," fo' ")
	t = t.replace(" speaking "," frontin ")
	t = t.replace(" important "," bangin' ")
	t = t.replace(" what "," wud ")
	t = t.replace(" word "," WORD ")
	t = t.replace(" America "," Amerikuh ")
	t = t.replace(" minister "," minista ")
	t = t.replace(" isn't "," aint ")
	t = t.replace(" to "," ta ")
	t = t.replace(" President "," Prez ")
	t = t.replace(" Obama ", " Obeezy ")
	t = t.replace(" is "," be ")
	t = t.replace(" and "," n ")
	t = t.replace(" serious "," straight up ")
	t = t.replace(" change "," changizzle ")
	t = t.replace(" citizen "," playa hater ")
	t = t.replace(" people"," playa haters")
	t = t.replace(" folks"," player haters")
	t = t.replace(" speaking"," frontin")
	t = t.replace(" all "," y'all ")
	t = t.replace(" countries"," hoods")
	t = t.replace(" we "," us brothers ")
	t = t.replace(" have"," gots")
	t = t.replace(" big"," big ass")
	t = t.replace(" have to"," gotta")
	t = t.replace(" community"," hood")
	t = t.replace(" this"," dis")
	t = t.replace(" too"," 2")
	t = t.replace(" first"," original gangsta")
	t = t.replace(" can "," ass can ")
	t = t.replace(" something"," sumthin")
	t = t.replace(" about "," bout ")
	t = t.replace(" that"," dat")
	t = t.replace(" it "," dat shit ")
	t = t.replace(" children"," young bloods")
	t = t.replace(" their "," they ")
	t = t.replace(" do not"," aint")
	t = t.replace(" deliviering"," dropping")
	t = t.replace(" at "," all up in ")
	t = t.replace(" strong"," phat")
	t = t.replace(" large"," dope")
	t = t.replace(" giant"," phat")
	t = t.replace(" get"," git")
	t = t.replace(" no"," nah")
	t = t.replace(" sure"," shizzle")
	t = t.replace(" partnering"," crewing up")
	t = t.replace(" companies"," dope dealers")
	t = t.replace(" leaders"," g-units")
	t = t.replace(" sexual"," bubble butt")
	t = t.replace(" video"," vid")
	t = t.replace(" check"," peep")
	t = t.replace(" say"," holla")
	t = t.replace(" said"," holla")
	t = t.replace(" ready"," rdy")
	t = t.replace(" your ", " yo ")
	t = t.replace(" those", " dem")
	t = t.replace(" good ", " phat ")
	t = t.replace(" Good ", " Dope ")
	t = t.replace(" more", " mo")
	t = t.replace(" are ", " is ")
	t = t.replace(" consumers ", " suckas ")
	t = t.replace("ng ", "n ")

	
	return t
		

class listener(StreamListener):
    
    print "listening..."
    def on_data(self, data):
		tweets = json.loads(data)
		if tweets["user"]["screen_name"] == "BarackObama":
			print "retrieving...\n"
			print tweets["text"] + "\n"
			print "translating..."
			tweets["text"] = translate(tweets["text"])
			print "successfully translated\n"
			print tweets["text"] + "\n"
			if len(tweets["text"]) < 140:
				if len(tweets["text"]) < 120:
					print "appending..."
					rnd = randint(0,7)
					appStrings = ["", ", nahmean", "", ", shiiiit", "", ", word up", "", ", biatch"]
					tweets["text"] = tweets["text"] + appStrings[rnd]
					print "successfully appended"
				print "posting..."
				api.update_status(tweets["text"])
				print "succesfully posted"
				print "### \n\n"
			else:
				print "tweet too long\n\n"
			print "listening..."
		#print tweets["user"]["screen_name"]
    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(follow=["813286"])

#Obama ID 813286
#My ID 357289633
#secondary test Id 2417516252

