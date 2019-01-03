
CentOS 環境のPython
--------------------------------

`CentOS 7 <https://www.centos.org/>`_ では、Python 2.7 がインストールされています。しかし、Python 2.x はもう古いリリースですので、最新のPython3.xをインストールして使用しましょう。




Pythonのビルド
======================

1. ビルドツール・ライブラリのインストール
+++++++++++++++++++++++++++++++++++++++++++++++++


次のコマンドで、必要なツール類をダウンロードします。


.. code-block:: bash

   $ sudo yum groupinstall "development tools"
   $ sudo yum install bzip2-devel gdbm-devel libffi-devel \
     libuuid-devel ncurses-devel openssl-devel readline-devel \
     sqlite-devel tk-devel wget xz-devel zlib-devel


.. jinja::

   {{ content.load('/install/build_python_unix.rst').html }}


