import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_excel(r'C:/Users/Zhuo/Desktop/即山海/茶饮数据回瑱收集表.xlsx')

print('=== 重新确认数据 ===')
print(df[['小红书昵称', '笔记曝光', '阅读量', '点赞', '收藏', '评论']].to_string())

# 互动 = 点赞 + 收藏 + 评论
df['总互动'] = df['点赞'] + df['收藏'] + df['评论']

# 互动率(基于阅读量)
df['阅读互动率'] = (df['总互动'] / df['阅读量'] * 100).round(2)

# 曝光互动率(基于曝光量)
df['曝光互动率'] = (df['总互动'] / df['笔记曝光'] * 100).round(2)

print('\n=== 互动率对比 ===')
print(df[['小红书昵称', '笔记曝光', '阅读量', '总互动', '阅读互动率', '曝光互动率']].to_string())
