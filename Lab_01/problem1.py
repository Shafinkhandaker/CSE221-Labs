def read():
    file = open('input.txt', 'r')
    nums, words = [], []
    for line in file:
        number, string = line.split(' ')
        string = string[0: len(string) - 1]
        try:
            nums.append(int(number))
        except:
            nums.append(float(number))
        words.append(string)
    file.close()
    return nums, words


def write(nums, words):
    output_file = open("output.txt", "w")
    for i in range(len(nums)):
        new_line = ""
        new_line += f"{nums[i]} has {parity(nums[i])} parity and {words[i]} is "
        if isPalindrome(words[i]):
            new_line += "a palindrome"
        else:
            new_line += "not a palindrome"
        output_file.write(new_line + "\n")
    output_file.close()
    record_file = open("record.txt", "w")
    for i in range(len(percentages)):
        new_line2 = ""
        new_line2 += f"{percentages[i]} "
        record_file.write(new_line2 + "\n")
    record_file.close()


def parity(N):
    if type(N) == float:
        return "no"
    elif N % 2 == 0:
        return "even"
    else:
        return "odd"


def isPalindrome(word):
    if len(word) == None:
        return False
    n = len(word)
    for i in range(0, n//2):
        if word[i] != word[n-1-i]:
            return False
    return True


# counting the number of how many even parity,odd parity,no parity ,palindrome and non palindrome
count_even_parity = 0
count_odd_parity = 0
count_no_parity = 0
count_palindrome = 0
count_not_palindrome = 0

nums, words = read()
for num in nums:
    if parity(num) == "odd":
        count_odd_parity += 1
    elif parity(num) == "even":
        count_even_parity += 1
    else:
        count_no_parity += 1

for word in words:
    if isPalindrome(word):
        count_palindrome += 1
    else:
        count_not_palindrome += 1


# compute parcentages
percentages = []
percentages.append(
    f"Percentage of odd parity: {(count_odd_parity/len(nums)) * 100}%")
percentages.append(
    f"Percentage of even parity: {(count_even_parity/len(nums)) * 100}%")
percentages.append(
    f"Percentage of no parity:{count_no_parity/len(nums)* 100}%")
percentages.append(
    f"Percentage of palindrome:{(count_palindrome/len(nums)) * 100}%")
percentages.append(
    f"Percentage of non-palindrome:{(count_not_palindrome/len(nums)) * 100}%")
write(nums, words)
