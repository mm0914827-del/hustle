# ticket 1 # Mohammed ( lab 3 ) intro to python

# ticket 2
#  predict m and d will print
print (mohammed[0])
print (mohammed[len(mohammed) -1])
# explain:the last index is len(username)

#ticket 3

print ("welcome to loop @ mohammed")
print (f" welcome to loop @ {mohammed}")
# explain: the f-stringwas easier because it was easier to read.

# ticket 4 
# predict : i think it will give an error.
mohammed[0] = "x"
# copy the error message here after ruunning th code:
# TypeError: 'str' object does not support item assignment
print (mohammed,uupper())
# explain: the error occurred because strings in Python are immutable, meaning their individual characters cannot be changed after the string is created.

# ticket 5
feed = ["first day at loop", "coding is fun","just caught a shiny pokemon!"]
print(len(feed))
print(feed[0])
# explain: I uused the index 0 to get the first post becauuse python lists are zero-indexed.

# ticket 6
feed.append('lunch break!')
print(feed)
explain: the fourth post sits at index 3 because indexing starts counting at 0, 1,2 and 3.

# ticket 7
feed.pop(0)
feed.sort()
print(feed)
explain: the first post was removed using pop(0), and then the remaining posts were sorted alphabetically.

# ticket 8
prfile = {
    "username": "mohammed",
    "followers": 200
    "verified": True
}
print(profile["followers"])
# peofile[0] # copy the error message here after running this line
# keyError: 0 
explain: the error occurred because dictionaries in Python are accessed by keys, not by numeric indices. The key "0" does not exist in the profile dictionary.

# ticket 9
profile["followers"] = profile["followers"] + 50 # or profile["followers"] += 50
profile["bio"] = "coding my way through the hustle."
print(profile)

print(profile.get("age"))

explain: the get() method is used to safely retrieve a value from a dictionary by its key, and it returns None if the key is not found, instead of raising a KeyError.

# ticket 10
print(f"@{profile['username']} has {profile['followers']} followers and {lens(feed)} posts. Top post: first day at loop")
