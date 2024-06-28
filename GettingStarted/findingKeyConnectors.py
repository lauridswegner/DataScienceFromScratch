users = [
    {"id": 0,"name": "Hero"},
    {"id": 1,"name": "Dunn"},
    {"id": 2,"name": "Sue"},
    {"id": 3,"name": "Chi"},
    {"id": 4,"name": "Thor"},
    {"id": 5,"name": "Clive"},
    {"id": 6,"name": "Hicks"},
    {"id": 7,"name": "Devin"},
    {"id": 8,"name": "Kate"},
    {"id": 9,"name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to fill it with data
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

# getting total of connections
total_connections = sum(number_of_friends(user) for user in users)
print("total connections:", total_connections)

# average connections
num_users = len(users)
avg_connections = total_connections/num_users
print("avg connections:", avg_connections)

# sorting from most to least friends
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse = True
)
print(num_friends_by_id)

# finding friends of friends
from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]           # for each of my friends
        for foaf_id in friendships[friend_id]           # find their friends
        if foaf_id != user_id                           # who aren't me
        and foaf_id not in friendship_pairs[user_id]    # and aren't my friends
    )

print(friends_of_friends(users[3]))