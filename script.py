from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from random import randint
import tweepy, time, sys
import json


CONSUMER_KEY = 'CQNkbsaG4jl8bOQak0RjZkAXg'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'qno72MTcPiZxLZ4ozjdklQGbKOs65vhY0GORGpxmmqbQMqWZuZ'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '357289633-jhKLehdgZLFgoUetUcXk64JH9hfrgKIfrlZPKXFv'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KooJ0QAeYl7G1eDxSoP1g7YVphK1KtYMDStTyicHk8JML'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

follow_list = ["2417516252", "1339835893", "216776631", "23022687", "15745368", "216881337"]
user_lists = ["mclowgan", "hillaryclinton", "berniesanders", "tedcruz", "marcorubio", "randpaul"]


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
	t = t.replace(" to "," 2 ")
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
	t = t.replace(" too "," 2 ")
	t = t.replace(" first"," original gangsta")
	t = t.replace(" can "," can ")
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
	t = t.replace("Good ", "Dope ")
	t = t.replace(" more", " mo")
	t = t.replace(" are ", " is ")
	t = t.replace(" consumers ", " suckas ")
	t = t.replace(" going ", " finna ")
	t = t.replace(" mother ", " motha ")
	t = t.replace("'s ", "z ")
	t = t.replace(" news ", " shizz ")
	t = t.replace("ers ", "az ")
	t = t.replace(" meet ", " hook up wit ")
	t = t.replace(" cruel ", " cold-ass ")
	t = t.replace(" me ", " mah ")
	t = t.replace(" speech ", " rap ")
	t = t.replace(" follow ", " shout out to ")
	t = t.replace(" anyone ", " ne1 ")
	t = t.replace(" dad ", " pops ")
	t = t.replace(" friends", " homies ")
	t = t.replace("ing ", "in ")


	
	return t
		

class listener(StreamListener):
    
    print "listening..."
    def on_data(self, data):
		tweets = json.loads(data)
		if tweets["user"]["screen_name"].lower() in user_lists:
			print "retrieving...\n"
			print tweets["text"] + "\n"
			print "translating..."
			tweets["text"] = translate(tweets["text"])
			print "successfully translated\n"
			print tweets["text"] + "\n"
			if len(tweets["text"]) < 140:
				if len(tweets["text"]) < 120:
					print "appending..."
					usernames = tweets["user"]["screen_name"]
					tweets["text"] = tweets["text"] + " -" + usernames
					print "successfully appended username"
				if len(tweets["text"]) < 125:
					rnd = randint(0,6)
					appStrings = ["", ", nahmean", "", ", shiiiit", "", ", word up", ", biatch"]
					tweets["text"] = tweets["text"] + appStrings[rnd]
					print "succesfully added ending"
				print "posting..."
				if len(tweets["text"]) <= 140:
					api.update_status(status = tweets["text"])
					print tweets["text"]
					print "succesfully posted"
				else:
					print "Tweet too long"
				print "### \n\n"
			else:
				print "tweet too long\n\n"
			print "listening..."
		#print tweets["user"]["screen_name"]
    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(follow = follow_list)

#Obama ID 813286
#Hillary ID 1339835893
#Bernie ID 216776631
#Cruz ID 23022687
#OMalley ID 15824288
#Webb ID 2746932876
#Bush ID 113047940
#Walker ID 33750798
#Christie ID 90484508
#Huckabee ID 15416505
#Rubio ID 15745368
#Paul ID 216881337
#Santorum ID 58379000
#Perry ID 18906561
#Jindal ID 17078632
#Fiorina ID 65691824
#Carson ID 1180379185

#My ID 357289633
#Mclowgan test Id 2417516252

