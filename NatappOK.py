import pandas as pd
from bs4 import BeautifulSoup
import requests
from io import StringIO

# 指定要讀取的 URL
url = 'http://security.netapp.com/advisory/'

# 設置請求標頭
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 發送GET請求
response = requests.get(url, headers=headers)

# 檢查請求狀態碼
if response.status_code == 200:
    # 解析HTML內容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有表格
    tables = soup.find_all('table')

    # 初始化一個空的 DataFrame 來存儲所有表格數據
    all_data = pd.DataFrame()

    # 遍歷每個表格
    for table in tables:
        # 讀取表格數據
        html = str(table)
        df = pd.read_html(StringIO(html))[0]

        # 將數據追加到總的 DataFrame 中
        all_data = pd.concat([all_data, df], ignore_index=True)

    # 顯示讀取的 DataFrame
    print(all_data)

    # 寫入 Excel 檔案
    all_data.to_excel('./data.xlsx', index=False)
else:
    print("請求失敗")