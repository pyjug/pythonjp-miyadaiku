
Windows 環境のPython
--------------------------------

Windows環境では、Python公式サイトで64bit版Windows用と32bit版Windows用のパッケージが公開されています。Windowsの種類が不明な場合は、

    https://support.microsoft.com/ja-jp/help/958406

を参照して確認してください。




パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.python.org/downloads より、パッケージをダウンロードします。利用するPythonのバージョンを選択します。特別な理由がなければ、最新版のPython (下図では Python 3.7.1) をクリックします。


.. CAUTION::

   Windows上のプラウザからダウンロードすると、上部に ``Download Python 3.7.1`` のようなボタンが表示されますが、これは使用しないでください。



:jinja:`{{ utils.enlarge_image(content.load('./download-win-1.png')) }}`




画面の一番下に、ダウンロード可能なファイルが表示されます。

:jinja:`{{ utils.enlarge_image(content.load('./download-win2.png')) }}`


64bit版Windowsにインストールするなら

  **Windows x86-64 executable installer**

32bit版なら

  **Windows x86 executable installer**


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





その他の作業
=========================

:jinja:`{{ content.link_to('./install_vstools2017.rst') }}` (オプション)

   Pythonの拡張パッケージをインストールするときに、Cコンパイラが必要となる場合があります。

   Windows環境では、Cコンパイラが添付されていないので、必要に応じてインストールします。

:jinja:`{{ content.link_to('./install_py2.7.rst') }}` (オプション)

   Python 2.7が必要であれば、公式パッケージをダウンロードしてインストールします。
