# python3
import sys
from threading import Thread
import numpy as np

def get_height(i, values, heights):
    if heights[i] != 0:
        return heights[i]
    if values[i] == -1:
        heights[i] = 1
    else:
        heights[i] = get_height(values[i], values, heights) + 1
    return heights[i]

def compute_height(n, values):
    max_height = 0
    heights = np.zeros(n, dtype=int)
    for i in range(n):
        height = get_height(i, values, heights)
        if height > max_height:
            max_height = height
    return max_height

def read_input():
    while True:
        source = input("Enter I or F: ").strip().upper()

        if source == 'I':
            try:
                n = int(input("Enter element count: "))
                values = np.asarray(list(map(int, input("Enter values: ").split())))
                return n, values
            except ValueError:
                print("Invalid input")
            
        elif source == 'F':
            filename = input("Enter file name: ")
            if 'a' in filename:
                return None, None

            try:
                with open(f"./test/{filename}", "r") as file:
                    n = int(file.readline())
                    values = np.asarray(list(map(int, file.readline().split())))
                return n, values
            except FileNotFoundError:
                print("File not found")
        else:
            print("Invalid source")

def main():
    n, values = read_input()
    if n is None or values is None:
        return
    max_height = compute_height(n, values)
    print(max_height)

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    Thread(target=main).start()