import matplotlib
matplotlib.rcParams['font.family']
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

import pymysql
import matplotlib.pyplot as plt

font_name = fm.FontProperties(fname = 'C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family = font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

conn = pymysql.connect(host = 'skuser57-instance.ctxvewe48g71.us-west-2.rds.amazonaws.com',port = 3306, user = 'admin', password = 'pax5022kr', db = 'mydb')
curs = conn.cursor()

sql = "SELECT * FROM my_topic_stock"
curs.execute(sql)
rows = curs.fetchall()

df  = pd.read_sql(sql, conn)


df['price'] = df['price']

num = input('현재가를 가장 높은 순서대로 보여드립니다. 보고 싶은 주식의 갯수를 입력하세요 ( *20개가 넘는 데이터를 출력할 시 글자가 잘 보이지 않을 수 있습니다* ): ')

df1 = df.sort_values(by=['price'], axis=0, ascending=False).head(int(num))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(df1['title'],df1['price'])
ax.set_xlabel('title')
ax.set_ylabel('price')
ax.set_title('현재가')
plt.xticks(rotation=45, fontsize = 5)
#plt.show()
plt.savefig('price.png')

df['volume'] = df['volume']

num = input('거래량을 가장 높은 순서대로 보여드립니다. 보고 싶은 주식의 갯수를 입력하세요 ( *20개가 넘는 데이터를 출력할 시 글자가 잘 보이지 않을 수 있습니다* ): ')
df2 = df.sort_values(by=['volume'], axis=0, ascending=False).head(int(num))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(df2['title'],df2['volume'])
ax.set_xlabel('title')
ax.set_ylabel('volume')
ax.set_title('거래량')
plt.xticks(rotation=45, fontsize = 5)
#plt.show()
plt.savefig('volume.png')

df['payment'] = df['payment']

num = input('거래대금을 가장 높은 순서대로 보여드립니다. 보고 싶은 주식의 갯수를 입력하세요 ( *20개가 넘는 데이터를 출력할 시 글자가 잘 보이지 않을 수 있습니다* ): ')
df3 = df.sort_values(by=['payment'], axis=0, ascending=False).head(int(num))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(df3['title'],df3['payment'])
ax.set_xlabel('title')
ax.set_ylabel('payment')
ax.set_title('거래대금')
plt.xticks(rotation=45, fontsize = 5)
#plt.show()
plt.savefig('payment.png')

df['buy'] = df['buy']

num = input('매수호가를 가장 높은 순서대로 보여드립니다. 보고 싶은 주식의 갯수를 입력하세요 ( *20개가 넘는 데이터를 출력할 시 글자가 잘 보이지 않을 수 있습니다* ): ')
df4 = df.sort_values(by=['buy'], axis=0, ascending=False).head(int(num))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(df4['title'],df4['buy'])
ax.set_xlabel('title')
ax.set_ylabel('buy')
ax.set_title('매수호가')
plt.xticks(rotation=45, fontsize = 5)
#plt.show()
plt.savefig('buy.png')

df['sell'] = df['sell']

num = input('매도호가를 가장 높은 순서대로 보여드립니다. 보고 싶은 주식의 갯수를 입력하세요 ( *20개가 넘는 데이터를 출력할 시 글자가 잘 보이지 않을 수 있습니다* ): ')
df5 = df.sort_values(by=['sell'], axis=0, ascending=False).head(int(num))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
ax.plot(df5['title'],df5['sell'])
ax.set_xlabel('title')
ax.set_ylabel('sell')
ax.set_title('매도호가')
plt.xticks(rotation=45, fontsize = 5)
#plt.show()
plt.savefig('sell.png')
