"""
Problem B. Infinite House of Pancakes
This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the Quick-Start Guide to get started.
Small input
9 points	
Solve B-small
Large input
12 points	
Solve B-large
Problem

At the Infinite House of Pancakes, there are only finitely many pancakes, but there are infinitely many diners who would be willing to eat them! When the restaurant opens for breakfast, among the infinitely many diners, exactly D have non-empty plates; the ith of these has Pi pancakes on his or her plate. Everyone else has an empty plate.

Normally, every minute, every diner with a non-empty plate will eat one pancake from his or her plate. However, some minutes may be special. In a special minute, the head server asks for the diners' attention, chooses a diner with a non-empty plate, and carefully lifts some number of pancakes off of that diner's plate and moves those pancakes onto one other diner's (empty or non-empty) plate. No diners eat during a special minute, because it would be rude.

You are the head server on duty this morning, and it is your job to decide which minutes, if any, will be special, and which pancakes will move where. That is, every minute, you can decide to either do nothing and let the diners eat, or declare a special minute and interrupt the diners to make a single movement of one or more pancakes, as described above.

Breakfast ends when there are no more pancakes left to eat. How quickly can you make that happen?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with D, the number of diners with non-empty plates, followed by another line with D space-separated integers representing the numbers of pancakes on those diners' plates.

Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the smallest number of minutes needed to finish the breakfast.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ D ≤ 6.
1 ≤ Pi ≤ 9.
Large dataset

1 ≤ D ≤ 1000.
1 ≤ Pi ≤ 1000.
"""

#if anyone has > 1 pancakes than anyone else, move. repeat untill delta is < 1

T = int( input() )
for t in range(1,T+1):
    D = int( input() )
    P = [ int(x) for x in input().split() ]
    P.sort()
    states = set([ tuple(P) ])
    steps = 0
    while True:
        steps += 1
        new_states = set()
        done = False
        for P in states:
            Q = [ x-1 for x in P if x != 1 ]
            if Q == []:
                done = True
                break
            new_states.add( tuple(Q) )
            for i in range(len(P)):
                if P[i] > 1:
                    for j in range(1,(P[i]//2)+1):
                        Q = [ P[k] for k in range(len(P)) if k!=i ] + [ j, P[i]-j ]
                        Q.sort()
                        new_states.add( tuple(Q) )
        if done:
            print('Case #{}: {}'.format(t,steps))
            break
        states = new_states
