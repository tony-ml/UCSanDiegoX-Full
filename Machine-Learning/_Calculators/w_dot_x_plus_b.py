import numpy as np

# A linear classifier on  ℝ2  is specified by  𝑤=(−1,3)  and  𝑏=−6 .
# What label,  1  or  −1 , is assigned to the point  (1,1) ?

w = np.array([3,4])
x = np.array([1,2.5])
b = -12
y = 1

y  = w.dot(x) + b
print('w.x + b =', y)

# Test the classifier quickyly
if y > 0:
    print('Classify as 1')
elif y < 0:
    print('Classify as -1')
else:
    print('Classify as "Correct" or 0')
