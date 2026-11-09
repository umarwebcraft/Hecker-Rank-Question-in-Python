"""
HackerRank Python - 25  Questions with Solutions
-----------------------------------------------------

"""

from collections import Counter, OrderedDict


# ---------------------------------------------------------------
# Q1. Simple Array Sum
# Given a list of integers, return the sum of its elements.
# ---------------------------------------------------------------
def q1_simple_array_sum(arr):
    return sum(arr)


# ---------------------------------------------------------------
# Q2. Compare the Triplets
# Alice and Bob each have a triplet of ratings. For each position
# the higher rating earns 1 point. Return [alice_points, bob_points].
# ---------------------------------------------------------------
def q2_compare_triplets(a, b):
    alice = sum(1 for x, y in zip(a, b) if x > y)
    bob = sum(1 for x, y in zip(a, b) if y > x)
    return [alice, bob]


# ---------------------------------------------------------------
# Q3. Diagonal Difference
# Given a square matrix, return the absolute difference between
# the sums of its two diagonals.
# ---------------------------------------------------------------
def q3_diagonal_difference(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


# ---------------------------------------------------------------
# Q4. Plus Minus
# Return the fractions of positive, negative and zero values in
# an array, each rounded to 6 decimal places.
# ---------------------------------------------------------------
def q4_plus_minus(arr):
    n = len(arr)
    positive = sum(1 for x in arr if x > 0) / n
    negative = sum(1 for x in arr if x < 0) / n
    zero = sum(1 for x in arr if x == 0) / n
    return [f"{positive:.6f}", f"{negative:.6f}", f"{zero:.6f}"]


# ---------------------------------------------------------------
# Q5. Staircase
# Given n, return a right-aligned staircase of height n made of '#'.
# ---------------------------------------------------------------
def q5_staircase(n):
    return [("#" * i).rjust(n) for i in range(1, n + 1)]


# ---------------------------------------------------------------
# Q6. Mini-Max Sum
# Given 5 integers, return the minimum and maximum sums obtained
# by adding exactly 4 of them.
# ---------------------------------------------------------------
def q6_mini_max_sum(arr):
    total = sum(arr)
    return total - max(arr), total - min(arr)


# ---------------------------------------------------------------
# Q7. Birthday Cake Candles
# Return how many candles are the tallest.
# ---------------------------------------------------------------
def q7_birthday_cake_candles(candles):
    return candles.count(max(candles))


# ---------------------------------------------------------------
# Q8. Time Conversion
# Convert a 12-hour time (e.g. 07:05:45PM) to 24-hour format.
# ---------------------------------------------------------------
def q8_time_conversion(s):
    hour = int(s[:2]) % 12
    if s[-2:] == "PM":
        hour += 12
    return f"{hour:02d}{s[2:-2]}"


# ---------------------------------------------------------------
# Q9. Lonely Integer
# Every element appears twice except one. Return the one that
# appears once (XOR cancels out pairs).
# ---------------------------------------------------------------
def q9_lonely_integer(arr):
    result = 0
    for x in arr:
        result ^= x
    return result


# ---------------------------------------------------------------
# Q10. Counting Valleys
# A hike is a string of U (up) and D (down) steps starting at sea
# level. A valley starts with a step below sea level and ends when
# returning to sea level. Count the valleys.
# ---------------------------------------------------------------
def q10_counting_valleys(path):
    level = valleys = 0
    for step in path:
        level += 1 if step == "U" else -1
        if level == 0 and step == "U":
            valleys += 1
    return valleys


# ---------------------------------------------------------------
# Q11. Sales by Match (Sock Merchant)
# Given a list of sock colors, return the number of matching pairs.
# ---------------------------------------------------------------
def q11_sock_merchant(socks):
    return sum(count // 2 for count in Counter(socks).values())


# ---------------------------------------------------------------
# Q12. Jumping on the Clouds
# Clouds are 0 (safe) or 1 (thunderhead). You can jump 1 or 2
# clouds at a time, only landing on safe ones. Return the minimum
# number of jumps to reach the last cloud.
# ---------------------------------------------------------------
def q12_jumping_on_clouds(clouds):
    i = jumps = 0
    while i < len(clouds) - 1:
        if i + 2 < len(clouds) and clouds[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps


# ---------------------------------------------------------------
# Q13. Repeated String
# A string s is repeated infinitely. Count the 'a' characters in
# the first n characters.
# ---------------------------------------------------------------
def q13_repeated_string(s, n):
    full, remainder = divmod(n, len(s))
    return s.count("a") * full + s[:remainder].count("a")


# ---------------------------------------------------------------
# Q14. Fizz Buzz
# For numbers 1..n: multiples of 3 -> Fizz, multiples of 5 -> Buzz,
# multiples of both -> FizzBuzz, otherwise the number itself.
# ---------------------------------------------------------------
def q14_fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# ---------------------------------------------------------------
# Q15. Palindrome Check
# Return True if the string reads the same forwards and backwards,
# ignoring case and non-alphanumeric characters.
# ---------------------------------------------------------------
def q15_is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


# ---------------------------------------------------------------
# Q16. Anagram Check
# Return True if two strings contain the same letters in any order.
# ---------------------------------------------------------------
def q16_is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())


# ---------------------------------------------------------------
# Q17. Pangrams
# A pangram contains every letter of the English alphabet at least
# once. Return "pangram" or "not pangram".
# ---------------------------------------------------------------
def q17_pangram(s):
    letters = set(s.lower().replace(" ", ""))
    return "pangram" if set("abcdefghijklmnopqrstuvwxyz") <= letters else "not pangram"


# ---------------------------------------------------------------
# Q18. Caesar Cipher
# Shift each letter by k positions (wrapping around), leaving
# non-letters unchanged.
# ---------------------------------------------------------------
def q18_caesar_cipher(s, k):
    k %= 26
    result = []
    for c in s:
        if c.isupper():
            result.append(chr((ord(c) - ord("A") + k) % 26 + ord("A")))
        elif c.islower():
            result.append(chr((ord(c) - ord("a") + k) % 26 + ord("a")))
        else:
            result.append(c)
    return "".join(result)


# ---------------------------------------------------------------
# Q19. Two Strings
# Return "YES" if the two strings share at least one common
# substring (a single common character is enough), else "NO".
# ---------------------------------------------------------------
def q19_two_strings(a, b):
    return "YES" if set(a) & set(b) else "NO"


# ---------------------------------------------------------------
# Q20. Capitalize!
# Capitalize the first letter of every word in a full name, keeping
# the original spacing (words starting with a digit stay unchanged).
# ---------------------------------------------------------------
def q20_capitalize(s):
    return " ".join(word.capitalize() for word in s.split(" "))


# ---------------------------------------------------------------
# Q21. Symmetric Difference
# Given two lists of integers, return the values that are in
# either list but not in both, in ascending order.
# ---------------------------------------------------------------
def q21_symmetric_difference(a, b):
    return sorted(set(a) ^ set(b))


# ---------------------------------------------------------------
# Q22. Word Order
# Given a list of words, return the number of distinct words and
# the occurrence count of each, in order of first appearance.
# ---------------------------------------------------------------
def q22_word_order(words):
    counts = OrderedDict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return len(counts), list(counts.values())


# ---------------------------------------------------------------
# Q23. Zipped!
# Given each subject's marks for all students, return every
# student's average mark.
# ---------------------------------------------------------------
def q23_zipped(subject_marks):
    return [round(sum(marks) / len(marks), 1) for marks in zip(*subject_marks)]


# ---------------------------------------------------------------
# Q24. Power - Mod Power
# Given a, b, m, return a**b and (a**b) % m.
# ---------------------------------------------------------------
def q24_mod_power(a, b, m):
    return pow(a, b), pow(a, b, m)


# ---------------------------------------------------------------
# Q25. The Minion Game
# Stuart scores with substrings starting with consonants, Kevin
# with substrings starting with vowels. Each substring scores one
# point per occurrence. Return the winner and score.
# ---------------------------------------------------------------
def q25_minion_game(s):
    vowels = "AEIOU"
    stuart = kevin = 0
    n = len(s)
    for i, c in enumerate(s):
        if c in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if stuart > kevin:
        return f"Stuart {stuart}"
    if kevin > stuart:
        return f"Kevin {kevin}"
    return "Draw"


# ---------------------------------------------------------------
# Demo runner
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("Q1 :", q1_simple_array_sum([1, 2, 3, 4, 10, 11]))
    print("Q2 :", q2_compare_triplets([5, 6, 7], [3, 6, 10]))
    print("Q3 :", q3_diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
    print("Q4 :", q4_plus_minus([-4, 3, -9, 0, 4, 1]))
    print("Q5 :")
    for line in q5_staircase(4):
        print("    " + line)
    print("Q6 :", q6_mini_max_sum([1, 2, 3, 4, 5]))
    print("Q7 :", q7_birthday_cake_candles([4, 4, 1, 3]))
    print("Q8 :", q8_time_conversion("07:05:45PM"), q8_time_conversion("12:01:00AM"))
    print("Q9 :", q9_lonely_integer([1, 2, 3, 4, 3, 2, 1]))
    print("Q10:", q10_counting_valleys("UDDDUDUU"))
    print("Q11:", q11_sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
    print("Q12:", q12_jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
    print("Q13:", q13_repeated_string("aba", 10))
    print("Q14:", q14_fizz_buzz(15))
    print("Q15:", q15_is_palindrome("A man, a plan, a canal: Panama"))
    print("Q16:", q16_is_anagram("Listen", "Silent"))
    print("Q17:", q17_pangram("We promptly judged antique ivory buckles for the next prize"))
    print("Q18:", q18_caesar_cipher("middle-Outz", 2))
    print("Q19:", q19_two_strings("hello", "world"))
    print("Q20:", q20_capitalize("1 w 2 r 3g"))
    print("Q21:", q21_symmetric_difference([2, 4, 5, 9], [2, 4, 11, 12]))
    print("Q22:", q22_word_order(["bcdef", "abcdefg", "bcde", "bcdef"]))
    print("Q23:", q23_zipped([[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]]))
    print("Q24:", q24_mod_power(3, 4, 5))
    print("Q25:", q25_minion_game("BANANA"))
