# ron_JP_sub_tools
[ron_JP_sub](https://github.com/4sumi/RoN_jp_sub)で使用するツール類です。

## 使用方法
- ダウンロードしたものをron_JP_subリポジトリの中に入れます。  
Releasesページからダウンロードしてください。
- リポジトリ内にフォルダを置いてください。  
こう言ったファイル構成になればokです。
> ./  
> ├ VO/  
> └ automatas/  
- automatas/内の使いたい物を実行すればokです。  
実行結果は概ね破壊的であるため、不安であれば事前にバックアップを取るなりしてください。
## 各種スクリプトの内容
### automata1
VOフォルダ内の各フォルダにsub_jp.csvファイルがあるかをチェックします。  
excludes.txtに名前が書かれたフォルダは無視します。  
実行結果はno_JP_sub_list.txtに出力されます。
### automata2
VOフォルダ内の各フォルダにおいて、sub_en.csvの内容の順番を基準にして、sub_jp.csvの内容の順番を入れ替えます。  
excludes.txt、no_JP_sub_list.txtに名前が書かれたフォルダは無視します。  
実行すると全てのsub_jp.csvに影響します。
### automata3
使用しません。別ブランチ(en_sort)に隔離してあります。  
VOフォルダ内の各フォルダのsub_en.csvの内容の順番を各接頭辞ごとにソートします。  
実行すると全てのsub_en.csvに影響します。sub_en.csvファイルは、元プロジェクトのgitignore対象であることに注意してください。
### automata4
VOの各フォルダの、sub_ja.csvをsub_jp.csvにリネームします  
Home invasionリリースにより字幕が表示されなくなった問題に対処します  
ReadyOrNot/Contents/ ディレクトリの中に配置して実行してください
### automata5
VOの各フォルダのsub_jp.csv、sub_en.csvのみのコピーを作成します  
実行結果はautomatas/フォルダ内にVOという名前で出力されます
### automata6
sub_en、sub_jp間の齟齬を検出しリストアップします  
sub_enとsub_jpの行数の齟齬、sub_enにあるがsub_jpに無いKeyが対象です  
出力結果はコンソールに表示されます
