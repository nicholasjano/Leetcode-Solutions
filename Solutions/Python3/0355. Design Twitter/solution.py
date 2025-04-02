class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_counter = 0
        self.news_tweet_amount = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.tweet_counter, tweetId))
        self.tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posters = self.following[userId].union({userId})
        options = []
        for poster in posters:
            if poster in self.tweets:
                tweets = self.tweets[poster]
                for i in range(len(tweets) - 1, max(-1, len(tweets) - self.news_tweet_amount - 1), -1):
                    timestamp, tweet = tweets[i]
                    options.append((timestamp, tweet))
        
        feed = []
        heapify(options)
        for i in range(min(self.news_tweet_amount, len(options))):
            _, tweet = heappop(options)
            feed.append(tweet)
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)