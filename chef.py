
def main():
    no_tests = input()
    test_case = []
    for i in range(no_tests):
        test_case.append(input())
 
    for i in range(no_tests):
        print find_height(test_case[i])
 
if __name__ == '__main__':
    main()


    -----

def count4(n):
    count = 0
    for i in range(len(str("n"))):
        if i == "4":
            count += 1
    print count

cor::
t = input()
for i in range(len(str(n))):
    lucky_four = 0
    for digit in n:
        if digit == '4':
            lucky_four+=1
    print lucky_four

def reverse(text):
    r_text = ''
    index = len(text) - 1

    while index >= 0:
        r_text += text[index]
        index -= 1
        
'''
quad formula solved for n, gauss eq:
s = n(n+1)/2 
n = (-1 +-  sqrt ( 1 + 8s ) ) / 2
'''

"""

It's possible for all the digits displayed on a digital clock in the hours:minutes format to be identical. The time shown above (3:33) is an example of such a situation. Other examples are 2:2 and 1:11. Note that the digits of 33:33 are identical, but it is not a valid time on a usual digital clock.
The above example was for a usual 24-hour format digital clock. Let's consider a more general clock, where an hour lasts M minutes and a day lasts H hours (therefore, the clock can show any number of hours between 0 and H-1, inclusive, and any number of minutes between 0 and M-1, inclusive). Both the hours and the minutes are shown without leading zeroes in decimal notation and their separator (e.g., ':') doesn't matter.
Can you tell how many minutes during a day will the digital clock have identical digits displayed on it?
Input

The first line of the input contains an integer T - the number of test cases.
Each of the next T lines contains two space-separated integers H and M for one test case.
Output

For each test case, output a single line corresponding to the answer of the problem.
Constraints

1 ≤ T ≤ 50
1 ≤ H, M ≤ 100
Example

Input:
6
24 60
34 50
10 11
10 12
11 11
1 1

Output:
19
20
10
11
10
1

"""
"""
-make every time into a list
-check each list that every item is the same as every other item
"""

4589
5555
x = [4, 4, 4, 4]
x = [4, 4, 5, 4]

# for i in range(len(x)):
#     if x[0]

def make_times(x, y):
    times = []
    all_times = []
    for i in range y:
        times.append y

counter = 0
if all_same(itmes):
    counter += 1

def all_same(items):
    return all(x == items[0] for x in items)
    
def check_connectivity(reference):
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False
