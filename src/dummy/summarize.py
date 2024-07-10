# src/summarize.py
# This script calculates the sum of squared numbers.

with open('data/squared_numbers.txt', 'r') as f:
    squared_numbers = [int(line.strip()) for line in f]

total_sum = sum(squared_numbers)

with open('data/summary.txt', 'w') as f:
    f.write(f"Total Sum: {total_sum}\n")
