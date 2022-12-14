numbers = [int(x) for x in input().split()]


def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0
    for v in args:
        if v > 0:
            positive_sum += v
        else:
            negative_sum += v
    return positive_sum, negative_sum


positive_sum, negative_sum = find_positive_and_negative_sums(*numbers)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
