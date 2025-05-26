#静岡市の道路の規制区間を確認できる。東名高速を通るときに便利。


import requests

API_URL  = "https://openapi.city.shizuoka.jp/opendataapi/servicepoint/PreReg" #ベース GETで取得 PreRegで道路規制区間の検索になるが、disasterで災害状況も確認できる

#基本形はこれ https://openapi.city.shizuoka.jp/opendataapi/servicepoint/{サービスポイント名}

params = {

    "extent":"35,138.4,35.05,138.48" #北緯35度と北緯35.05度の緯線および東経138.4度と東経138.48度の経線に囲まれた範囲であるかないか
    #radiusで円形範囲で検索することもできる
    #radius=50&lat=34.975&lng=138.382 //東経138.382、北緯34.975の地点から半径50メートル以内

}

response = requests.get(API_URL, params=params)　
# Process the response
data = response.json()
print(data)

#"今は"JSONでこう返ってくる↓
#{'Success': True, 'Data': {'features': [], 'type': 'FeatureCollection'}, 'Error': None, 'TotalRecord': 0, 'TotalPage': 0, 'PageRecord': 30}
