# Recursion in Python means to have a function call itself in order to solve a particular problem.
# for example, your ancestors can be defined recursively: your parent has parents, who have parents, and so on. who are all your ancestors?
def get_ancestors(person, family_tree):
    # Base case: if the person has no parents in the family tree, return an empty list
    if person not in family_tree or not family_tree[person]:
        return []
    
    ancestors = []
    # Recursive case: for each parent of the person, get their ancestors
    for parent in family_tree[person]:
        ancestors.append(parent)
        ancestors.extend(get_ancestors(parent, family_tree))
    
    return ancestors

# Example family tree represented as a dictionary
family_tree = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["David", "Eve"],
    "Carol": ["Frank"],
    "David": [],
    "Eve": [],
    "Frank": []
}

# Get ancestors of Alice
print(get_ancestors("Alice", family_tree))

# Recursion is often used to traverse data structures with nested or hierarchical relationships, such as trees or graphs.
# Note that most programming problems can be solved without recursion, but recursion can provide a more elegant and concise solution in certain cases (like tree traversal).

# Also, recursion can lead to infinite loops if not created correctly, however python has a recursion limit (which can be changed using sys.setrecursionlimit()) to prevent this from happening.
# Be cautious when using recursion, especially with deep or complex data structures, as it can lead to stack overflow errors if the recursion depth exceeds the limit.
# Always ensure that your recursive functions have a well-defined base case to terminate the recursion.

# Another more simple recursive function is just counting down from any n to 0
def countdown(n):
    if n <= 0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n-1)

# Notice that the function has a definite base case (n <= 0) and a recursive case (countdown(n-1)).
countdown(5)

# Here is the non recursive version of the same countdown function:
def countdown_non_recursive(n):
    while n > 0:
        print(n)
        n -= 1
    print("Countdown finished!")

# Note that for such a simple use case, the non-recursive version is often preferred due to its simplicity and efficiency.
countdown_non_recursive(5)