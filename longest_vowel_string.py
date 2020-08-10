from collections import deque


def longest_vowel_string(s: str) -> int:
    """
    Time  : O()
    Space : O(), where N = len(s)
    """
    s = deque(list(s))
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    # POP FRONT AND BACK
    while s and s[0] in vowels: count += int(bool(s.popleft()))
    while s and s[-1] in vowels: count += int(bool(s.pop()))

    # GET THE LARGEST CONSECUTIVE VOWEL COUNT
    longest = 0
    length = 0
    for char in s:
        if char in vowels:
            length += 1
        else:
            longest = max(longest, length)
            length = 0
    return count + longest


if __name__ == "__main__":
    print(longest_vowel_string("aeiou") == 5)
    print(longest_vowel_string("aexaeuixaeiou") == 11)
    print(longest_vowel_string("aexaeuixaeioux") == 7)
    print(longest_vowel_string("earthproblem") == 3)
    print(longest_vowel_string("letsgosomewhere") == 2)
    print(longest_vowel_string("xaxaeixaeioux") == 5)
    print(longest_vowel_string("axaxaeixaeiouxa") == 7)
