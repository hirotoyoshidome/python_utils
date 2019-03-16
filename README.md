# python-tools
## Pythonで作成したツールを格納する。
* ファイル読み込み
* OpenCVサンプル


## pip
* pipを最新バージョンにする

```
python -m pip --upgrade pip
```

* opencvをインストールする

```
pip install opencv-python
```

* Pyinstallerをインストールする

```
pip install pyinstaller
```

exeファイル作成

```
pyinstaller xxx.py -onefile
```
でexeファイルを作成することができる(C言語のはずのためpython環境がなくても実行できる)
⇒かなり多くのファイルが作成されるため注意

* Requestsをインストール(リクエストを送信するモジュール)

```
pip install requests
```

* BeautifulSoup4をインストール(HTML解析モジュール)

```
pip install beautifulsoup4
```

* seleniumをインストール(ブラウザを操作)

```
pip install selenium
pip install chromedriver-binary
```
※[ダメな場合はこちらからバージョンを合わせてダウンロード](http://chromedriver.chromium.org/downloads)
