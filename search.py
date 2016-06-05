import json
import requests

# ElasticsearchのIP
url = "http://192.168.99.101:9200"

# ユーザからのクエリ
user_query = input("input query: ")

# クエリをちょっと書き換え
query = {
    "query": {
        "simple_query_string": {
            "query": user_query,
            "fields": ["name", "name_kana"],
            "default_operator": "and"
        }
    }
}

# ESにコンテンツ検索クエリを投げる
r = requests.post(url+'/ldgourmet/restaurant/_search', data=json.dumps(query))
res = r.json()

# ESの結果をユーザに返す
hits = map(lambda hit: hit['_source']['name'], res['hits']['hits'])
print(list(hits))  # ありがちなPython3対応...
