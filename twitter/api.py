import requests


class TwitterAPI:
    def __init__(self, bearer_token):
        self.BEARER_TOKEN = bearer_token

    BASE_URL = "https://api.twitter.com/2/tweets/counts/recent"

    def tweet_count(self, query_string):
        result = requests.get(self.BASE_URL, params={'query': query_string},
                     headers={"Authorization": f'Bearer {self.BEARER_TOKEN}'})

        if result.status_code != 200:
            print(result.text)
            return 0

        twit_resp = result.json()
        total_count_of_tweets = twit_resp["meta"]["total_tweet_count"]
        return total_count_of_tweets