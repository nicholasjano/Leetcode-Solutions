# Solution Walk Through
Question: https://leetcode.com/problems/design-twitter/

## Intuition
I can create a following dictionary to store the userId as a key, and anyone they are following as a set value. I can also create a tweets dictionary with the userId as a key, and their tweets along with a timestamp. To post a tweet, simply add the tweet to the tweets dictionry. To add or remove a follower, just modify the following dictionary. To get the news feed, iterate through tweets by the users followees and themselves. For each user, store their top 10 most recent tweets in a heap, as 10 is the max tweets for the feed. Afterward, pop the most recent 10 tweets from the heap for the feed.

## Approach
- `__init__()`:
    - Initialize the `following` dictionary to store users that a user follows.
    - Initialize the `tweets` dictionary to store the tweets by a user.
    - Initialize a tweet counter as a timestamp.
- `postTweet()`:
    - Add the tweet along with the current counter to the users `tweets`.
- `getNewsFeed()`:
    - Get the total list of posters, which is the users followers and themselves.
    - Loop through the posters top 10 tweets and add them to a heap.
    - Once completed for every poster, take the top 10 values from the heap for the feed.
    - In the case where a user doesn't have 10 tweets or the heap doesn't contain 10 tweets, take the maximum.
- `follow()`:
    - Add the followee within the followers `following` dictionary values.
- `unfollow()`:
    - Remove the followee from the followers `following` dictionary values.

## Time Complexity
`__init__()`: $O(1)$ \
`postTweet()`: $O(1)$ \
`getNewsFeed()`: $O(F)$ \
`follow()`: $O(1)$ \
`unfollow()`: $O(1)$

$F$ represents the total amount of following relations.

## Space Complexity
$O(T + F)$

$T$ represents the total amount of tweets.