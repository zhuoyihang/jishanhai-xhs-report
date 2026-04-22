import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_excel(r'C:/Users/Zhuo/Desktop/即山海/茶饮数据回瑱收集表.xlsx')

print('=== 达人汇总数据 ===')
print(f'总达人数: {len(df)}')
print(f'总曝光量: {df["笔记曝光"].sum():,.0f}万')
print(f'总阅读量: {df["阅读量"].sum():,.0f}')
print(f'总点赞: {df["点赞"].sum():,.0f}')
print(f'总收藏: {df["收藏"].sum():,.0f}')
print(f'总评论: {df["评论"].sum():,.0f}')

print('\n=== 单篇平均数据 ===')
print(f'平均曝光: {df["笔记曝光"].mean():.2f}万')
print(f'平均阅读: {df["阅读量"].mean():,.0f}')
print(f'平均点赞: {df["点赞"].mean():,.1f}')
print(f'平均收藏: {df["收藏"].mean():,.1f}')
print(f'平均评论: {df["评论"].mean():,.1f}')

print('\n=== 互动率计算 ===')
df['总互动'] = df['点赞'] + df['收藏'] + df['评论']
df['互动率'] = (df['总互动'] / df['阅读量'] * 100).round(2)
print(df[['小红书昵称', '阅读量', '点赞', '收藏', '评论', '总互动', '互动率']].to_string())

print(f'\n平均互动率: {df["互动率"].mean():.2f}%')

print('\n=== 达人详情 ===')
for idx, row in df.iterrows():
    print(f"{idx+1}. {row['小红书昵称']}: 曝光{row['笔记曝光']}万, 阅读{row['阅读量']}, 点赞{row['点赞']}, 收藏{row['收藏']}, 评论{row['评论']}, 互动率{row['互动率']}%")
