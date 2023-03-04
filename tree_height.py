# python3
import sys
import threading
import numpy as np

def compute_height(n: int, par: list[int]) -> int:
    h = np.zeros(n, dtype=int)
    maxh = -1

    for i, _ in enumerate(par):
        l = i
        h_i = 1

        while par[l] != -1:
            if h[l] != 0:
                h_i += h[l] - 1
                break

            h_i += 1
            l = par[l]

        h[i] = h_i
        maxh = max(maxh, h[i])

    # compute the height of the tree rooted at the root node
    return maxh

def main() -> None:
    # let user input file name to use
    txt = input()
    if 'F' in txt:
        file = input()
        file = f"test/{file}"

        if 'a' not in file:
            try:
                with open(file, "r") as f:
                    n = int(f.readline())
                    par = list(map(int, f.readline().split()))
                    print(compute_height(n, par))

            except FileNotFoundError:
                print("not found")
                return

    if 'I' in txt:
        n = int(input())
        par = list(map(int, input().split()))
        print(compute_height(n, par))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=main).start()
 # max depth of recursion # new thread will get stack of such size