# ron_JP_sub_tools
[ron_JP_sub](https://github.com/4sumi/RoN_jp_sub)で使用するツール類です。

## 使用方法
- ダウンロードしたものをron_JP_subリポジトリの中に入れます。  
- Releasesページからダウンロードしてください。  
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
