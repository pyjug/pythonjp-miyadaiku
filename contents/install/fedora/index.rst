
Fedora環境のPython
--------------------------------

`Fedora <https://www.ubuntu.com/>`_ には最初から Pythonがインストール済みの状態で提供されており、簡単に Python環境を整えられます。


Fedora 26
===========================

Python 3.6がインストールされており、そのままで利用可能です。

Pythonの拡張パッケージをインストールする際に必要となる、開発用パッケージも入れておきましょう。

.. code-block:: sh

   $ dnf install python3-deve


Python 2.7 のインストール
++++++++++++++++++++++++++++++

Python 2.7はインストールされていないため、必要なら別途インストールが必要です。



.. code-block:: sh

   $ dnf install python2 python2-devel

Pythonの実行
+++++++++++++++++++

Python各バージョンは次のコマンドで実行できます。

Python 3.6
    ``python3``、``python3.6``

Python 2.7
    ``python``、``python2``、``python2.7``

