roll = "1024160035"
L=[int(digit)*10 for digit in roll]

scores = tuple(L[:8])
print(scores)

highest_score = max(scores)
print(highest_score)
highest_score_index = scores.index(highest_score)
print(highest_score_index)
lowest_score = min(scores)
print(lowest_score)
lowest_count = scores.count(lowest_score)
print(lowest_count)


##Tuples are immutable, so they cannot be reversed in place.
user_score = int(input("Enter a score to search: "))

if user_score in scores:
        print("First occurrence index:", scores.index(user_score))
else:
    print("Score not present in the tuple.")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

##Tuples are immutable so they cant be changed at a specified index
first_score,second_score,*remaining_scores = scores
print(first_score)
print(second_score)
print(remaining_scores)