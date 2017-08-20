
.. jinja::

   {{ content.load('/install/why_virtualenv.rst').html }}


仮想環境
--------------------------------

Python を使って開発や実験を行うときは、用途に応じて専用の実行環境を作成し、切り替えて使用するのが一般的です。こういった、一時的に作成する実行環境を、**「仮想環境」** と言います。

仮想環境は、次のような目的で使われます。

- システム全体で使うPython環境に影響を与えずにモジュールの追加・入れ替えをしたい。

- 同じモジュールの、複数のバージョンを使い分けたい。例えば、開発中のWebアプリケーション開発では、Webアプリケーションフレームワークとして `Django <https://www.djangoproject.com/>`_ の 1.10 を使い、新しいプロジェクトではバージョン 1.11 を使用したい場合など、簡単に切り替えられるようにしたい。

- 異なるバージョンの Python を使いたい。Python2 でしか利用できない、古いモジュールやアプリケーションを使用する場合、Python3.x と Python2.x を切り替える手段が必要となります。


仮想環境には特定のバージョンのPython本体と、各種モジュールがインストールされます。あるプロジェクトで使用する仮想環境では Python 3.6 と Django 1.11をインストールし、別のプロジェクトの仮想環境には Python 2.7 と Django 1.10 を利用する、といった環境を簡単に構築できます。

仮想環境を作成するモジュールには `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_ と、`venv <https://docs.python.jp/3/library/venv.html>`_ があります。venv は Python3 の標準ライブラリですが、Python2.x で使用することができないため、ここでは Virtualenv を取り上げます。


Virtualenvのインストール
=============================

Virtualenvは、:jinja:`{{ page.link_to('./pip.rst') }}` コマンドでインストールできます。

.. code-block::

   C:\> py -m pip install virtualenv


仮想環境の作成
=============================

では、最初の仮想環境を作成しましょう。適当なディレクトリで、次のコマンドを実行します。


.. code-block:: 

   C:\Users\user1> py -m virtualenv py3env
   Using base prefix 'C:\\Users\\user1\\AppData\\Local\\Programs\\Python\\Python36'
   New python executable in C:\Users\user1\py3env\Scripts\python.exe
   Installing setuptools, pip, wheel...done.


``C:\Users\user1\py3env\`` に Python3.6 用の仮想環境が作成されました。


仮想環境の切り替え
=============================

Windowsでは、Python を コマンド プロンプトで実行する場合と、PowerShell で実行する場合で、仮想環境の使い方が違います。それぞれの環境で、作成した ``py3env`` を使うときは、次のように使用します。

コマンド プロンプトでの切り替え
++++++++++++++++++++++++++++++++++++++++++

作成した仮想環境の ``Scripts\activate.bat`` を実行します

.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>


コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境が設定されたことを示します。


PowerShellでの切り替え
++++++++++++++++++++++++++++++++++++++++++

まず、PowerShellでPowerShellスクリプトを実行できるようにします。

PowerShellを起動し、次のコマンドを実行します。

.. code-block::

    PS C:\> Set-ExecutionPolicy Unrestricted -Force -Scope CurrentUser


次に、作成した仮想環境の ``Scripts\activate.ps1`` を実行します

.. code-block:: 

   PS C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.ps1
   (py3env) C:\Users\user1>


コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境が設定されたことを示します。



仮想環境の使用
=============================

仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンド や ``py`` コマンドで仮想環境の ``Scripts`` ディレクトリから実行されるようになります。

``Scripts`` ディレクトリには ``pip`` などのコマンドもインストールされており、コマンドラインから直接実行できるようになります。

.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>pip

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

   (py3env) PS C:\Users\user1> deactivate
   C:\Users\user1>


.. target:: select_python_version

Pythonを指定した仮想環境
==========================================================

複数のバージョンの Python をインストールしていれば、使用する Python を指定して仮想環境を作成できます。

異なるバージョンの Python 用に仮想環境を作成する場合、そちらの環境にも ``virtualenv`` をインストールしておくと簡単です。

次のコマンドは、Python2.7 に ``virtualenv`` をインストールします。

.. code-block:: 

   C:\Users\user1> py -2 -m pip install virtualenv

Python2.7 を使って、仮想環境を作成します。

.. code-block:: 

   C:\Users\user1> py -2 -m virtualenv py27env

ここで作成した ``py27env`` を使用すると、python2.7 環境に切り替わります。


.. code-block:: 

   C:\Users\user1> py27env\Scripts\activate.bat
   (py27env) C:\Users\user1>python
   Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

