
numbers = [4, 1, 2, 1, 2, 1, 3, 4, 1]


most_frequent = max(set(numbers), key=numbers.count)


print("Most frequent element is:", most_frequent)
