
macOS環境のPython
--------------------------------

macOS Sierra では、Python 2.7 がインストールされています。しかし、Python 2.x はもう古いリリースで、あまり推奨できません。

また、そのままのmacOS環境では、他のライブラリを使用した拡張モジュールのインストールなどが難しくなるため、なんらかのパッケージマネージャを利用して、その管理下で Python 環境を整備することをおすすめします。


macOS でよく使われるパッケージとして、次の2種類を紹介します。

- `Homebrew パッケージマネージャ <https://brew.sh/>`_

  macOS でよく使われるパッケージマネージャで、Python だけではなく、他の多くのアプリケーションの管理を行います。


:jinja:`{{ content.load('/install/about_anaconda.rst').html }}`


.. jinja::

   <div class="card">
     <div class="card-block">
       <h2 style='margin: 0; text-align: center;'>
         {{ content.link_to('./brew/install.rst', text='Homebrewによるインストール手順') }}
       </h2>
     </div>
   </div>

   <br>

   <div class="card">
     <div class="card-block">
       <h2 style='margin: 0; text-align: center;'>
         {{ content.link_to('./anaconda/install.rst', text='Anaconda のインストール手順') }}
       </h2>
     </div>
   </div>

