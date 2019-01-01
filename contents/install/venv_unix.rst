
.. article::
   :type: snippet




仮想環境の作成
=============================

では、最初の仮想環境を作成しましょう。適当なディレクトリで、次のコマンドを実行します。


.. code-block:: 

   $ python3 -m venv ./py3env


このコマンドは、指定したディレクトリ ``./py3env`` に仮想環境を作成します。



仮想環境の切り替え
=============================


作成した仮想環境の ``bin/activate`` を実行します

.. code-block:: 

   $ . ./py3env/bin/activate
   (py3env) $ 

コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境で実行中であることをを示します。


仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンドや ``python3`` コマンドで仮想環境の ``bin`` ディレクトリから実行されるようになります。

通常の環境では、``python`` コマンドを実行するとPython2.xが実行されますが、仮想環境中では、``python`` コマンドでも ``python3`` コマンドでも仮想環境を作成した Python を起動します。

.. code-block:: 

   (py3env) $ python
   Python 3.6.1 (default, Apr  4 2017, 09:40:21)
   [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


``bin`` ディレクトリには ``pip`` などのコマンドもインストールされており、コマンドラインから実行できます。

.. code-block:: 

   (py3env) $ pip

   Usage:
     pip <command> [options]

   Commands:
     install                     Install packages.
     download                    Download packages.
     …


パッケージのインストール
=============================


仮想環境を利用中も、通常通り ``pip`` コマンドを使ってパッケージをインストールできます。

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

複数のバージョンの Python をインストールしている環境では、使用する Python を指定して仮想環境を作成できます。


Python 3.6とPython 3.7がインストールされた環境で、Python 3.7の仮想環境を作成する場合は、次のように指定します。


.. code-block:: 

   $ python3.7 -m venv py37env

ここで作成した ``py37env`` を使用すると、python3.7 環境に切り替わります。

.. code-block:: 

   $ . py37env/bin/activate
   (py37env) $ python
   Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
   [Clang 6.0 (clang-600.0.57)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
