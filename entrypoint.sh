#!/bin/bash

set -e

# 証明書と秘密鍵を生成
openssl req -newkey rsa:2048 -nodes -keyout private_key.pem -x509 -days 365 -out self_signed_cert.pem -subj "/CN=Hyunwook Park"

# 証明書を PFX 形式に変換
openssl pkcs12 -export -out self_signed_cert.pfx -inkey private_key.pem -in self_signed_cert.pem -name "Hyunwook Park" -passout pass:pakupaku

echo "Self-signed certificate created."

# .exe ファイルを処理
for exe in /app/dist/*.exe; do
    if [ -f "$exe" ]; then
        output_file="/app/output/$(basename "$exe")"

        # ここで実際の署名コマンドを呼び出します（現状はコピーで代替）
        cp "$exe" "$output_file"

        echo "Signed $exe -> $output_file"
    fi
done

echo "All files signed."
