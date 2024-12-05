import sys
from collections import Counter

input = sys.argv[1] if len(sys.argv) >= 2 else 'input'
file = open(input).read().strip()

lines = file.split('\n')
left_list = []
rigth_list = Counter()
# add a counter from collections to get every times lft is eq to rht

for line in lines:
    left, rigth = line.split()
    left, rigth = int(left), int(rigth)
    left_list.append(left)
    rigth_list[rigth] += 1
# make a sum to get the info

left_list = sorted(left_list)

ans = 0

for lft in left_list:
    ans += lft*rigth_list.get(lft, 0)

print(ans)
