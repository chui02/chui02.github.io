from collections import defaultdict, deque
import time
import heapq

class User:
    def __init__(self, userID):
        self.id = userID
        self.following = set()
        self.followers = set()
        self.posts = []
        self.inbox = []
        self.privacy = "public"  #Can be set to diff settings like public, private, followers-only

class Post:
    post_id_counter = 0

    def __init__(self, userID, content, privacy="public", replyTo=None):
        self.id = Post.post_id_counter
        Post.post_id_counter += 1
        self.userID = userID
        self.content = content
        self.timestamp = time.time() #Honestly have no clue how to actually implement a timestamp well
        self.likes = 0
        self.privacy = privacy
        self.replyTo = replyTo
        self.replies = []
        self.mentions = self.mentions()

    def mentions(self):
        return [word[1:] for word in self.content.split() if word.startswith("@")]

class SocialMediaService:
    def __init__(self):
        self.users = {}
        self.posts = []
        self.trendingHeap = []

    def registeredUser(self, userID):
        if userID not in self.users:
            self.users[userID] = User(userID)

    def postMessage(self, userID, content, privacy="public", replyTo=None):
        if userID not in self.users:
            return "User not found."

        post = Post(userID, content, privacy, replyTo)
        self.users[userID].posts.append(post)
        self.posts.append(post)

        if replyTo is not None:
            parent_post = next((p for p in self.posts if p.id == replyTo), None)
            if parent_post:
                parent_post.replies.append(post)

        heapq.heappush(self.trendingHeap, (-post.likes, post.timestamp, post))
        return post.id

    def follow(self, follower_id, followID):
        if follower_id in self.users and followID in self.users:
            self.users[follower_id].following.add(followID)
            self.users[followID].followers.add(follower_id)

    def like_post(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                post.likes += 1
                return

    def send_message(self, senderID, receiverID, message):
        if receiverID in self.users:
            self.users[receiverID].inbox.append((senderID, message))

    def getNewsFeed(self, userID):
        if userID not in self.users:
            return []

        feed = []
        user = self.users[userID]
        for followID in user.following:
            followee = self.users.get(followID)
            if followee:
                for post in followee.posts:
                    if post.privacy == "public" or \
                       (post.privacy == "followers-only" and userID in followee.followers):
                        feed.append(post)

        feed.sort(key=lambda p: p.timestamp, reverse=True)
        return [f"@{p.userID}: {p.content}" for p in feed[:10]]

    def getTrendingPosts(self, limit=5):
        sortedPosts = sorted(self.posts, key=lambda p: (-p.likes, p.timestamp))
        return [f"@{p.userID}: {p.content} ({p.likes} likes)" for p in sortedPosts[:limit]]

s = SocialMediaService()

s.registeredUser("jack")
s.registeredUser("daniela")
s.registeredUser("lee")

s.follow("jack", "daniela")
s.postMessage("daniela", "Hello world!")
s.postMessage("daniela", "@jack Check this out!", privacy="followers-only")

s.like_post(0)
s.send_message("jack", "daniela", "Hey daniela!")

print("Jack's Feed:", s.getNewsFeed("jack"))
print("Trending:", s.getTrendingPosts())