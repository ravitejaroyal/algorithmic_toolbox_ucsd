# Usage: python3 main_script.py 1(tests) 2(parameter to tests) generator.py max_pairwise_product.py
import random
import sys
import os

#accepts the number of tests as a command line parameter
tests = int(sys.argv[1])
#accepts the parameter for the tests as a command line parameter
n = int(sys.argv[2])
data_generator_path = sys.argv[3]
input_data_storage_path ='input.txt'
output_data_storage_path ='output.txt'
source_file = sys.argv[4]

for i in range(tests):
    print(f"Test {i}")
    #run the generator generator.py with parameter n and seed i
    os.system(f"python3 {data_generator_path} {n} {i} > {input_data_storage_path}")
    #run the solution file
    os.system(f"python3 {source_file} < {input_data_storage_path} > {output_data_storage_path}")
    with open('output.txt') as f:
        output = f.read()
        print(f"output is {output}")
