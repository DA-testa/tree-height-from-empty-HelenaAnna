# python3
import sys
import threading

def compute_height(n, parents):
    # Write this function
    children = {i: [] for i in range(n)}

    # populate the children dictionary
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            children[p].append(i)

    def height(node):
        if not children[node]:
            return 1
        return 1 + max(height(child) for child in children[node])

    # compute the height of the tree rooted at the root node
    return height(root)

def main():
    # let user input file name to use
    if len(sys.argv) > 1:
        # read input from file
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    else:
        # read input from keyboard
        while True:
            try:
                n = int(input())
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
        parents = list(map(int, input().strip().split()))

    max_height = compute_height(n, parents)
    print(max_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()