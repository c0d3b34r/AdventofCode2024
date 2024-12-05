import sys

input = sys.argv[1] if len(sys.argv) >= 2 else 'input'
file = open(input).read().strip()

lines = file.split('\n')
left_list = []
rigth_list = []

for line in lines:
    left, rigth = line.split()
    left, rigth = int(left), int(rigth)
    left_list.append(left)
    rigth_list.append(rigth)

left_list = sorted(left_list)
rigth_list = sorted(rigth_list)

ans = 0

for l, r in zip(left_list, rigth_list):
    ans += abs(l-r)

print(ans)
