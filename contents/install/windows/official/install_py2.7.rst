Python 2.7のインストール
-----------------------------------


Python2 でしか利用できない古いモジュールやアプリケーションを使用する場合、Pyton3 と Python2 をどちらもインストールして併用できます。


パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.python.org/downloads/windows/ より、Python 2.7 パッケージをダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download-win.png')) }}`


画面の一番下に、ダウンロード可能なファイルが表示されます。インストールするWindowsが32bit版なら

  **Windows x86 MSI installer**

64bit版なら

  **Windows x86-64 MSI installer**

をインストールしてください。


Windowsの種類が不明な場合は、

    https://support.microsoft.com/ja-jp/help/958406

を参照に確認してください。


:jinja:`{{ utils.enlarge_image(content.load('./download-py2.7.png')) }}`



パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行し、*Next* をクリックしてインストールを開始します。

:jinja:`{{ utils.enlarge_image(content.load('./py27-install1.png')) }}`

:jinja:`{{ utils.enlarge_image(content.load('./py27-install2.png')) }}`

:jinja:`{{ utils.enlarge_image(content.load('./py27-install3.png')) }}`


Cコンパイラのインストール
++++++++++++++++++++++++++++++++++++++++++++++++++



Pythonの拡張モジュールをインストールする際に、Cコンパイラが必要となる場合があります。

WindowsではCコンパイラが添付されていないため、別途インストールする必要があります。Python2.7の場合は、

    https://www.microsoft.com/en-us/download/details.aspx?id=44266



より、

    **Microsoft Visual C++ Compiler for Python 2.7**

をダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download-vstools27.png')) }}`


ダウンロードしたインストーラを実行し、

    **Visual C++ Build Tools 2017**

をチェックして **Install** ボタンをクリックします。

:jinja:`{{ utils.enlarge_image(content.load('./install-vc27-1.png')) }}`


実行環境の切り替え
+++++++++++++++++++++++++++++


Python2.7 への実行環境の切り替えは、`Virtualenv <https://virtualenv.pypa.io/en/stable/>`_ で行います。

仮想環境の作成方法は、

    :jinja:`{{ content.link_to('virtualenv.rst', fragment='select_python_version')}}` 

を参照してください。
