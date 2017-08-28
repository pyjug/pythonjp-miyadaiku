
Windows環境のPython
--------------------------------

Windowsでは、PythonはOSに添付されていないため、自分でパッケージをダウンロードして、インストールする必要があります。


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

を参照に確認できます。


:jinja:`{{ utils.enlarge_image(content.load('./download-win2.png')) }}`



パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行し、*Install now* をクリックしてインストールを開始します。

:jinja:`{{ utils.enlarge_image(content.load('./py-install1.png')) }}`




TBD chocolatey/nuget
