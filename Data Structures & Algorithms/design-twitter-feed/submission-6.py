import heapq
class Twitter:

    def __init__(self):
        #some sort of graph structure
        #adjacency list?
        #every user should have a current feed
        #when a user posts, it updates the feed of its followees
        #we first implement this idea, putting the bulk of the work on the getNewsFeed func.
        #we build newsfeed from scratch everytime. 
        self.global_time = 0
        self.posts: Dict[int:List[(float, int)]] = {}
        self.followee_per_user: Dict[int:Set[int]] = {}

        #self.feed_cache_per_user: Dict[str:List[str]] = {}
        #self.follewer_per_user: Dict[str:List[str]] = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        userPost = self.posts.get(userId, [])
        if not userPost:
            self.posts[userId] = [(self.global_time, tweetId)]
        else:
            userPost.append((self.global_time, tweetId))
    
        self.global_time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #dynamic construction of max heap
        heap = []
        newsFeed = []
        followees = self.followee_per_user.get(userId, None)

        if not followees:
            self.followee_per_user[userId] = {userId}
            followees = self.followee_per_user[userId]
        else:
            followees.add(userId)


        pos_counter = {followee: -1 for followee in followees}

        for followee in followees:
            posts = self.posts.get(followee, None)
            if not posts:
                continue
            
            time, tweetId = posts[-1]
            heapq.heappush(heap, [-time, tweetId, followee])

        while len(newsFeed) < 10 and heap:
            time, tweetId, followee = heapq.heappop(heap)
            newsFeed.append(tweetId)
            pos_counter[followee] -= 1
            pos = pos_counter[followee]

            followee_posts = self.posts[followee]
            if abs(pos) <= len(followee_posts):
                time, tweetId = followee_posts[pos]
                heapq.heappush(heap,[-time, tweetId, followee])

        
        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        userFollowee = self.followee_per_user.get(followerId, set())
        if not userFollowee:
            self.followee_per_user[followerId] = {followeeId}
        else:
            userFollowee.add(followeeId)
    

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        userFollowee = self.followee_per_user.get(followerId, None)
        if not userFollowee:
            return
        else:
            if followeeId in userFollowee:
                userFollowee.remove(followeeId)
        #remove from followerID from follewer_per_user
        #clean follower feed cache (going over list of 10)
        #rebuild cache via follower_per_user and posts

        
