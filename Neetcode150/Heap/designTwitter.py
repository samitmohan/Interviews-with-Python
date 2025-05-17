# https://leetcode.com/problems/design-twitter/
# Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the
# user followed or by the user themself. Tweets must be ordered from most recent to least recent.
"""
Not Hashmap because we need to remove values in unfollow and removing from list is O(N) : in hashset it's O(1)
"""

from collections import defaultdict


class Twitter:
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # array of userid and tweet id
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        i = len(self.tweets) - 1  # number of tweets (userID, tweetID)
        # get 10 most recent tweets
        while i >= 0 and len(ans) < 10:
            # if tweet posted by users who the user follows or user himself
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0] == userId:
                ans.append(self.tweets[i][1])  # add tweetID
            i -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        # hashset  (follower can follow multiple people : hashmap of lists)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
