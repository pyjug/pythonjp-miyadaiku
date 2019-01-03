
仮想環境
--------------------------------


.. jinja::

   {{ content.load('/install/why_venv.rst').html }}





仮想環境の作成
=============================

では、最初の仮想環境を作成しましょう。適当なディレクトリで、次のコマンドを実行します。


.. code-block:: 

   C:\Users\user1> py -m venv C:\Users\user1\py3env

このコマンドは、指定したディレクトリ ``C:\Users\user1\py3env`` に仮想環境を作成します。



仮想環境の切り替え
=============================

Windowsでは、Python を コマンド プロンプトで実行する場合と、PowerShell で実行する場合で、仮想環境の使い方が違います。それぞれの環境で、作成した ``py3env`` を使うときは、次のように使用します。

コマンド プロンプトでの切り替え
++++++++++++++++++++++++++++++++++++++++++

作成した仮想環境の ``Scripts\activate.bat`` を実行します

.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>


コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境で実行中であることを示します。


PowerShellでの切り替え
++++++++++++++++++++++++++++++++++++++++++

まず、PowerShellでPowerShellスクリプトを実行できるようにします。

PowerShellを起動し、次のコマンドを実行します。このコマンドは、一番最初に一回だけ実行してください。2回目以降は不要です。


.. code-block::

    PS C:\> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force


次に、作成した仮想環境の ``Scripts\activate.ps1`` を実行します

.. code-block:: 

   PS C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.ps1

   (py3env) C:\Users\user1>


コマンド プロンプトの先頭に ``(py3env)`` と表示され、仮想環境で実行中であることを示します。



仮想環境の使用
=============================

仮想環境に切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンド や ``py`` コマンドで仮想環境の Pythonを実行できるようになります。


.. code-block:: 

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>python
   Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


仮想環境を使用中に ``pip`` コマンドでパッケージをインストールすると、仮想環境にインストールされます。

.. code-block:: 

   (py3env) C:\Users\user1>py -m pip install tse
       Collecting tse
     Downloading tse-0.0.15.tar.gz
   Collecting argparse (from tse)
     Downloading argparse-1.4.0-py2.py3-none-any.whl
   Collecting six (from tse)
     Using cached six-1.10.0-py2.py3-none-any.whl
     …


インストールしたパッケージは、仮想環境内にのみ書き込まれ、元の Python や他の仮想環境からは利用できません。

仮想環境を使用中は、仮想環境の ``Scripts`` ディレクトリにインストールされるコマンドも実行できるようになります。``pip`` などコマンドを、次のように実行できます。

.. code-block::

   C:\Users\user1> C:\Users\user1\py3env\Scripts\activate.bat
   (py3env) C:\Users\user1>pip 


仮想環境の終了
=============================

仮想環境の使用を終え、通常の状態に復帰するときは、``deactivate`` コマンドを実行します。

.. code-block:: 

   (py3env) PS C:\Users\user1> deactivate
   C:\Users\user1>


.. target:: select_python_version

Pythonを指定した仮想環境
==========================================================

複数のバージョンの Python をインストールしている環境では、使用する Python を指定して仮想環境を作成できます。


Python 3.6とPython 3.7がインストールされた環境で、Python 3.7の仮想環境を作成する場合は、次のように指定します。

.. code-block:: 

   C:\Users\user1> py -3.7 -m venv py37env

ここで作成した ``py37env`` を使用すると、python 3.7の仮想環境に切り替わります。


.. code-block:: 

   C:\Users\user1>py37env\Scripts\activate.bat
   (py37env) C:\Users\user1>python
   Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

