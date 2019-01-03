.. article::
   :title: pip


.. jinja::

   {{  content.load('/install/pip_unix.rst').html }}


Ubuntu 環境の pip
=======================

Ubuntuは標準パッケージとして pip コマンドを提供しており、次のコマンドでインストールできます。

.. code-block:: bash

   $ sudo apt install python3-pip

標準パッケージでインストールした pip は、以下の点でオリジナルの pip と異なりますので注意してください。

Debian パッケージの pipコマンド (python3-pip/python-pip) は独自の修正が加えられており、特権ユーザではない、一般ユーザとして ``pip install`` コマンドを実行すると、自動的に ``--user`` オプションが指定されたのもとして実行します。

通常、pipコマンドでパッケージをインストールすると、``/usr/local/lib/`` などの、全ユーザが参照できる、Pythonのモジュール格納ディレクトリにインストールされます。

しかし、``--user`` オプションを指定すると、それぞれのユーザ個別の専用ディレクトリにインストールされ、他のユーザに影響を与えずに自由にパッケージのインストールや削除ができます。

このため、Ubuntuが提供する pip コマンド使用する場合、非rootユーザが ``pip install`` を実行すると、ホームディレクトリの ``~/.local`` ディレクトリにインストールされます。

``sudo pip3 install xxx`` のように、特権ユーザとしてコマンドを実行した場合には、``/usr/local/lib`` にインストールされます。


