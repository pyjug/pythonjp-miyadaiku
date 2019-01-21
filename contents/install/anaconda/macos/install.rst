MacOS 版のインストール
-----------------------------------



パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.anaconda.com/download/ より、パッケージをダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('./download.png')) }}`


最新パッケージとして、Python 3.x と Python 2.7.x がダウンロードできます。特別な理由がなければ、Python 3.x (上図では Python 3.6) をインストールします。


パッケージのインストール
+++++++++++++++++++++++++++++

ダウンロードしたパッケージを実行し、インストールを開始します。


:jinja:`{{ utils.enlarge_image(content.load('./install1.png')) }}`


:jinja:`{{ utils.enlarge_image(content.load('./install2.png')) }}`

:jinja:`{{ utils.enlarge_image(content.load('./install3.png')) }}`

:jinja:`{{ utils.enlarge_image(content.load('./install4.png')) }}`

:jinja:`{{ utils.enlarge_image(content.load('./install5.png')) }}`


.. target:: conda_conf

condaコマンドの設定
+++++++++++++++++++++++++++++

利用しているシェルがbashの場合は、自動的に ``conda`` が利用できるように設定され、デフォルトのConda環境である ``base`` が有効になります。

zshなど、bash以外のシェルを利用している場合は、以下のようにcondaコマンドを設定します。

.. code-block:: bash

   # bashの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc

   # zshの場合
   $ echo "source ~/anaconda3/etc/profile.d/conda.sh" >> ~/.zshrc

   # fishの場合
   $ echo "source ~/anaconda3/etc/fish/conf.d/conda.fish" >> ~/.config/fish/config.fish

Conda環境については、:jinja:`{{ content.link_to('../conda.rst') }}` を参照してください。

