
Conda コマンド
--------------------------------

Anaconda には `conda <https://conda.io/docs/index.html>`_ コマンドがインストールされており、パッケージのインストールや、実行環境の作成・切り替えなどを行えます。


Conda パッケージのインストール
=======================================

``conda install`` コマンドを使って、`ANACONDA PACKAGE LIST <https://docs.continuum.io/anaconda/packages/pkg-docs>`_ の Pythonパッケージをインストールできます。

.. code-block::

   $ conda install idna
   Fetching package metadata ...........
   Solving package specifications: .

   Package plan for installation in environment C:\Users\user1\Anaconda3\envs\xxx:

   The following packages will be UPDATED:

       anaconda: 4.4.0-np112py36_0 --> custom-py36_0
       idna:     2.5-py36_0        --> 2.6-py36_0

   Proceed ([y]/n)?
   …


Conda環境の作成
=======================================

``conda create`` コマンドは、特定のPythonバージョンやパッケージなどをインストールし、用途に応じて切り替えられる環境を作成します。

.. code-block::

   $ conda create --name env1
   Fetching package metadata ...........
   Solving package specifications:
   Package plan for installation in environment C:\Users\user1\Anaconda3\envs\env1:

   Proceed ([y]/n)? y
   …

Conda環境は独立したPythonの実行環境で、他の環境には影響を与えずにパッケージのインストールや削除を行えます。


作成した環境は、``activate`` コマンドで使用します。

.. code-block::

   $ activate env1
   (env1) $ 

環境が切り替わると、コマンドプロンプトに ``(env1)`` と表示されます。

仮想環境を切り替えると、環境変数 ``PATH`` が設定され、``python`` コマンドは ``env1`` 環境から実行されるようになります。また、``conda install`` でインストールするパッケージも、``env1`` 環境にのみインストールされます。



Pythonのバージョンを指定して環境を作成するときは、``python`` 引数を使用します。次の例は、Python 2.7 用の環境を作成します。

.. code-block::

   $ conda create -n py2env python=2.7
   Fetching package metadata ...........
   Solving package specifications: .

   Package plan for installation in environment C:\Users\user1\Anaconda3\envs\py2env:

   The following NEW packages will be INSTALLED:

       pip:            9.0.1-py27_1
       python:         2.7.13-1
       setuptools:     27.2.0-py27_1
       vs2008_runtime: 9.00.30729.5054-0
       wheel:          0.29.0-py27_0

   Proceed ([y]/n)?y
   …

