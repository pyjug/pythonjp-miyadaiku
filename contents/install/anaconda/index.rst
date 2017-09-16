Anaconda 
-----------------------------------


`Anaconda <https://www.continuum.io/>`_ はデータサイエンス向けに作成された Pythonパッケージで、科学技術計算などを中心とした数多くのモジュールやツールが独自の形式で同梱されています。


macOSやUnix環境では、ほとんどのモジュールがコンパイル済みパッケージを提供しているため、Anaconda を使わなくとも、通常の :jinja:`{{ page.link_to('../macos/pip.rst') }}` コマンドでも簡単に環境を構築できます。

しかし、Windows環境のように、簡単にインストール可能なモジュールが提供されていない環境で、機械学習などのためにPython を使用するなら、多くのモジュールがデフォルトでインストールされる Anaconda はとても便利です。

また、Anaconda でインストールされるモジュールは、`Intel Math Kernel Library <https://software.intel.com/en-us/mkl>`_ を使ってビルドされるなどの、特定用途向けパッケージならではの工夫が加えられている場合もあります。

Anaconda は一部に独自技術を使用しているため、公式パッケージでは一般的に使用されているツールなどでも、Anaconda では利用できないものがあるため、注意が必要です。特に、Anacondaは標準的な Pythonの :jinja:`{{ page.link_to('../macos/virtualenv.rst') }}` を利用できないため、専用の :jinja:`{{ page.link_to('./conda.rst') }}` を利用する必要があります。また、Anaconda はさまざまなツールを統合してインストールするため、もともと OS が提供している機能に干渉してしまうケースもあります。

Anaconda を利用する場合には、慣れるまではできるだけ Anaconda が提供する環境だけを利用するように心がけたほうが良いかもしれません。



