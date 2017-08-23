
.. article::
   :type: snippet


VirtualEnv
*******************************


仮想環境の作成
=============================

では、最初の仮想環境を作成しましょう。適当なディレクトリで、次のコマンドを実行します。


.. code-block:: 

   $ virtualenv py3env


``./py3env/`` に Python3.6 用の仮想環境が作成されました。


仮想環境の切り替え
=============================


作成した仮想環境の ``bin/activate`` を実行します

.. code-block:: 

   $ . ./py3env/bin/activate
   (py3env) $ 

コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境が設定されたことを示します。


仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンド で仮想環境の ``bin`` ディレクトリから実行されるようになります。

``bin`` ディレクトリには ``pip`` などのコマンドもインストールされており、コマンドラインから実行できるようになります。

.. code-block:: 

   (py3env) $ pip

   Usage:
     pip <command> [options]

   Commands:
     install                     Install packages.
     download                    Download packages.
     …

``pip`` コマンドを使って、通常通りパッケージをインストールできます。

.. code-block:: 

   (py3env) $ pip install tse
   Collecting tse
     Downloading tse-0.0.15.tar.gz
   Collecting argparse (from tse)
     Downloading argparse-1.4.0-py2.py3-none-any.whl
   Collecting six (from tse)
     Using cached six-1.10.0-py2.py3-none-any.whl
     …


インストールしたパッケージは、仮想環境内にのみ書き込まれ、元の Python や他の仮想環境からは利用できません。


仮想環境の終了
=============================

仮想環境の使用を終え、通常の状態に復帰するときは、``deactivate`` コマンドを実行します。

.. code-block:: 

   (py3env) $ deactivate
   $ 


.. target:: select_python_version


Pythonを指定した仮想環境
==========================================================

複数のバージョンの Python をインストールしていれば、使用する Python を指定して仮想環境を作成できます。

異なるバージョンの Python 用に仮想環境を作成する場合、そちらの環境にも ``virtualenv`` をインストールしておくと簡単です。

次のコマンドは、Python2.7 に ``virtualenv`` をインストールします。

.. code-block:: 

   $ python2.7 -m pip install virtualenv

Python2.7 を使って、仮想環境を作成します。

.. code-block:: 

   $ python2.7 -m virtualenv py27env

ここで作成した ``py27env`` を使用すると、python2.7 環境に切り替わります。


.. code-block:: 

   $ . py27env/bin/activate
   (py27env) $ python
   Python 2.7.13 (default, Apr  4 2017, 08:47:57)
   [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>




