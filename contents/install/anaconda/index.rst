Anaconda 
-----------------------------------

`Anaconda <https://www.continuum.io/>`_ はデータサイエンス向けのPythonパッケージなどを提供するプラットフォームです。科学技術計算などを中心とした、多くのモジュールやツールのコンパイル済みバイナリファイルを提供しており、簡単にPythonを利用する環境を構築できます。

Pythonのパッケージだけではなく、他言語のライブラリやいろいろなユーティリティも提供しており、NvidiaのGPUを利用する場合に必要な、CUDAなどの環境も簡単にインストールできるようになっています。

`python公式サイト <http://www.python.org>`_ などのPythonを利用する場合は、`pipコマンド <https://pypi.org/project/pip/>`_ でパッケージを `PyPIサーバ <https://pypi.org/>`_ からダウンロードし、`venv <https://docs.python.org/3/library/venv.html>`_ で作成した仮想環境にインストールして使用します。

Anacondaは、``pip`` コマンドと ``venv`` 両方と同等な機能を :jinja:`{{ page.link_to('./conda.rst', text='Conda コマンド') }}` で提供しています。Condaは、PyPIではなく、Anacondaが運営する独自のパッケージリポジトリからダウンロードして、Conda環境にインストールします。

Anacondaは、``pip`` コマンドと ``venv`` 両方と同等な機能を :jinja:`{{ page.link_to('./conda.rst', text='Conda コマンド') }}` で提供しています。Condaは、PyPIではなく、Anacondaが運営する独自のパッケージリポジトリからダウンロードしてインストールします。Anacondaのリポジトリに含まれていないパッケージを利用するときは、``pip`` コマンドでPyPIサーバからインストールする必要があります。
