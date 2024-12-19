FROM ubuntu:20.04

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    openssl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# entrypoint.sh をコピー
COPY entrypoint.sh /app/entrypoint.sh

# 実行権限を付与
RUN chmod +x /app/entrypoint.sh
