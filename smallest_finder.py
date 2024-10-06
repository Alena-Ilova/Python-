

def find_two_smallest(int_list):
    
    if len(int_list) < 2:
        raise ValueError("List must contain at least two integers.")


    unique_values = list(set(int_list))
    unique_values.sort()

    if len(unique_values) < 2:
        raise ValueError("List must contain at least two unique integers.")

        
    return unique_values[0], unique_values[1]