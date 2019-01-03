Unix版 のインストール
-----------------------------------


パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.continuum.io/downloads より、パッケージをダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('/install/anaconda-dl-linux.png')) }}`


最新パッケージとして、Python 3.x と Python 2.7.x がダウンロードできます。特別な理由がなければ、Python 3.x (上図では Python 3.6) をダウンロードします。


ダウンロードしたファイルは、次のように実行します。


.. code-block::

   # sh ./Anaconda3-2018.12-Linux-x86_64.sh
   
   Welcome to Anaconda3 2018.12
   
   In order to continue the installation process, please review the license
   agreement.
   Please, press ENTER to continue
   >>>        <------------------------------------ エンターを入力
   ===================================
   Anaconda End User License Agreement
   
   ...
   
   Do you accept the license terms? [yes|no]
   [no] >>> yes   <-------------------------------- yes を入力
   
   Anaconda3 will now be installed into this location:
   /home/user1/anaconda3
   
     - Press ENTER to confirm the location
     - Press CTRL-C to abort the installation
     - Or specify a different location below
   
   [/home/user1/anaconda3] >>>  <------------------------ エンターを入力
   PREFIX=/home/user1/anaconda3
   
   ...
   
   Do you wish the installer to initialize Anaconda3
   in your /home/user1/.bashrc ? [yes|no]
   [no] >>> <-------------------------------------- エンターを入力(下記参照)
   Initializing Anaconda3 in /home/user1/.bashrc
   A backup will be made to: /home/user1/.bashrc-anaconda3.bak
   

途中で、

    |   Do you wish the installer to initialize Anaconda3
    |   in your /home/user1/.bashrc ? [yes|no]
    
と質問されます。ここで ``yes`` と指定すると、自動的にデフォルトのConda環境である ``base`` がアクティブとなります。

ここでは、デフォルトの ``no`` を選択して設定を行わないほうが既存のシステムへの影響が少なく、おすすめです。

次のコマンドを実行して、``conda`` コマンドだけを有効にするようにしましょう。

.. code-block:: bash

   # bashの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile


Conda環境については、:jinja:`{{ content.link_to('../conda.rst') }}` を参照してください。


