
仮想環境
--------------------------------

Pythonを使い続けていると、いろいろな用途に合わせて、Python の実行環境を切り替えたくなることがあります。

例えば、現在開発中のWebアプリケーション開発では、Webアプリケーションフレームワークとして `Django <https://www.djangoproject.com/>`_ のバージョン 1.10 を使っており、新しいプロジェクトではバージョン 1.11 を使用することになった場合、両方のプロジェクトの開発を行うためには、簡単に Django のバージョンを切り替えられるようにしなければなりません。

また、Python2 でしか利用できない、古いモジュールやアプリケーションを使用する場合、Python3.x と Python2.x を切り替える手段が必要となります。

このような場合、Pythonではそれぞれの用途に応じて専用の **「仮想環境」** を作成し、仮想環境を切り替えながら利用します。

「仮想環境」には特定のバージョンのPython本体と、各種モジュールがインストールされます。あるプロジェクトで使用する仮想環境では Python 3.6 と Django 1.11をインストールし、別のプロジェクトの仮想環境には Python 2.7 と Django 1.10 を利用する、といった環境を簡単に構築できます。

仮想環境を作成するモジュールには `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_ と、`venv <https://docs.python.org/3/library/venv.html>`_ があります。venv は Python3 の標準ライブラリですが、Python2.x で使用することができないため、ここでは Virtualenv を取り上げます。


Virtualenvのインストール
=============================

Virtualenvは、pip でインストールできます。

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

Windowsでは、Python を コマンド プロンプトで実行する場合と、PowerShell で実行する場合で、仮想環境の使い方が違います。それぞれの環境で、``py3env`` を使うときは、次のように使用します。

コマンド プロンプトで仮想環境を使用する
++++++++++++++++++++++++++++++++++++++++++

作成した仮想環境の ``Scripts\activate.bat`` を実行します

.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>


コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境が設定されたことを示します。


PowerShellで仮想環境を使用する
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


仮想環境の終了
=============================

仮想環境の使用を終え、通常の状態に復帰するときは、``deactivate`` コマンドを実行します。

.. code-block:: 

   (py3env) PS C:\Users\user1> deactivate
   C:\Users\user1>

