Cコンパイラのインストール
-----------------------------------

Pythonの拡張モジュールをインストールする際に、Cコンパイラが必要となる場合があります。WindowsではCコンパイラが添付されていないため、必要に応じて別途インストールします。


Python3.6/3.7の場合は、

  https://www.visualstudio.com/ja/downloads


を開いて ``Tools for Visual Studio 2017`` をクリックし、

:jinja:`{{ utils.enlarge_image(content.load('./download-vstools.png')) }}`


より、

    **Tools for Visual Studio 2017**

をダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download-vstools2.png')) }}`


ダウンロードしたインストーラを実行し、

    **Visual C++ Build Tools 2017**

を選択して **インストール** ボタンをクリックします。

:jinja:`{{ utils.enlarge_image(content.load('./install-vc.png')) }}`
