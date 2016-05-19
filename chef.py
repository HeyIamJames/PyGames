
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
