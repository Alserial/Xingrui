import requests
import pandas as pd

# 请求URL
url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"

# 请求头
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "AlteonP10=AsleSyw/F6wDLyskafm7aA$$; apache=bbfde8c184f3e1c6074ffab28a313c87; ags=b168c5dd63e5c0bebdd4fb78b2b4704a; _ulta_id.ECM-Prod.ccc4=a5f2133ce14939db; _ulta_ses.ECM-Prod.ccc4=df373a887526545c; lss=fd9e664ef34511dcdc4a51a4e8d84abc; _ulta_id.CM-Prod.ccc4=74e624ce08d00792; _ulta_ses.CM-Prod.ccc4=5733aad22a9bc711; isLogin=0",
    "Host": "iftp.chinamoney.com.cn",
    "Origin": "https://iftp.chinamoney.com.cn",
    "Referer": "https://iftp.chinamoney.com.cn/english/bdInfo/",
    "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# 请求参数
data = {
    "pageNo": 1,
    "pageSize": 15,
    "isin": "",
    "bondCode": "",
    "issueEnty": "",
    "bondType": 100001,
    "couponType": "",
    "issueYear": 2023,
    "rtngShrt": "",
    "bondSpclPrjctVrty": ""
}

# 存储数据
all_data = []

# 抓取所有页
while True:
    # 发送请求
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        print("请求失败，状态码：", response.status_code)
        break

    # 解析数据
    response_json = response.json()
    result_list = response_json.get('data', {}).get('resultList', [])
    
    if not result_list:
        print("没有更多数据了。")
        break

    all_data.extend(result_list)

    if response_json.get('data', {}).get('nextpg') == 0:
        print("已到达最后一页。")
        break
    
    # 下一页
    data['pageNo'] += 1

# 保存为 CSV
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv("bond_data.csv", index=False, encoding="utf-8-sig")
    print("数据已保存到 bond_data.csv")
else:
    print("没有抓取到数据。")
