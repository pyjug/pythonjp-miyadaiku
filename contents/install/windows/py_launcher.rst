
Pythonの実行方法
===============================

Pythonを起動する方法にもいろいろありますが、ここではWindowsのコマンドプロンプトを使う方法を紹介します。

まず、スタートボタンをクリックし、*Windows システム ツール* の *コマンド プロンプト* を選択します。

:jinja:`{{ utils.enlarge_image(content.load('./commandprompt1.png')) }}`

すると、次のようにコマンドプロンプトが表示されます。

:jinja:`{{ utils.enlarge_image(content.load('./commandprompt2.png')) }}`


Windows環境では、Pythonランチャー ``py.exe`` がインストールされます。

コマンドプロンプトxで ``py.exe`` を起動して、``1+1`` と入力してみましょう。

.. code-block::

   C:\Users\user1>py.exe
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 1+1
   2

Pythonを終了するときは、``quit()`` と入力するか、コントロールキーを押しながら ``Z`` キーを押します。

.. code-block::

   C:\Users\user1>py.exe
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 1+1
   2
   >>> quit()
   C:\Users\user1>



MacOS や Linux などの Unix系OSでは、``python`` コマンドや ``python3`` コマンドで Python を実行しますが、Windowsではこの ``py.exe`` で実行したほうが便利です。

通常、Python をコマンドラインから実行するときには、Pythonをインストールしたディレクトリを環境変数というシステム設定に記録する必要がありますが、``py.exe`` は、設定をしなくとも実行できます。

``py.exe`` は、インストールされている最新バージョンの Python を実行します。インストール済みの、他のバージョンの Python を実行する場合は、オプションで指定します。

``py -3.6`` と指定すると、Python 3.6を実行します。

.. code-block::

   C:\Users\user1>py -3.6
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


``py -3`` で、最新のPython 3.xを実行します。


.. code-block::

   C:\Users\user1>py -3
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


Python 2.x は、``py.exe -2`` で起動できます。

.. code-block::

   C:\Users\user1>py -2
   Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


Pythonモジュールの実行
---------------------------------

:jinja:`{{ content.link_to('./pip.rst') }}` などのPythonアプリケーションをインストールして実行するときには、通常の ``python.exe`` と同じように、``-m`` オプションでモジュール名を指定して実行できます。

たとえば、``pip`` モジュールを実行するときは、次のように ``-m`` オプションを使って実行します。

.. code-block::

   C:\Users\user1>py -m pip freeze
   virtualenv==15.1.0


特定のPythonバージョンを指定して実行することもできます。次の例は、Python3.6で ``pip`` コマンドを実行します。

.. code-block::

   C:\Users\user1>py -3.6 -m pip freeze
   virtualenv==15.1.0

