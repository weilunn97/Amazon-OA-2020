from collections import deque


def longest_vowel_string(s: str) -> int:
    """
    Time  : O()
    Space : O(), where N = len(s)
    """
    # LET DP[I] = LONGEST VOWEL STRING ENDING AT S[I], INCLUSIVE
    vowels = set("aeiou")
    dp = deque([0] * len(s))
    dp[0] = int(s[0] in vowels)

    for i in range(1, len(dp)):
        dp[i] = 0 if s[i] not in vowels else dp[i - 1] + 1

    # ADD ANY STARTING AND ENDING VOWEL STRINGS TO OUR COUNT
    start, end = 0, 0
    while dp and dp[0] > 0: start = dp.popleft()
    while dp and dp[-1] > 0: end = max(end, dp.pop())

    # FIND THE LONGEST STRING IN THE MIDDLE
    count = max(dp) if dp else 0
    return start + count + end


if __name__ == "__main__":
    print(longest_vowel_string("aeiou") == 5)
    print(longest_vowel_string("aexaeuixaeiou") == 11)
    print(longest_vowel_string("aexaeuixaeioux") == 7)
    print(longest_vowel_string("earthproblem") == 3)
    print(longest_vowel_string("letsgosomewhere") == 2)
    print(longest_vowel_string("xaxaeixaeioux") == 5)
    print(longest_vowel_string("axaxaeixaeiouxa") == 7)
