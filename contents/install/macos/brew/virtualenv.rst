
仮想環境
--------------------------------

Pythonを使い続けていると、いろいろな用途に合わせて、Python の実行環境を切り替えたくなることがあります。

例えば、現在開発中のWebアプリケーション開発では、Webアプリケーションフレームワークとして `Django <https://www.djangoproject.com/>`_ のバージョン 1.10 を使っており、新しいプロジェクトではバージョン 1.11 を使用することになった場合、両方のプロジェクトの開発を行うためには、簡単に Django のバージョンを切り替えられるようにしなければなりません。

また、Python2 でしか利用できない、古いモジュールやアプリケーションを使用する場合、Python3.x と Python2.x を切り替える手段が必要となります。

このような場合、Pythonではそれぞれの用途に応じて専用の **「仮想環境」** を作成し、仮想環境を切り替えながら利用します。

「仮想環境」には特定のバージョンのPython本体と、各種モジュールがインストールされます。あるプロジェクトで使用する仮想環境では Python 3.6 と Django 1.11をインストールし、別のプロジェクトの仮想環境には Python 2.7 と Django 1.10 を利用する、といった環境を簡単に構築できます。

仮想環境を作成するモジュールには `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_ と、`venv <https://docs.python.jp/3/library/venv.html>`_ があります。venv は Python3 の標準ライブラリですが、Python2.x で使用することができないため、ここでは Virtualenv を取り上げます。


Virtualenvのインストール
=============================

Virtualenvは、:jinja:`{{ page.link_to('./pip.rst') }}` コマンドでインストールできます。

.. code-block::

   $ pip3 install virtualenv


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




仮想環境の使用
=============================

仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンド で仮想環境の ``bin`` ディレクトリから実行されるようになります。

``bin`` ディレクトリには ``pip`` などのコマンドもインストールされており、コマンドラインから直接実行できるようになります。

.. code-block:: 

   $ . py3env/bin/activate
   (py3env) $>pip

   Usage:
     pip <command> [options]

   Commands:
     install                     Install packages.
     download                    Download packages.
     …

``pip`` コマンドを使って、通常通りパッケージをインストールできます。

.. code-block:: 

   (py3env) C:\Users\user1>pip install tse
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

   (py3env)$ deactivate
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

