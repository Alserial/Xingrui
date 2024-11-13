import re
from datetime import datetime

def reg_search(text, regex_list):
    results = {}
    
    for key, patterns in regex_list.items():
        for pattern in patterns:
            matches = re.findall(pattern, text)
            
            if matches:
                if len(matches) == 1:
                    results[key] = matches[0]
                else:
                    results[key] = matches
                break
                
    return results

# Test
text = """
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债
券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
日至 2027 年 6 月 1 日止。
"""

# Input
regex_list = {
    '标的证券': [r'\b(\d{6}\.SH)\b'],
    '换股期限': [r'(\d{4}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日)', r'(\d{4})年(\d{1,2})月(\d{1,2})日']  
}

result = reg_search(text, regex_list)
if '换股期限' in result:
    formatted_dates = []
    for date_str in result['换股期限']:
        try:
            formatted_date = datetime.strptime(date_str.replace(" ", ""), "%Y年%m月%d日").strftime("%Y-%m-%d")
            formatted_dates.append(formatted_date)
        except ValueError:
            continue
    result['换股期限'] = formatted_dates

print("格式化后的结果：", result)
