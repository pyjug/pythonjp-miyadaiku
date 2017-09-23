.. article::
   :title: pip


.. jinja::

   {{  content.load('/install/pip_unix.rst').html }}


Ubuntu 環境の pip
=======================

通常、pipコマンドでパッケージをインストールすると、``/usr/local/lib/`` などの、システムの管理下にあるディレクトリにインストールされます。

しかし、Debian パッケージの pipコマンド (python3-pip/python-pip) は独自の修正が加えられており、非rootユーザが仮想環境外で ``pip install`` を実行すると、ホームディレクトリの ``~/.local`` ディレクトリにインストールされます。

``sudo pip3 install xxx`` のように、特権ユーザとしてコマンドを実行した場合には、``/usr/local/lib`` にインストールされます。
