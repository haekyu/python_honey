def get_ranks(score_lst):
    rank_lst = []
    for e in score_lst:
        rank = 1
        for i in range(len(score_lst)):
            if e < score_lst[i]:
                rank = rank + 1
        rank_lst.append(rank)
    return rank_lst

name_lst = ['일', '이', '삼', '사', '오']
score_lst = [30, 42, 51, 18, 23]

ranks = get_ranks(score_lst)
#print(ranks)

i = 0
for name, score, rank in zip(name_lst, score_lst, ranks):
    print('{}번째 학생: 이름={}, 점수={}, 등수={}등'.format(i, name, score, rank))
    i = i + 1

i = 0
for i, (name, score, rank) in enumerate(zip(name_lst, score_lst, ranks)):
    print('{}번째 학생: 이름={}, 점수={}, 등수={}등'.format(i, name, score, rank))
