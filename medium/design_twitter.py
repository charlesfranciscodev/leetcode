from collections import defaultdict


class Twitter:
    def __init__(self):
        self.tweets = []  #  => tweets list [(tweet_id, user_id)]
        self.following = defaultdict(set)  # user_id => ids of users he is following

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append((tweet_id, user_id))

    def getNewsFeed(self, current_user_id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweet_ids = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweet_id, user_id = self.tweets[i]
            if user_id == current_user_id or user_id in self.following[current_user_id]:
                tweet_ids.append(tweet_id)
                if len(tweet_ids) == 10:
                    break
        return tweet_ids

    def follow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[follower_id].discard(followee_id)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
