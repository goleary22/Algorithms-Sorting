

#Split the input lines into the seperate criterias





if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        number_of_lines = data_file.readline() #read first line
        lines = data_file.readlines() #read the rest of the lines

    # Actually do the work
    #print(summation(lines))