
Ubuntu環境のPython
--------------------------------

`Ubuntu <https://www.ubuntu.com/>`_ には最初から Pythonがインストール済みの状態で提供されており、簡単に Python環境を整えられます。


Ubuntu 16.04 LTS
===========================

Python 3.5/Python 2.7がインストールされており、そのままで利用可能です。

デフォルトでは :jinja:`{{ content.link_to('./pip.rst') }}` がインストールされていませんので、インストールしておきます。

また、Pythonの拡張パッケージをインストールする際に必要となる、開発用パッケージも入れておきましょう。

.. code-block:: sh

   $ apt install python3-pip python3-dev
   $ apt install python-pip python-dev


Python 3.6 のインストール
++++++++++++++++++++++++++++++

Python 3.6 を使用する場合は、`Jonathon F <https://launchpad.net/~jonathonf>`_ 氏のプライベートリポジトリからインストールできます。

.. code-block:: sh

   $ sudo add-apt-repository ppa:jonathonf/python-3.6
   $ sudo apt-get update
   $ sudo apt-get install python3.6 python3.6-dev
   $ wget https://bootstrap.pypa.io/get-pip.py
   $ sudo python3.6 get-pip.py


Ubuntu 16.10 以降
===========================

Python 3.5/Python 2.7がインストールされています。Python 3.6も追加インストール可能です。

.. code-block:: sh

   $ sudo apt install python3.6


デフォルトでは :jinja:`{{ content.link_to('./pip.rst') }}` がインストールされていませんので、インストールしておきます。

また、Pythonの拡張パッケージをインストールする際に必要となる、開発用パッケージも入れておきましょう。

.. code-block:: sh

   $ apt install python3.6-pip python3.6-dev
   $ apt install python3.5-pip python3.5-dev
   $ apt install python-pip python-dev




