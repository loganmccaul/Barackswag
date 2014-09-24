from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
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
	t = t.replace("house","hizzle")
	t = t.replace("the","tha")
	t = t.replace("retweet","hmu")
	t = t.replace("agree","feel")
	t = t.replace("you","ya")
	t = t.replace("up","turnt")
	t = t.replace("step","get")
	t = t.replace("support","back up")
	t = t.replace("action","bang bang")
	t = t.replace("change","word")
	t = t.replace("for","fo")
	t = t.replace("speaking","frontin")
	t = t.replace("important","bangin'")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")
	t = t.replace("for","fo")


	return t
		

class listener(StreamListener):
    
    def on_data(self, data):
		tweets = json.loads(data)
		print tweets["text"]
		tweets["text"] = translate(tweets["text"])
		print tweets["text"]
		api.update_status(tweets["text"])
    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(follow=["357289633"])

#Obama ID 813286
#My ID 357289633

