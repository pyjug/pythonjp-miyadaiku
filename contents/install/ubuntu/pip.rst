
.. jinja::

   {{  content.load('/install/pip_unix.rst').html }}


pip
=======================

Debian パッケージでインストールした pip (python3-pip/python-pip) コマンドは独自の修正が加えられており、非rootユーザが仮想環境外で ``pip install`` を実行すると、デフォルトで ``--user`` オプションが指定されます。

このため、一般ユーザが ``pip install xxxx`` でパッケージをインストールしても、``/usr/local/lib/...`` などにはインストールされず、ユーザのホームディレクトリの ``~/.local`` ディレクトリにインストールされます。
