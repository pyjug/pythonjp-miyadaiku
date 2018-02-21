
Python3のインストール
--------------------------------

Windows環境に、Pythonの公式パッケージをダウンロードしてインストールする手順を解説します。



パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.python.org/downloads/windows/ より、パッケージをダウンロードします。

最新パッケージとして、Python 3.x と Python 2.7.x がダウンロードできます。特別な理由がなければ、Python 3.x.x (下図では Python 3.6.4) をクリックします。

:jinja:`{{ utils.enlarge_image(content.load('./download-win-1.png')) }}`




画面の一番下に、ダウンロード可能なファイルが表示されます。

:jinja:`{{ utils.enlarge_image(content.load('./download-win2.png')) }}`


32bit版Windowsにインストールするなら

  **Windows x86 web-based installer**

64bit版なら

  **Windows x86-64 web-based installer**

をダウンロードします。

Windowsの種類が不明な場合は、

    https://support.microsoft.com/ja-jp/help/958406

を参照して確認できます。








パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行します。

:jinja:`{{ utils.enlarge_image(content.load('./py-install1.png')) }}`


1. "**Add Python 3.x to PATH**" をチェックします。
2. *Install now* をクリックしてインストールを開始します。




TBD chocolatey/nuget
