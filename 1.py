import base64
import requests, time, re
from urllib.parse import quote, urljoin, unquote, quote_plus
# from bs4 import BeautifulSoup
import threading
import queue, random
from datetime import datetime

def prx3(chanel_name1, file_num1):      # >> str
  try:
    # chanel_name1 = 'freeirnet'
    res1 = requests.get(f'https://t.me/s/{chanel_name1}')
    re1 = re.findall('((vmess|trojan|vless|ss|ssr):\/\/.*?)<', res1.text)
    re2 = re.findall(f'\/s\/{chanel_name1}\?before=(\d+)"', res1.text)
    str1 = ''
    for r in re1:
      if r[0] not in str1:
        if str1.count('\n') >= 50:
          break
        str1 += r[0] + '\n'
    for i in range(10):
      if str1.count('\n') >= 50:
        break
      res2 = requests.get(f"https://t.me/s/{chanel_name1}?before={re2[0]}")
      re1 = re.findall('((vmess|trojan|vless|ss|ssr):\/\/.*?)<', res2.text)
      re2 = re.findall(f'\/s\/{chanel_name1}\?before=(\d+)"', res2.text)
      for r in re1:
        if str1.count('\n') >= 50:
          break
        if r[0] not in str1:
          str1 += r[0] + '\n'
    base64_string = base64.standard_b64encode(str1.encode()).decode()
    data_up1 = {'text': str(base64_string), 'API': 'IPA1', 'File': file_num1}
    res_jig1 = requests.post('https://jigaarr24.pythonanywhere.com/xprr', data=data_up1)
    return 'https://jigaarr24.pythonanywhere.com/xprr?File={}'.format(file_num1)
  except Exception as ex:
    return str(ex)

def random_v2ray_Or_Not(fle_num1, url1 ='', rnd1= True):
  try:
    max_1 = 50
    lnk_lst1 = ['https://raw.fastgit.org/Leon406/SubCrawler/master/sub/share/vless', 'https://free.iam7.tk/vmess/sub', 
                'https://free.iam7.tk/ss/sub', 'https://free.iam7.tk/sip002/sub', 'https://free.iam7.tk/ssr/sub',
                'https://free.iam7.tk/trojan/sub', 'https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all2']
    if rnd1:
      lnk1 = random.choice(lnk_lst1)
    else:
      lnk1 = url1
    res1 = requests.get(lnk1)

    if '://' in res1.text:
      src1 = res1.text
    else:
      src1 = base64.standard_b64decode(res1.text.encode()).decode()
    
    re1 = re.findall('(vmess|trojan|ss|ssr|vless:\/\/)', src1)
    if len(re1) < 1 :
      return 'Error'
    lst1 = src1.split('\n')
    cnt = 0
    str1 = ''
    
    while cnt <= max_1 + 1:
      str0 = random.choice(lst1)
      cnt += 1
      if str0 not in str1:
        str1 += str0 + '\n'
  
    base64_string = base64.standard_b64encode(str1.encode()).decode()
    data_up1 = {'text': str(base64_string), 'API': 'IPA1', 'File': fle_num1}
    res_jig1 = requests.post('https://jigaarr24.pythonanywhere.com/xprr', data=data_up1)
    return 'https://jigaarr24.pythonanywhere.com/xprr?File={}'.format(fle_num1)

  except Exception as ex:
      return str(ex)

def vpn_fail_servers(fle_num1):
  try:
    res1 = requests.get('https://vpn.fail/free-proxy/v2ray')
    base64_string = base64.standard_b64encode(res1.text.encode()).decode()
    data_up1 = {'text': str(base64_string), 'API': 'IPA1', 'File': fle_num1}
    res_jig1 = requests.post('https://jigaarr24.pythonanywhere.com/xprr', data=data_up1)
    return 'https://jigaarr24.pythonanywhere.com/xprr?File={}'.format(fle_num1)
  except Exception as ex:
    return str(ex)

while True:
  try:
    random_v2ray_Or_Not(26)
    time.sleep(3)
    random_v2ray_Or_Not(27)
    time.sleep(3)
    random_v2ray_Or_Not(28)
    time.sleep(3)
    random_v2ray_Or_Not(29)
    time.sleep(3)
    random_v2ray_Or_Not(30)
    
    
    # break
    time.sleep(60*60*3)
  except Exception as ex:
    print(ex)
