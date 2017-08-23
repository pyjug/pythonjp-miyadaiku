
Pythonランチャー
===============================


Python 3.3以降には、Pythonランチャーとして ``py.exe`` がインストールされます。

MacOS や Linux などの Unix系OSでは、Python は ``python`` コマンドで実行しますが、Windowsではこの ``py.exe`` で実行したほうが便利です。


通常、Python をコマンドラインから実行するときには、Pythonをインストールしたディレクトリを環境変数というシステム設定に記録する必要がありますが、``py.exe`` は、設定をしなくとも実行できます。


.. code-block::

   C:\Users\user1>py
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

``py.exe`` は、最後にインストールしたバージョンの Python を実行します。インストール済みの、他のバージョンの Python を実行する場合は、オプションで指定します。

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


.. code-block::

   C:\Users\user1>py -3 -m pip freeze
   virtualenv==15.1.0


