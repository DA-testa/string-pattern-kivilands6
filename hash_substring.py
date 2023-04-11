# Edzus Kivilands 221RDB339
# python3
#testing git

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_text = input()
    if 'F' in input_text:
        input_file = input()
        input_file = "tests/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    pattern = f.readline().rstrip()
                    text = f.readline().rstrip()
                    print(pattern,text)
                    return pattern, text

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        pattern = input()
        text = input()
        return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    p_hash = sum(ord(pattern[i]) * pow(101, i) for i in range(p)) # Calculate pattern hash
    t_hash = sum(ord(text[i]) * pow(101, i) for i in range(p)) # Calculate hash of the first segment of text
    output = []
    
    for i in range(t - p + 1):
        if p_hash == t_hash: # Compare the hash values
            if text[i:i+p] == pattern: # If hash values are same, then check if the pattern actually matches
                output.append(i)
                
        if i < t - p: # Calculate hash for next segment of text
            t_hash = t_hash - ord(text[i])
            t_hash = t_hash // 101
            t_hash += ord(text[i+p]) * pow(101, p-1)
            
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

