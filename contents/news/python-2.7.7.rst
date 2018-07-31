.. article::
   :date: 2014-06-02 14:00:00

Python 2.7.7 リリース
=============================




Python 2.7.7 の正式版 `Python 2.7.7 <https://www.python.org/download/releases/2.7.7/>`_ が公開されました。このリリースでの修正内容は、`Misc/Newsファイル <http://hg.python.org/cpython/raw-file/f89216059edf/Misc/NEWS>`_ で確認できます。

このリリースでは、セキュリティホールとなる可能性がある、潜在的な問題を2件修正しています。一つは `jsonモジュール <https://docs.python.org/ja/2.7/library/json.html>`_ の `JSONDecoder` による不正なメモリアクセスで、もう一件は `stringモジュール <https://docs.python.org/ja/2.7/library/string.html>`_ から呼び出される、`strop` モジュールの不具合です。
