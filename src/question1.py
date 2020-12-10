"""
設問1
監視ログファイルを読み込み、故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラムを作成せよ。
出力フォーマットは任意でよい。
なお、pingがタイムアウトした場合を故障とみなし、最初にタイムアウトしたときから、次にpingの応答が返るまでを故障期間とする。
"""

#故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラム
import pandas as pd
import datetime

#ログファイルの読み込み
df = pd.read_csv("./../log.csv", sep = "[,/ ]", engine='python')

#ログファイルにカラム名をつける
df.columns = ['time', 'IP', 'プレフィックス', 'ping']

#pingを確認して故障したインデックスを探す
failure_Index = df[df['ping']=='-'].index.tolist()
#print(failure_Index)

for i in failure_Index:
    
    if i < len(df.index)-1: #最後のログに対しては次の時間が分からないので無視

        #故障したpingのインデックスから時間を取り出す
        failure_time = str(df.iloc[i]['time'])
        after_failuer_time = str(df.iloc[i+1]['time']) 
    
        #時間の変換
        failure_time = datetime.datetime.strptime(failure_time, '%Y%m%d%H%M%S')
        after_failuer_time = datetime.datetime.strptime(after_failuer_time, '%Y%m%d%H%M%S')
        #print(failure_time, after_failuer_time)
        
        #応答が再開した時間と応答が消えた時間の差分を取る
        not_signal_time = after_failuer_time - failure_time
        
        server1 = df.iloc[i]['IP'] 
        server2 = df.iloc[i]['プレフィックス'] 
        
        #IPにプレフィックスを付随する
        server = str(server1) + '/' +str(server2) 
        
        print(f'故障していたサーバは{server}で、サーバの故障期間は{not_signal_time}です。')

    else:
        pass