import tweepy
import keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key,keys.api_secret)
    auth.set_access_token(keys.access_token,keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api:tweepy.api,message:str,image_path = None):
    if image_path:
        api.update_status_with_media(message,image_path)
    else:
        api.update_status(message)

    print('tweeted successfully!')
   


if __name__ == '__main__':
    api = api()

    tweet(api,"here we go","/Users/suvigyapandey/Desktop/personal projects/tWITTER API project/10wmt-superJumbo-v4.jpg")

