

from smallest_finder import find_two_smallest
import data_lists

results = []


for name, int_list in vars(data_lists).items():
    if isinstance(int_list, list):  
        try:
            smallest_two = find_two_smallest(int_list)
            results.append(f"The two smallest numbers in {name} are: {smallest_two}")
        except ValueError as ve:
            results.append(f"Error for {name}: {ve}")


with open("result.txt", "w") as file:
    for result in results:
        file.write(result + "\n")

print("Results have been saved to result.txt.")