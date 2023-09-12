#本日受災戶:稷下書院- 網絡小說閱讀網

#導入解析網頁的庫
import requests
from bs4 import BeautifulSoup
import re

#最基礎的url,後面換網頁(章節),變化都靠它了
#如果要用的話記得自己依樣畫葫蘆改一下就行了
base_url = 'https://www.novel543.com/0321218234/8090_{}.html'

#要爬的章節,start為開始章節,end為結束章節
start_page = 1
end_page = 3

#小說內容存這邊
novel_text = ""

#現在爬蟲爬到第幾章節
now=1

# 循環遍歷範圍 page
for page in range(start_page, end_page + 1):
    # 根據現在的變數page改url
    url = base_url.format(page)

    #方便看現在進度
    print("目前爬到了第 ",now," 章節")
    now +=1

    # 請求網頁內容
    response = requests.get(url)

    if response.status_code == 200:
        # 解析頁面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 小說內容的位置 soup.find(左鍵檢查小說內文就能找到)
        novel_content = soup.find('div', class_='content py-5')

        # 提取文本
        if novel_content:
            # 找到所有的 <br> 標籤
            br_tags = novel_content.find_all('br')

            # 遍歷每個 <br> 標籤後換行
            for br in br_tags:
                br.insert_after("\n")

            # 取得文本內容
            content_text = novel_content.get_text()

            # 把重複換行換成單個換行
            content_text = re.sub(r'\n+', '\n', content_text)

            # 開始時先換行
            novel_text += "\n" + content_text + "\n"

# 把內容存到文件（在 E:\ 電腦下載位置）
file_path = r'E:\電腦下載位置\我天命大反派.txt'  #文件目錄 #名字.txt
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(novel_text)

#成功時返回
print(f"小說已保存到 {file_path}")
