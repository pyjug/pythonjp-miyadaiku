
Python3のインストール
--------------------------------


Windows 環境のPython
--------------------------------

Windows環境では、PythonはOSに添付されていないので、自分でパッケージをダウンロードしてインストールします。

ここでは、Windows環境に、Pythonの公式パッケージをダウンロードしてインストールする手順を解説します。



パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.python.org/downloads/windows/ より、パッケージをダウンロードします。

特別な理由がなければ、Python 3.x.x (下図では Python 3.7.1) をクリックします。

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






.. target:: execute_py3_install

パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行します。

:jinja:`{{ utils.enlarge_image(content.load('./py-install1.png')) }}`


1. "**Add Python 3.x to PATH**" をチェックします。
2. *Install now* をクリックしてインストールを開始します。




TBD chocolatey/nuget
