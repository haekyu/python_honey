import pandas as pd

print("--------------데이터 읽기-------------")
president_info = pd.read_csv('./presidents.csv', sep = ',')
print(president_info.columns)
print(president_info['President'])

print("--------------데이터 추출하기-------------")
pop_votes = list(president_info[" # of popular votes "])
print(pop_votes)

print("--------------데이터 파싱하기-------------")
def to_int(lst):
    for i in range(len(lst)):
        if lst[i] == "NA()":
            lst[i] = -1
        else:
            new_e = float(lst[i].replace(",",""))    # float string '2.3' -> float() -> int()
            lst[i] = int(new_e)
    return(lst)

output = to_int(pop_votes)
print(output)

