
CentOS 環境のPython
--------------------------------

`CentOS 7 <https://www.centos.org/>`_ では、Python 2.7 がインストールされています。しかし、Python 2.x はもう古いリリースですので、Python3.xのインストールを推奨します。


CentOS 7 環境のPython
===================================

Python 3.6 のインストール
++++++++++++++++++++++++++++

CentOSのリポジトリは Python 3.x をリリースしていないので、`IUS <https://ius.io/>`_ を利用してインストールします。

まず、IUS のリポジトリを yum に追加します

.. code-block:: console

   $ su
   # yum -y install https://centos7.iuscommunity.org/ius-release.rpm

次のコマンドで、Python 3.6 をインストールします。また、拡張モジュールのインストールに必要な開発環境と、:jinja:`{{ content.link_to('./pip.rst') }}` コマンドもインストールします。


.. code-block:: console

   $ su
   # yum -y install python36u  python36u-devel python36u-pip


Python 2.7 のインストール
++++++++++++++++++++++++++++

Python 2.7 はデフォルトでインストール済みですが、拡張モジュールのインストールに必要な開発環境と、:jinja:`{{ content.link_to('./pip.rst') }}` コマンドをインストールします。

.. code-block:: console

   $ su
   # yum -y install yum install python2-devel python2-pip


Pythonの実行
+++++++++++++++++++

Python各バージョンは次のコマンドで実行できます。

Python 3.6
    ``python3.6``

Python 2.7
    ``python``、``python2``、``python2.7``




