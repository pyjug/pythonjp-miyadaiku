Cコンパイラのインストール
-----------------------------------




Pythonの拡張モジュールをインストールする際に、Cコンパイラが必要となる場合があります。

WindowsではCコンパイラが添付されていないため、別途インストールする必要があります。Python3.6の場合は、

  https://www.visualstudio.com/ja/downloads



より、

    **Build Tools for Visual Studio 2017**

をダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download-vstools.png')) }}`


ダウンロードしたインストーラを実行し、

    **Visual C++ Build Tools 2017**

をチェックして **インストール** ボタンをクリックします。

:jinja:`{{ utils.enlarge_image(content.load('./install-vc.png')) }}`
