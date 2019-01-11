
Conda コマンド
--------------------------------

Anaconda には `conda <https://conda.io/docs/index.html>`_ コマンドがインストールされており、パッケージのインストールや、実行環境の作成・切り替えなどを行えます。

.. note::

   macOS、Linux では、conda コマンドの実行環境を設定する必要があります。macOSの場合は :jinja:`{{ content.link_to('macos/install.rst', fragment='conda_conf', text='macOSの設定') }}`、Linuxの場合は  :jinja:`{{ content.link_to('unix/install.rst', fragment='conda_conf', text='Linuxの設定') }}` を参照してください。

LinuxやmacOSでは ``conda`` コマンドはシェルの関数となっており、Anacondaのインストール先に ``PATH`` 環境変数を設定せずとも使用できるようになっています。


Windows環境では、スタートメニューの「**Anaconda3(64bit)** | **Anaconda Prompt**」で表示されるコマンドプロンプトから、condaコマンドを実行できます。



:jinja:`{{ utils.enlarge_image(content.load('./win-start-menu.png')) }}`


Conda環境
=======================================

Conda環境は独立したPythonの実行環境で、他の環境に影響を与えずにPythonのバージョンを用途によって切り替えたり、パッケージをインストールしたりできます。Anacondaをインストールすると、デフォルトのConda環境として ``base`` が利用できます。

AnacondaのPythonを利用するときは、Conda環境を有効にしてからコマンドを実行します。Conda環境は、``conda activate`` コマンドで開始します。


.. code-block::

   $ conda activate
   (base) $ 

環境名を指定せずに ``conda activate`` コマンドを実行すると、デフォルトのConda環境である ``base`` 環境が有効になります。

Conda環境を有効にして ``python`` コマンドを実行すると、システムにインストールされた Python ではなく、AnacondaでインストールされたPythonが実行されます。Pythonだけではなく、Anacondaに同梱された各種のアプリケーションも利用可能になります。

.. code-block:: bash

   $ python --version
   Python 2.7.15
   $ conda activate  # Conda環境を開始
   (base) $ python --version
   Python 3.7.1


Conda環境の作成
++++++++++++++++++++++++++++++++++++++

新しい環境は、 ``conda create`` コマンドで作成します。
次の例では、``base`` 環境をもとに、Python3.7を利用する、``py37env`` という名前の環境を作成します。

.. code-block::

   $ conda create --name py37env --clone base python=3.7
   Fetching package metadata ...........
   Solving package specifications:
   Package plan for installation in environment C:\Users\user1\Anaconda3\envs\env1:

   Proceed ([y]/n)? y
   …

ここでは、``--clone base`` と、デフォルトのConda環境である ``base`` をコピー元として指定しています。コピー元を指定せずに作成したConda環境には、``numpy`` や ``jupyter`` などの汎用的なパッケージも一切含まれておらず、あまりAnaconda環境としては便利ではありません。``base`` か、または好きな環境をコピー元として指定するようにしましょう。


Conda環境の切り替え
++++++++++++++++++++++++++++++++++++++

``py37env`` 環境を使うときには、``conda activate`` コマンドで環境名を指定します。

.. code-block::

   $ conda activate py37env
   (py37env) $ 

Conda環境を切り替えると、プロンプトに ``(py37env)`` と環境名が表示されます。``py37env`` 環境で ``python`` コマンドを実行すると、指定された Python 3.7 が実行されます。


conda環境を終了するときは、``conda deactivate`` コマンドを実行します。

.. code-block::

   (py37env) $ conda deactivate
   $ 




Conda パッケージのインストール
++++++++++++++++++++++++++++++++++++++

``conda install`` コマンドを使って、`ANACONDA PACKAGE LIST <https://docs.continuum.io/anaconda/packages/pkg-docs>`_ の Pythonパッケージを Conda環境にインストールできます。

.. code-block::

   C:\Users\user1>conda install idna
   Fetching package metadata ...........
   Solving package specifications: .
   …


.. caution::

   Conda環境でも、`python公式サイト <http://www.python.org>`_ などが配布するPythonと同じように、``pip`` コマンドを使ってパッケージを `PyPI <https://pypi.org>`_ からインストールすることもできます。

   しかし、``pip`` でインストールされるパッケージは Anaconda が管理するパッケージではないため、うかつに使用すると不具合が発生する場合があります。

   慣れるまでは、できるだけ Condaだけを使ってパッケージをインストールするようにしましょう。




複数バージョンの共存
++++++++++++++++++++++++++++++++++++++

Conda環境にインストールしたパッケージは、環境内でのみ利用できます。プロジェクトごとに専用のConda環境を用意しておけば、あるプロジェクトでは TensorFlow のバージョン1.9を利用し、別のプロジェクトでは TensorFlowの1.12を利用する、のような切り替えを簡単に実現できます。


