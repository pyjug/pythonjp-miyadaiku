
Pythonランチャー
===============================


Python 3.3以降には、Pythonランチャーとして ``py.exe`` がインストールされます。

MacOS や Linux などの Unix系OSでは、Python は ``python`` コマンドで実行しますが、Windowsではこの ``py.exe`` で実行したほうが便利です。

``py.exe`` は、環境変数 ``PATH`` を設定しなくとも、コマンドプロンプトから実行できます。


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

