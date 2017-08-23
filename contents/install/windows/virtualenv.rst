
仮想環境
--------------------------------


.. jinja::

   {{ content.load('/install/why_virtualenv.rst').html }}




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

仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンド や ``py`` コマンドで仮想環境の Pythonを実行できるようになります。


.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>python
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


仮想環境を使用中は、仮想環境の ``Scripts`` ディレクトリにインストールされるコマンドも実行できるようになります。``pip`` などコマンドが、次のように実行できます。

.. code-block::

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>pip 

   

``pip`` コマンドを使って、仮想環境にパッケージをインストールできます。

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

まず、Python2.7 を使って、仮想環境を作成します。

.. code-block:: 

   C:\Users\user1> py -2 -m virtualenv py27env

ここで作成した ``py27env`` を使用すると、python2.7 環境に切り替わります。


.. code-block:: 

   C:\Users\user1>py27env\Scripts\activate.bat
   (py27env) C:\Users\user1>python
   Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

