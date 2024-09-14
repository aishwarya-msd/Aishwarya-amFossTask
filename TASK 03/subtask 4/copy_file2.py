def print_diamond_to_string(n):
    """Generates a diamond pattern of asterisks and returns it as a string."""
    diamond_str = []
    
    # Print the upper half of the diamond
    for i in range(n):
        # Create each row with leading spaces and asterisks
        line = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        diamond_str.append(line)
    
    # Print the lower half of the diamond
    for i in range(n - 2, -1, -1):
        line = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        diamond_str.append(line)
    
    return '\n'.join(diamond_str)

def main():
    try:
        # Read the number of rows from input.txt
        with open('input.txt', 'r') as infile:
            n = int(infile.read().strip())
        
        if n <= 0:
            print("Please enter a positive integer in input.txt.")
            return
        
        # Generate the diamond pattern
        diamond_pattern = print_diamond_to_string(n)
        
        # Write the diamond pattern to output.txt
        with open('output.txt', 'w') as outfile:
            outfile.write(diamond_pattern)
        
        print("Diamond pattern has been written to output.txt.")
    
    except ValueError:
        print("Invalid number in input.txt. Please ensure it contains a valid integer.")
    except FileNotFoundError:
        print("input.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

