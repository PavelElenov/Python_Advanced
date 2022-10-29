from collections import deque


def collect_eggs(*args):
    eggs = deque(args[0])
    papers = args[1]
    boxes = 0

    while eggs and papers:
        egg = eggs.popleft()
        paper = papers.pop()

        if egg <= 0:
            papers.append(paper)
        elif egg == 13:
            new_paper = papers[0]
            papers.append(new_paper)
            papers[0] = paper
        else:
            sum = egg + paper

            if sum <= 50:
                boxes += 1
    if boxes > 0:
        print(f'Great! You filled {boxes} boxes.')
    else:
        print(f"Sorry! You couldn't fill any boxes!")
    if eggs:
        print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
    if papers:
        print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')


# eggs = [int(x) for x in input().split(', ')]
# papers = [int(x) for x in input().split(', ')]
# collect_eggs(eggs, papers)
