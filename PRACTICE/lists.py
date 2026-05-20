friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print (friends[0])  # Output: Alice
print (friends[1])  # Output: Bob
print (friends[2])  # Output: Charlie
print (friends[3])  # Output: David
print (friends[4])  # Output: Eve   

friends [0] = "Alex"
print (friends[0])  # Output: Alex
print (friends[0:3])  # Output: ['Alex', 'Bob', 'Charlie']
print (friends[1:4])  # Output: ['Bob', 'Charlie', 'David']
friends.append("Frank")
print (friends)  # Output: ['Alex', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

l1 = [12, 41, 33, 15, 56]
#l1.sort()
#print (l1)  # Output: [12, 15, 33, 41, 56]
l1.reverse()
print (l1)  # Output: [56, 41, 33, 15, 12]