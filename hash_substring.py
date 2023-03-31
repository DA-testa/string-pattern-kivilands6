# python3

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
                    pattern = f.readline()
                    text = f.readline()
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
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_hash = hash(pattern)
    text_hash = hash(text[:len(pattern)])
    output = []
    
    for i in range(len(text) - len(pattern) + 1):
        if text_hash == pattern_hash:
            if text[i:i+len(pattern)] == pattern:
                output.append(i)
        
        if i < len(text) - len(pattern):
            text_hash = hash(text[i+1:i+len(pattern)+1])
    
    return output
    # and return an iterable variable


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

