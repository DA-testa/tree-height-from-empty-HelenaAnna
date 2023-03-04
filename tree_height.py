# python3
import sys
import threading
import numpy as np


def compute_height(n: int, values: np.ndarray) -> int:
    max_height = 0
    heights = np.zeros(n, dtype=int)

    def get_height(i: int) -> int:
        if heights[i] != 0:
            return heights[i]

        if values[i] == -1:
            heights[i] = 1
        else:
            heights[i] = get_height(values[i]) + 1

        return heights[i]

    for i in range(n):
        height = get_height(i)
        if height > max_height:
            max_height = height
    
    return max_height


def main() -> None:
    while True:
        source = input("Enter I or F: ").strip().upper()

        if source == 'I':
            try:
                n = int(input("Enter element count: "))
                values = np.asarray(list(map(int, input("Enter values: ").split())))
                break
            except ValueError:
                print("Invalid input")
            
        elif source == 'F':
            filename = input("Enter file name: ")
            if 'a' in filename:
                return

            try:
                with open(f"./test/{filename}", "r") as file:
                    n = int(file.readline())
                    values = np.asarray(list(map(int, file.readline().split())))
                break
            except FileNotFoundError:
                print("File not found")
        else:
            print("Invalid source")
            return

    max_height = compute_height(n, values)

    print(max_height)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=main).start()