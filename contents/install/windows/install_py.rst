公式パッケージのインストール
-----------------------------------


パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.python.org/downloads/windows/ より、パッケージをダウンロードします。

最新パッケージとして、Python 3.x と Python 2.7.x がダウンロードできます。特別な理由がなければ、Python 3.x (下図では Python 3.6.2) をクリックします。


:jinja:`{{ utils.enlarge_image(content.load('./download-win.png')) }}`


画面の一番下に、ダウンロード可能なファイルが表示されます。インストールするWindowsが32bit版なら

  **Windows x86 web-based installer**

64bit版なら

  **Windows x86-64 web-based installer**

をインストールしてください。


Windowsの種類が不明な場合は、

    https://support.microsoft.com/ja-jp/help/958406

を参照に確認してください。


:jinja:`{{ utils.enlarge_image(content.load('./download-win2.png')) }}`



パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行し、*Install now* をクリックしてインストールを開始します。

:jinja:`{{ utils.enlarge_image(content.load('./py-install1.png')) }}`




TBD chocolatey/nuget

Build Tools for Visual Studio 2017
++++++++++++++++++++++++++++++++++++++++++++++++++

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
