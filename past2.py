import numpy as np

# Part A
foo = np.arange(30)
print("foo:", foo)
print("Shape of foo:", foo.shape)

# Part B
bar = foo.reshape(5, 6)
print("bar:\n", bar)
print("Shape of bar:", bar.shape)

# Part C
baz = foo.reshape(2, 3, 5)
print("baz:\n", baz)
print("Shape of baz:", baz.shape)

# Part D
bar[1, 0] = -1  # Set first value in the second row to -1
print("Modified bar:\n", bar)
print("foo after modifying bar:\n", foo)
print("baz after modifying bar:\n", baz)

# Part E
sum_over_second = np.sum(baz, axis=1)
print("Sum of baz over second dimension:\n", sum_over_second)

sum_over_third = np.sum(baz, axis=2)
print("Sum of baz over third dimension:\n", sum_over_third)

sum_over_first_and_third = np.sum(baz, axis=(0, 2))
print("Sum of baz over both first and third dimensions:\n", sum_over_first_and_third)

# Part F
second_row = bar[1, :]
print("Second row of bar:", second_row)

last_column = bar[:, -1]
print("Last column of bar:", last_column)

top_right_submatrix = bar[:2, -2:]
print("Top right 2x2 submatrix of bar:\n", top_right_submatrix)
