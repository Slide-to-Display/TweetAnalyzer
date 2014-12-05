class Tweet:

    def __init__(self, _tweet, _geo, _sentiment=""):
        self.tweet = _tweet.strip()
        self.geo = _geo.strip()
        self.sentiment = _sentiment

    def __str__(self):
        return ("text: " + self.tweet + " | sentiment: " + self.sentiment)

    def __repr__(self):
        return ("text: " + self.tweet + " | sentiment: " + self.sentiment)
