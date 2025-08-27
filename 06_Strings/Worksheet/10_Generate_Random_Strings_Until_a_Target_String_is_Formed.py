'''Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary)'''

import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_until_target(target):
    attempts = 0
    while True:
        attempts += 1
        guess = generate_random_string(len(target))
        if guess == target:
            print(f"Target '{target}' matched after {attempts} attempts.")
            break

generate_until_target("abc")