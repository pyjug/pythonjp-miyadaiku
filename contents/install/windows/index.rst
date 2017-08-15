
Windows環境のPython
--------------------------------

Windowsでは、PythonはOSに添付されていないため、自分でパッケージをダウンロードして、インストールする必要があります。

Windowsでよく使われるPythonのパッケージに、次の2種類があります。

- `Python.org公式パッケージ <https://www.python.org/downloads/>`_

  Pythonの開発元で作成した、公式のパッケージです。Pythonインタープリタと標準モジュール・ドキュメントをインストールします。


- `Anaconda <https://www.continuum.io/>`_

  データサイエンス向けに作成されたパッケージで、公式パッケージに加えて、科学技術計算などを中心とした数多くのモジュールやツールが独自の形式で同梱されています。


一般的なアプリケーション・Web開発やシステム管理ツールとしてPythonを利用する場合は、公式パッケージでも問題ありません。

データサイエンス・機械学習などを中心としてPythonを使用するなら、多くのモジュールがデフォルトでインストールされるAnacondaは便利です。特に、プログラミングが専門ではない研究者などのユーザにとっては、環境構築の手間を大きく省けます。

しかし、Anacondaは一部に独自技術を使用しているため、公式パッケージでは一般的に使用されているツールなどでも、Anaconda では利用できないものがあります。Anacondaを利用する場合には、慣れるまではできるだけAnacondaが提供する環境だけを利用するように心がけたほうが良いかもしれません。



.. jinja::

   <div class="card">
     <div class="card-block">
       <h4 class="card-title">{{ content.link_to('./install_py.rst') }}</h4>
     </div>
   </div>

   <br>

   <div class="card">
     <div class="card-block">
       <h4 class="card-title">{{ content.link_to('./install_anaconda.rst') }}</h4>
     </div>
   </div>

