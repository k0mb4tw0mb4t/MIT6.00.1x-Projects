
def longest_alphabetical_substring_finder():
    string = input("enter string to find longest alphabetical substring> ")

    
    longest_so_far = [string[0],]  # keep track of longest alpha substring so far
    longest_overall = [string[0],]  # keep track of longest overall alphabetical substring

    for alpha_char in range(len(string) - 1):  # avoid range error since we scan one index ahead of current index
        if string[alpha_char + 1] >= string[alpha_char]:  
            longest_so_far.append(string[alpha_char + 1])  
            if len(longest_so_far) > len(longest_overall):
                longest_overall = longest_so_far
        else:
            longest_so_far = [string[alpha_char + 1],]

    longest_alphabetical_substring = ''.join(longest_overall)
    print("Longest substring in alphabetical order is: ", longest_alphabetical_substring)



        
        
    
                

