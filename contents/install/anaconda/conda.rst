
Conda コマンド
--------------------------------

Anaconda には `conda <https://conda.io/docs/index.html>`_ コマンドがインストールされており、パッケージのインストールや、実行環境の作成・切り替えなどを行えます。

LinuxやmacOSでは、``source anaconda3/etc/profile.d/conda.sh`` コマンドを実行すると、``conda`` コマンドが利用可能になります。``bash`` を利用している場合は、次のように ``~/.bash_profile`` を設定します。


.. code-block:: bash

   # macOS の場合
   $ echo "source /anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile

   # linuxの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile


Windows環境では、スタートメニューの「**Anaconda3(64bit)** | **Anaconda Prompt**」で表示されるコマンドプロンプトで実行できます。


:jinja:`{{ utils.enlarge_image(content.load('./win-start-menu.png')) }}`



Conda環境
=======================================

Conda環境は独立したPythonの実行環境で、他の環境に影響を与えずにPythonのバージョンを用途によって切り替えたり、パッケージをインストールしたりできます。


Conda環境の作成
++++++++++++++++++++++++++++++++++++++

新しい環境は、 ``conda create`` コマンドで作成します。
次の例では、Python3.7を利用する、``py37env`` という名前の環境を作成します。

.. code-block::

   $ conda create --name py37env python=3.7
   Fetching package metadata ...........
   Solving package specifications:
   Package plan for installation in environment C:\Users\user1\Anaconda3\envs\env1:

   Proceed ([y]/n)? y
   …


Conda環境の切り替え
++++++++++++++++++++++++++++++++++++++

``py37env`` 環境を使うときには、``conda activate`` コマンドを実行します。

.. code-block::

   $ conda activate py37env
   (py37env) $ 

環境を指定すると、プロンプトに ``(py37env)`` と環境名が表示されます。``py37env`` 環境で ``python`` コマンドを実行すると、Python 3.7が実行されます。

conda環境を終了するときは、``conda deactivate`` コマンドを実行します。

.. code-block::

   (py37env) $ conda deactivate
   $ 




Conda パッケージのインストール
++++++++++++++++++++++++++++++++++++++

``conda install`` コマンドを使って、`ANACONDA PACKAGE LIST <https://docs.continuum.io/anaconda/packages/pkg-docs>`_ の Pythonパッケージをインストールできます。

.. code-block::

   C:\Users\user1>conda install idna
   Fetching package metadata ...........
   Solving package specifications: .
   …


複数バージョンの共存
++++++++++++++++++++++++++++++++++++++

Conda環境にインストールしたパッケージは、環境内でのみ利用できます。プロジェクトごとに専用のConda環境を用意しておけば、あるプロジェクトでは TensorFlow のバージョン1.9を利用し、別のプロジェクトでは TensorFlowの1.12を利用する、のような切り替えを簡単に実現できます。


