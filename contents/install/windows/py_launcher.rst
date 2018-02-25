
Pythonの実行方法
===============================


Windows環境では、Pythonランチャー  ``py.exe`` がインストールされます。

MacOS や Linux などの Unix系OSでは、``python`` コマンドで Python を実行しますが、Windowsではこの ``py.exe`` で実行したほうが便利です。


通常、Python をコマンドラインから実行するときには、Pythonをインストールしたディレクトリを環境変数というシステム設定に記録する必要がありますが、``py.exe`` は、設定をしなくとも実行できます。


.. code-block::

   C:\Users\user1>py
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

``py.exe`` は、最後にインストールしたバージョンの Python を実行します。インストール済みの、他のバージョンの Python を実行する場合は、オプションで指定します。

Python 3.6をインストールしてある環境では、``py -3.6`` でPython 3.6を指定して実行できます。


.. code-block::

   C:\Users\user1>py -3.6
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Python 2.x は、``py.exe -2`` で起動できます。

.. code-block::

   C:\Users\user1>py -2
   Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


Pythonにインストールされた :jinja:`{{ content.link_to('./pip.rst') }}` などのモジュールをコマンドとして実行するときは、通常の ``python.exe`` と同じように、``-m`` オプションでモジュール名を指定して実行できます。

たとえば、``pip`` パッケージを実行するときは、次のように ``-m`` オプションを使って実行できます。

.. code-block::

   C:\Users\user1>py -3 -m pip freeze
   virtualenv==15.1.0


PATH 環境変数の登録
-------------------------

``py.exe`` を使わず、``python.exe`` コマンドを実行するときは、環境変数 ``PATH``  にPythonのインストールディレクトリを登録します。

:jinja:`{{page.link_to('./install_py3.rst', fragment='execute_py3_install')}}` 時に **"Add Python 3.x to PATH"** を指定していれば、自動的に ``PATH`` が設定されます。


:jinja:`{{ utils.enlarge_image(content.load('./py-install1.png')) }}`


