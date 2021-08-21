import pandas as pd

df = pd.read_csv(
    "./data.csv", 
    names=["name", "age"],
    dtype={"age": float}
)
print(df)
print()
df["age"] = [11, 6, 13, 2]

df.to_csv(
    "./data_sample.csv", 
    index=False,
    sep=","
)

# # Data Frame
# df = pd.read_csv("./data.csv")
# print(df)
# print()

# # column name 이 없는 경우
# df2 = pd.read_csv("./data.csv", header=None)
# print("df2 before")
# print(df2)
# print()

# # column 이름 바꾸기
# df2.columns = ["age", "name"]
# print("df2 after")
# print(df2)
# print()

# # column name을 직접 주고싶은 경우
# df3 = pd.read_csv(
#     "./data.csv", 
#     header=None, 
#     names=["Name", "Age"]
# )
# print(df3)
# print(df3.columns)

# df = pd.read_csv("./data.tsv", sep="\t")

