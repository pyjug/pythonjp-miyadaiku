
pip
===============================

`pip <https://pip.pypa.io/en/stable/>`_ は、`The Python Package Index <https://pypi.python.org/pypi>`_ に公開されているPythonパッケージのインストールなどを行うユーティリティで、Python 3.4以降には、標準で付属しています。


パッケージのインストールは、``pip install`` コマンドで行います。

.. code-block::

   $ pip install xxx
   …


不要なパッケージは、``pip uninstall`` コマンドで削除できます。

.. code-block::

   $ pip uninstall xxx
   …
   Proceed (y/n)?
    Successfully uninstalled xxx-0.0.15


Pythonを指定してインストール
-------------------------------------

複数のバージョンの Python がインストールされている環境では、どの Python の実行環境にパッケージをインストールするか、指定する必要があります。

パッケージは、``pip`` を実行する Pythonの実行環境にインストールされます。たとえば、複数のPythonがインストールされている環境で Python 3.6 にパッケージをインストールする場合には、Python 3.6 を使って次のように実行します。


.. code-block::

   $ python3.6 -m pip install xxx
   …

特定のディレクトリにあるPython 2.7環境にパッケージをインストールする場合には、


.. code-block::

   $ /opt/python/bin/python2.7 -m pip install xxx
   …

とします。

