
pip
===============================


`pip <https://pip.pypa.io/en/stable/>`_ は、`The Python Package Index <https://pypi.python.org/pypi>`_ に公開されているPythonパッケージのインストールなどを行うユーティリティで、Python 3.4以降には、標準で付属しています。

LinuxやmacOSでは、pipはコマンドとして

.. code-block::

   $ pip install xxxx

と使うことが多いのですが、Windows環境では、:jinja:`{{ content.path_to('./py_launcher.rst') }}` を使うと簡単に起動できます。

.. code-block::

   C:\>py -m pip install xxxx



パッケージのインストールは、``pip install`` コマンドで行います。

.. code-block::

   C:\Users\user1>py -m pip install xxxx
   …


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

