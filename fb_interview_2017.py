'''
Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!
--------------------------------------------------------
Write a function that takes an input string and an alphabet, and returns the shortest substring of the input which contains every letter of the alphabet at least once.

Example:

Input:  "aaccbc"
Alphabet: "abc"
Output:  "accb"
--------------------------------------------------------
'''

output_arr = []


def pangram_solver(input_str, alphabet):
    pangram_helper(input_str, alphabet)
    print output_arr
    sorted_arr = sorted(output_arr, key=len)
    return sorted_arr[0]


def pangram_helper(input_str, alphabet):
    if not input_str:
        return None
    alpha_dict = {}
    for i in range(0, len(input_str)):
        a = input_str[i]
        if a in alphabet:
            if a in alpha_dict.keys():
                alpha_dict[a] += 1
            else:
                alpha_dict[a] = 1
    if len(alpha_dict.keys()) == len(alphabet) and input_str not in output_arr:
        output_arr.append(input_str)
        pangram_helper(input_str[1:], alphabet)
        pangram_helper(input_str[:-1], alphabet)

if __name__ == '__main__':
    print pangram_solver("aaccbc", "abc")
