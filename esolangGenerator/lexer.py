import os
import yaml

# testing script for yaml
# TODO: Remove and build template and template reader <-- Do this first 
#       Build lexer that builds from template to perform lexical analysis
#       Look into using c/cpp front end of LLVM (use llvmlite? JIT compilation supported)

current_dir = os.getcwd()

target_dir = "definition"

file_name = "test.yaml"

file_path = os.path.join(current_dir, target_dir, file_name)

with open(file_path, 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['prime_numbers'][0])
print(prime_service['rest']['port'])