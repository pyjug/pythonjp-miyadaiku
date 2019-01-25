

2. ソースコードのダウンロード
+++++++++++++++++++++++++++++++++++++++++++++++++

https://www.python.org/downloads より、パッケージをダウンロードします。利用するPythonのバージョンを選択します。特別な理由がなければ、最新版のPython (下図では Python 3.7.2) をクリックします。


:jinja:`{{ utils.enlarge_image(content.load('./python-download-versions.png')) }}`


画面の一番下に、ダウンロード可能なファイルが表示されますので、「**Gzipped source tarball**」をダウンロードします。


:jinja:`{{ utils.enlarge_image(content.load('./python-download-filelist.png')) }}`


ダウンロードしたファイルは、次のコマンドで解凍します。

.. code-block:: bash

   $ tar xzf Python-3.7.2.tgz


3. ビルド
+++++++++++++++++++++++++++++++++++++++++++++++++

次のコマンドで、Pythonをビルドしてインストールします。


.. code-block:: bash

   $ cd Python-3.7.2
   $ ./configure --enable-shared
   $ make
   $ sudo make install
   $ sudo ldconfig

ビルドしたコマンドは ``/usr/local/bin`` にインストールされ、``python3.7`` コマンドまたは ``python3`` コマンドで起動できます。

