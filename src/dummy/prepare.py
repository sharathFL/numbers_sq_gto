import yaml

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

start = params['prepare']['start']
end = params['prepare']['end']

with open('data/numbers.txt', 'w') as f:
    for i in range(start, end):
        f.write(f"{i}\n")
