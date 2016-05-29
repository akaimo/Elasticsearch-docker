#! /bin/bash

# 初期設定
# テスト用のindexをPOST、テストデータをPUTする
# これでKibanaからデータの確認ができるようになる
curl -X POST $(docker-machine ip akaimo):9200/ldgourmet -d @data/mapping.json && \
  curl -X PUT $(docker-machine ip akaimo):9200/ldgourmet/restaurant/1 -d @data/restaurant_test.json && \
  curl -X PUT $(docker-machine ip akaimo):9200/ldgourmet/rating/1 -d @data/rating_test.json
