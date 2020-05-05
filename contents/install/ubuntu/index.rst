
Ubuntu環境のPython
===================================


`Ubuntu <https://www.ubuntu.com/>`_ には最初からPythonがインストールされており、そのまま利用可能です。


しかし、このPython は、 OS がさまざまな機能を提供するために使用しています。ユーザが勝手にパッケージを導入したりすると、 OS の安定性を損なうことも考えられます。また、バージョンが古く、Pythonの最新機能は使用できません。

そこで、ここでは最新版のPythonをダウンロードし、インストールする手順を紹介します。






1. ビルドツール・ライブラリのインストール
+++++++++++++++++++++++++++++++++++++++++++++++++


次のコマンドで、必要なツール類をダウンロードします。


.. code-block:: bash

   $ sudo apt update
   $ sudo apt install build-essential libbz2-dev libdb-dev \
     libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
     libncursesw5-dev libsqlite3-dev libssl-dev \
     zlib1g-dev uuid-dev tk-dev

.. jinja::

   {{ content.load('/install/build_python_unix.rst').html }}


