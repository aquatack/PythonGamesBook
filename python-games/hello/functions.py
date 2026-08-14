def fruit_score(fruit):
    if fruit == "apple":
       return 10
    elif fruit == "banana":
        return -5

fruit_score("apple")
fruit_score("banana")

total_score = fruit_score("apple") + fruit_score("banana")
print(total_score)