Linux版 のインストール
-----------------------------------


パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.anaconda.com/download/ より、パッケージをダウンロードします。

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


.. target:: conda_conf

condaコマンドの設定
+++++++++++++++++++++++++++++
   

途中で、

    |   Do you wish the installer to initialize Anaconda3
    |   in your /home/user1/.bashrc ? [yes|no]

という選択肢が表示されます。

ここでは、デフォルトの ``no`` が既存のシステムへの影響が少なく、おすすめです。手動で次のコマンドを実行して、``conda`` コマンドを有効にしましょう。

.. code-block:: bash

   # bashの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc

   # zshの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.zshrc

   # fishの場合
   $ echo "source ~/anaconda3/etc/fish/conf.d/conda.fish" >> ~/.config/fish/config.fish


ここで ``yes`` と指定した場合は、bashを利用している環境では自動的にデフォルトのConda環境である ``base`` がアクティブとなります。

Conda環境については、:jinja:`{{ content.link_to('../conda.rst') }}` を参照してください。

