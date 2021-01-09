import tweepy

def autenticar():
    consumer_key = "mDQiWnpgG2SBQJBqMMxBtQDmL"
    consumer_secret = "BH0UB599jUCXxwmgC58c2jAUiNMq95aVbQsUDJxM9yEmCgbgCI"

    access_token = "1326267633063309312-mbtW1yn7GuWdNly4IPuApG85UGmgGz"
    access_token_secret = "glNOmPtvwjAxNUu7gIY7YP3HbT5h4qrMBtBLeFRdhCow5"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

if __name__ == "__main__":
    autenticar()