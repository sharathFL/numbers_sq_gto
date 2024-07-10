import yaml

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

multiplier = params['process']['multiplier']

with open('data/numbers.txt', 'r') as infile, open('data/squared_numbers.txt', 'w') as outfile:
    numbers = [int(line.strip()) for line in infile]
    processed_numbers = [num * multiplier for num in numbers]
    for number in processed_numbers:
        outfile.write(f"{number}\n")
