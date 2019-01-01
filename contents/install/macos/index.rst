
macOS環境のPython
--------------------------------

現在のmacOS では、Python 2.7 がインストールされています。しかし、Python 2.7 はもう古いリリースで、利用はおすすめできません。

ここでは、最新のPythonをダウンロードして、インストールする手順を紹介します。


Python3 のダウンロード
===========================

ブラウザで https://www.python.org/downloads/ を開きます。macOSで開いた場合は、**「Downoad Python 3.x.x」** をクリックして最新版のインストーラをダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download.png')) }}`


最新バージョン以外のPythonを利用する場合は、画面下のバージョン別ダウンロードページへのリンクから、**「macOS 64-bit installer」** (macOS 10.8以前の場合は 「macOS 64-bit/32-bit installer」) をダウンロードします。




Python3 のインストール
===========================

ダウンロードしたパッケージを実行し、画面の指示に従ってインストールします。

:jinja:`{{ utils.enlarge_image(content.load('./installer.png')) }}`



SSL証明書のインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python3.6以降では、インストール後にネットワーク通信に使用するSSL証明書をインストールする必要があります。

1. ファインダで **アプリケーションフォルダ** を開きます。


2. **Python 3.xフォルダ** (Python 3.7.xなら **Python 3.7 フォルダ**) をダブルクリックし、フォルダを開きます。

   :jinja:`{{ utils.enlarge_image(content.load('./finder1.png')) }}`


3. **Install Certificates.command** ファイルをダブルクリックし、証明書のインストールを行います。

   :jinja:`{{ utils.enlarge_image(content.load('./install_cert.png')) }}`


   インストールが終了すると、次のような画面が表示されます。


   :jinja:`{{ utils.enlarge_image(content.load('./cert_finished.png')) }}`



Python3 の実行方法
===========================

Pythonインストーラは、環境変数 ``PATH`` の設定を行いますので、インストール終了後、新しく起動したコンソールでは、``python3`` コマンドで最後にインストールしたPythonを実行できます。

.. code-block::

   $ python3
   Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
   [Clang 6.0 (clang-600.0.57)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>



または、``python3.7`` のように、バージョンを指定してPythonを実行します。

.. code-block::

   $ python3.7
   Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
   [Clang 6.0 (clang-600.0.57)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


環境変数 ``PATH`` は、使用中のシェルに応じた設定ファイルで設定されますので、必要に応じて修正してください。

設定ファイルは、bashの場合は``~/.bash_profile``、zshの場合は ``~/.zprofile``、その他の場合は ``~/.profile`` などとなります。

インストール時にディレクトリ ``/usr/local/bin`` にも Python3コマンドやPython3.xコマンドのリンクが作成されますので、こちらを利用するようにしても良いでしょう。

