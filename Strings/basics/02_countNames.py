# Dictionary and counter in Python to find winner of election

# Given an array of names of candidates in an election.
# A candidate name in the array represents a vote cast to the candidate.
# Print the name of candidates received Max vote.
# If there is tie, print a lexicographically smaller name.

# Examples: 
# Input :  votes[] = {"john", "johnny", "jackie", 
#                     "johnny", "john", "jackie", 
#                     "jamie", "jamie", "john",
#                     "johnny", "jamie", "johnny", 
#                     "john"};
# Output : John
# We have four Candidates with name as 'John', 
# 'Johnny', 'jamie', 'jackie'. The candidates
# John and Johny get maximum votes. Since John
# is alphabetically smaller, we print it.

from collections import Counter

# Method 1: 
# Convert given list of votes into dictionary using Counter(iterator) method. We will have a dictionary having candidate names as Key and their frequency ( counts ) as Value.
# Since more than 1 candidate may get same number of votes and in this situation we need to print lexicographically smaller name, so now we will create another dictionary by traversing previously created dictionary, counts of votes will be Key and candidate names will be Value.
# Now find value of maximum vote casted for a candidate and get list of candidates mapped on that count value.
# Sort list of candidates having same number of maximum votes and print first element of sorted list in order to print lexicographically smaller name.

def electionWinner (inputList):
    votes = Counter (inputList)
    dict = {}
    
    for value in votes.values ():
        dict[value] = list ()
    
    for (key, values) in votes.items ():
        dict[values].append (key)

    maxVotes = sorted (dict.keys(), reverse=True)[0]

    if len (dict[maxVotes]) > 1:
        print (sorted (dict[maxVotes])[0])
    else:
        print (dict[maxVotes][0])

    # Time complexity : O(nlogn) 
    # Auxiliary Space : O(n)
    # =================================================================================================
# Method 2: 
# Shorter method.
#     Count the number of votes for each person and stores in a dictionary. 
#     Find the maximum number of votes. 
#     Find corresponding person(s) having votes equal to maximum votes. 
#     As we want output according to lexicographical order, so sort the list and print first element. 

def electionWinnerShorter (inputList):
    votes = Counter (inputList)
    maxVotes = max (votes.values ())
    output = [i for i in votes.keys () if votes[i] == maxVotes]
    print (sorted (output)[0])

# Time complexity : O(n) 
# Auxiliary Space : O(1)


if __name__ == '__main__':
    inputList =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

    # electionWinner (inputList)
    electionWinnerShorter (inputList)