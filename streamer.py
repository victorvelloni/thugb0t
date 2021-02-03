import tweepy
import autenticador

class Listener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if tweet.user.id == self.me.id:
            print("eh seu mane")
        if not tweet.favorited:
            print(tweet.text)
            tweet.favorite()

    def on_error(self, status):
        print("Error detected")

def likes():
    api = autenticador.autenticar()
    tweets_listener = Listener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["stronda", "Stronda", "strondando", "Strondando", "strondar", "Strondar"])

if __name__ == "__main__":
    likes()