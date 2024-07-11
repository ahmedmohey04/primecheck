import csv

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Reading from the input CSV file
input_file = 'input_numbers.csv'
output_file = 'output_results.csv'

with open(input_file, mode='r') as file:
    reader = csv.reader(file)
    numbers = [int(row[0]) for row in reader]

# Processing numbers and checking if they are prime
results = []
for num in numbers:
    if is_prime(num):
        results.append([num, "is a prime number"])
    else:
        results.append([num, "is not a prime number"])

# Writing the results to the output CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Number", "Result"])
    writer.writerows(results)

print(f"Results have been written to {output_file}")
