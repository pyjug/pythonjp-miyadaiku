
pip
===============================


`pip <https://pip.pypa.io/en/stable/>`_ は、`The Python Package Index <https://pypi.python.org/pypi>`_ に公開されているPythonパッケージのインストールなどを行うユーティリティで、Python 3.4以降には、標準で付属しています。

Windows環境では、pipコマンドは :jinja:`{{ content.link_to('./py_launcher.rst') }}` を使用した起動が簡単です。

.. code-block::

   C:\>py -m pip install xxxx



パッケージのインストールは、``pip install`` コマンドで行います。

.. code-block::

   C:\Users\user1>py -m pip install xxxx
   …


Pythonを指定してインストール
-------------------------------------

複数のバージョンの Python がインストールされている環境では、どの Python の実行環境にパッケージをインストールするか、指定する必要があります。


パッケージは、``pip`` を実行する Pythonの実行環境にインストールされます。複数のPythonがインストールされている環境で Python3 にパッケージをインストールする場合には、

.. code-block::

   C:\Users\user1>py -3 -m pip install xxxxx
   …

とします。Python2.7にインストールする場合は、

.. code-block::

   C:\Users\user1>py -2.7 -m pip install xxxxx
   …

とします。

不要なパッケージは、``pip uninstall`` コマンドで削除できます。

.. code-block::

   C:\Users\user1>py -m pip uninstall xxxx
   …
   Proceed (y/n)?
    Successfully uninstalled xxxx-0.0.15

