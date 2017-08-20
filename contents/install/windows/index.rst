
Windows環境のPython
--------------------------------

Windowsでは、PythonはOSに添付されていないため、自分でパッケージをダウンロードして、インストールする必要があります。

Windowsでよく使われるPythonのパッケージに、次の2種類があります。

- `Python.org 公式パッケージ <https://www.python.org/downloads/>`_

  Pythonの開発元で作成した、公式のパッケージです。Pythonインタープリタと標準モジュール・ドキュメントをインストールします。

  一般的なアプリケーション・Web開発やシステム管理ツールとしてPythonを利用する場合は、公式パッケージで問題ありません。

:jinja:`{{ content.load('/install/about_anaconda.rst').html }}`


.. jinja::

   <div class="card">
     <div class="card-block">
       <h2 style='margin: 0; text-align: center;'>
         {{ content.link_to('./official/install_py.rst', text='公式パッケージのインストール手順') }}
       </h2>
     </div>
   </div>

   <br>

   <div class="card">
     <div class="card-block">
       <h2 style='margin: 0; text-align: center;'>
         {{ content.link_to('./anaconda/install_anaconda.rst', text='Anaconda のインストール手順') }}
       </h2>
     </div>
   </div>

