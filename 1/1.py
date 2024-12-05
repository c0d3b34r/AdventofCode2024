import sys
# import sys to manage the input file

input = sys.argv[1] if len(sys.argv) >= 2 else 'input'
file = open(input).read().strip()
# work with the input file and generate 2 list, one left and one right


lines = file.split('\n')
left_list = []
right_list = []

# put the info in diferent arrays
for line in lines:
    left, right = line.split()
    left, right = int(left), int(right)
    left_list.append(left)
    right_list.append(right)

# order arrays
left_list = sorted(left_list)
right_list = sorted(right_list)

ans = 0

for lft, rht in zip(left_list, right_list):
    ans += abs(lft-rht)

print(ans)
