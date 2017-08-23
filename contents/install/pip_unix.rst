
pip
===============================

`pip <https://pip.pypa.io/en/stable/>`_ は、`The Python Package Index <https://pypi.python.org/pypi>`_ に公開されているPythonパッケージのインストールなどを行うユーティリティで、Python 3.4以降には、標準で付属しています。


パッケージのインストールは、``pip install`` コマンドで行います。

.. code-block::

   $ pip install tse
   …


不要なパッケージは、``pip uninstall`` コマンドで削除できます。

.. code-block::

   $ pip uninstall tse
   …
   Proceed (y/n)?
    Successfully uninstalled tse-0.0.15


Pythonを指定してインストール
-------------------------------------

複数のバージョンの Python がインストールされている環境では、どの Python の実行環境にパッケージをインストールするか、指定する必要があります。

次のように、パッケージをインストールする対象の Python を使って ``pip`` を呼び出だすと、簡単にインストール先を指定できます。


.. code-block::

   $ python3.6 -m pip install tse
   …

この場合は、``python3.6`` にパッケージをインストールします。また、別のPython環境にパッケージをインストールする場合には、


.. code-block::

   $ /opt/python/bin/python2.7 -m pip install tse
   …

のように、インストール先のPythonを指定して実行します。

