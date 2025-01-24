import os
import yaml

current_dir = os.getcwd()

target_dir = "definition"

file_name = "test.yaml"

file_path = os.path.join(current_dir, target_dir, file_name)

with open(file_path, 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['prime_numbers'][0])
print(prime_service['rest']['port'])