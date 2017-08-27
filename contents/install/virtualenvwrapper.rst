
.. article::
   :type: snippet



Virtualenvwrapper
*******************************


`Virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_ は、広く使われている仮想環境の管理ツールで、仮想環境の生成・削除・切り替えなど行うコマンド集です。


Virtualenvwrapperのインストール
++++++++++++++++++++++++++++++++++++

``pip`` コマンドでインストールできます。

.. code-block::

   $ pip3 install Virtualenvwrapper

Shell環境設定ファイルの修正
++++++++++++++++++++++++++++++++++++

``~/.bashrc`` などのShell環境設定ファイルに、以下の設定を追加します。

.. code-block:: sh

   export WORKON_HOME=$HOME/.virtualenvs
   export PROJECT_HOME=$HOME/projects
   source `which virtualenvwrapper.sh`


ファイルを修正したら、次のコマンドで修正を適用します。

.. code-block:: sh

   $ . ~/.bashrc


Virtualenvwrapperのコマンド
++++++++++++++++++++++++++++++++++++

Virtualenvwrapper をインストールすると、次のようなコマンドを使えます。


mkvirtualenv
---------------------



仮想環境を作成します。``-p`` オプションで、使用する Python を指定できます。

.. code-block::

   $ mkvirtualenv testenv -p /usr/local/bin/python3.6
   (testenv) $ 

この例では、Python 3.6 を指定して仮想環境 ``testenv`` を作成しています。``testenv``  は、``.bashrc`` に指定した ``~/=$HOME/.virtualenvs`` に作成されます。


workon
---------------------

指定した仮想環境に切り替えます。


.. code-block::

   $ workon testenv
   (testenv) $


rmvirtualenv
---------------------

指定した仮想環境を削除します。


.. code-block::

   $ rmvirtualenv testenv


