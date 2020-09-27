import requests

from lxml import etree
def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
            "cookie":"hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=sjA56zcJ9u%2F8HHfzWeGenkosE0sTJKOlrlE3PMUsXa4T4ucIGh7utUvQoTVW1UqNtT0z0zaGdAm6xBhWgTSwhQ%3D%3D; miid=202266272065909521; tracknick=zhongkangtb; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; cna=Q8BkEwdNjwACASrHh4ywLeIq; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=495b1ae6d656f25318235b91cf412b1a; cookie2=1e352b66734f3c1b206751d815d354ed; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _tb_token_=e53945567abe7; mt=ci%3D-1_1; JSESSIONID=694C8BC65EFD5DCBCB5BD0FFFF0A8D54; isg=BOXl0kSA1LkPtzG_hnKhESi05qHfioaHPErXpufJqJwr_gRwr3FyhCfciCItfrFs; l=cBIvTKdVvmfdhDbzBOfZVuI81hQtoQ908sPzw4swkICP9wCH50UfWZeIGwLMCnGVK6SDR3Sq8BObB0LNuyCqJxpsw3k_J_f.."
        }
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")
        #'http://poedb.tw/tw/unique.php?n=Hands_of_the_High_Templar'
url = 'https://poedb.tw/tw/unique.php?l=1'
html = etree.HTML(getHTMLText(url))

res = html.xpath('''//*[@class="collapse show"]/div/table/tbody//tr/td[2]/a/text()''')
中文列表 = [i.split(' ')[0] for i in res]
res1 = html.xpath('''//*[@class="collapse show"]/div/table/tbody//tr/td[2]/span[@class="item_description"]/text()''')
英文列表 = [i for i in res1]
结果 = [{'ch_name':i,'en_name':j} for i,j in zip(中文列表,英文列表)]
with open("物品.txt", 'a', encoding='utf-8') as f:
    f.write(str(结果))