
Ubuntu環境のPython
--------------------------------

`Ubuntu <https://www.ubuntu.com/>`_ では、パッケージのインストールは `APT <https://help.ubuntu.com/lts/serverguide/apt.html>` で管理されており、簡単に Python環境を整えられます。

また、データサイエンス向けに作成された Pythonパッケージ `Anaconda <https://www.continuum.io/>`_ も利用できます。

- `APT <https://help.ubuntu.com/lts/serverguide/apt.html>` 

  Ubuntu標準のパッケージ管理ツールで、Python だけではなく、他の多くのアプリケーションも一括して管理を行います。

  一般的なアプリケーション・Web開発やシステム管理ツールとしてPythonを利用する場合は、APT で構築した環境で問題ありません。


:jinja:`{{ content.load('/install/about_anaconda.rst').html }}`



Ubuntu 16.04 LTS
===========================

Python 3.5/Python 2.7がインストールされています。

Python 3.6 を利用する場合は、`Jonathon F <https://launchpad.net/~jonathonf>`_ 氏のプライベートリポジトリからインストールできます。

.. code-block:: sh

   $ sudo add-apt-repository ppa:jonathonf/python-3.6
   $ sudo apt-get update
   $ sudo apt-get install python3.6


apt install python3-pip
apt install python-pip
apt install python-dev
apt install python3-dev
apt install python3.6-dev


Ubuntu 16.10 以降
===========================

Python 3.5/Python 2.7がインストールされています。Python 3.6も追加インストール可能です。

.. code-block:: sh

   $ sudo apt install python3.6




 apt install python3-dev

