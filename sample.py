import random
import pprint
import re
import os
import shutil

print('hello world')

str = 'a'

print("数字を入力してください")
# ユーザーに入力させるのは文字列で返却されるためキャスト整数型に変更する必要がある
inte = int(input())

# pythonでインデントが4つらしい
if inte == 2:
    print('2です')
elif inte == 3:
    print("３desu")
else:
    print('その他です')

# pythonでは真偽値はTrue, Falseの様に先頭は大文字で記述すること
integ = 0
while True:
    print(integ)
    integ = integ + 1
    if integ == 5:
        break
print("for文")
# for文も使用できる
for i in range(3, 5):
    print(i)

# randomのモジュールを使用してみる(モジュールのインポート)
print("ランダムな数字を出力します")
print(random.randint(1,10))

# 文字列、タプルはイミュータブル(不可変)、リストはミュータブル(可変)である
# リストはいわゆる配列のことであり、タプルはイミュータブルな配列のことである
# 変更がないものはタプルを使用した方がpythonっぽいかも(実行速度も若干早くなるっぽい)

# 文字列
moji = "moji"

# リスト
ary = ["li", "arr"]

# タプル
sample_tuple = ("li", "tup")

# 参照の仕方は他と一緒

# 関数
def greeting(name):
    print("こんにちは" + name + "さん")

# return は必須
def sum(in1, in2):
    return in1 + in2

# 関数を利用する
greeting("yoru")
print(sum(5, 8))

# javaはnull, Rubyはnil, python はNoneを使用するみたい
print(None)

# 辞書型は参照渡しのものである(いわゆるMapのこと、RubyではHashというがPythonでは辞書というらしい)
# setdefaultメソッドを使用するとデータがない時に初期値を設定してくれる様になる
map = {"key": "value", 1:1}
print(map.get("key", ""))

# pprintモジュールを使用すると整形して出力してくれる(Rubyのppモジュールみたいな感じ)
pprint.pprint(map)

# 正規表現
tar = "I'm not teenager, I'm 21"
regexp = re.compile(r'[0-9]{1,3}')
res = regexp.search(tar)
print(res.group())

# 正規表現の記法はもちろん一緒
# subメソッドで置換することもできる
# compileメソッドの引数にreモジュールの定数を渡すことで正規表現検索に柔軟性を持たせることができる

# osモジュールを使用する
# カレントディレクトリを出力する
print(os.getcwd())

# 階層を渡り歩いて出力する
for name, subs, names in os.walk('../'):
    print(name)
    for sub in subs:
        print(sub)
    for of_name in names:
        print(of_name)

# shutilモジュールを使用する(shell util)
# カレントディレクトリのディスク使用量を出力する
print(shutil.disk_usage('./'))

# ファイル読み込み
path = './read_file/sample.txt'
print(open(path).read())

# ファイル書き込み(上書き)
open(path, "w").write('override')
print(open(path).read())

# 追記
open(path, "a").write('add')
print(open(path).read())