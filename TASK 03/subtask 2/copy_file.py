# Open the input file in read mode
with open('input.txt', 'r') as infile:
    # Read the contents of the input file
    content = infile.read()

# Open the output file in write mode
with open('output.txt', 'w') as outfile:
    # Write the content to the output file
    outfile.write(content)

