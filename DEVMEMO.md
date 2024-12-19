## 動作環境準備

```console
python -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## exeファイル生成

```console
pyinstaller --onefile --windowed --name capture_with_countdown_0.1 capture_with_countdown.py
```

## exeに署名

```console
docker-compose up
docker-compose down --rmi all -v
```