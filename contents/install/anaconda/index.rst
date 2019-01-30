Anaconda 
-----------------------------------

`Anaconda <https://www.continuum.io/>`__ はデータサイエンス向けのPythonパッケージなどを提供するプラットフォームです。科学技術計算などを中心とした、多くのモジュールやツールのコンパイル済みバイナリファイルを提供しており、簡単にPythonを利用する環境を構築できます。

Pythonのパッケージだけではなく、他言語のライブラリやいろいろなユーティリティも提供しており、NvidiaのGPUを利用する場合に必要な、CUDAなどの環境も簡単にインストールできるようになっています。

Anacondはパッケージ管理ツールとして :jinja:`{{ page.link_to('./conda.rst', text='Conda コマンド') }}` を提供しています。 `Python公式サイト <http://www.python.org>`_ の Pythonでは、パッケージは `pipコマンド <https://pypi.org/project/pip/>`__ を使ってインストールしますが、Anacondaのパッケージは、Conda コマンドでAnacondaが管理・運用する専用のリポジトリからダウンロードし、Conda環境にインストールします。


また、標準のPythonでは、:jinja:`{{ page.link_to('../windows/venv.rst', text='仮想環境')}}` の管理は `venv <https://docs.python.org/ja/3.6/library/venv.html#module-venv>`__ モジュールで行いますが、Anacondaでは、仮想環境も Codnaコマンドで提供しています。
