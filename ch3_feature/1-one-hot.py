# санг импортлох
import pandas as pd
# [13]
text = "Мөрөөдлөө бүтэн биелэгдтэл сайн гүй"

# pd.get_dummies үг бүрийг багана болгон хувиргаж,
# тухайн үгийн байгааг 1, байхгүйг 0-оор тэмдэглэнэ
one_hot_df = pd.get_dummies(text.split())
print(one_hot_df)

# Гаралт:
#    Мөрөөдлөө  биелэгдтэл  бүтэн    гүй   сайн
# 0       True       False  False  False  False
# 1      False       False   True  False  False
# 2      False        True  False  False  False
# 3      False       False  False  False   True
# 4      False       False  False   True  False

one_hot_df = pd.get_dummies(text.split()).astype(int)
print(one_hot_df)

# Гаралт: 
#    Мөрөөдлөө  биелэгдтэл  бүтэн  гүй  сайн
# 0          1           0      0    0     0
# 1          0           0      1    0     0
# 2          0           1      0    0     0
# 3          0           0      0    0     1
# 4          0           0      0    1     0
