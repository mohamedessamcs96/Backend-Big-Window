import math
import numpy as np

test_scores=[88,92,34,11,22]
print(np.mean(test_scores))

s1=[math.sqrt(x)*10 for x in test_scores]
print(np.mean(s1))




#use list compreheisive to avoid spagiti code

def flat_curve(arr,n):
    return [i+n for i in arr]

s2=flat_curve(test_scores,10)

