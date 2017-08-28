
macOS環境のPython
--------------------------------

macOS Sierra では、Python 2.7 がインストールされています。しかし、Python 2.x はもう古いリリースで、あまり推奨できません。

また、そのままのmacOS環境では、他のライブラリを使用した拡張モジュールのインストールなどが難しくなるため、なんらかのパッケージマネージャを利用して、その管理下で Python 環境を整備することをおすすめします。


ここでは、代表的な macOS 用パッケージマネージャである `Homebrew <https://brew.sh/>`_ を使ってPython をインストールする手順を紹介します。


Homebrewのインストール
===========================

LaunchPadから **ターミナル** を起動し、次のコマンドを入力します。

.. code-block:: console

   $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ==> This script will install:
   /usr/local/bin/brew
   /usr/local/share/doc/homebrew
   /usr/local/share/man/man1/brew.1
   /usr/local/share/zsh/site-functions/_brew
   /usr/local/etc/bash_completion.d/brew
   /usr/local/Homebrew
   …



Python3 のインストール
===========================

**ターミナル**  で、次のコマンドを入力します。

.. code-block:: console

   $ brew install python3
   ==> Installing dependencies for python3: readline, sqlite, gdbm, openssl, xz
   ==> Installing python3 dependency: readline
   ==> Downloading https://homebrew.bintray.com/bottles/readline-7.0.3_1.sierra.bot
   ######################################################################## 100.0%
   …


インストールしたPythonは、``python3`` コマンドで実行できます。

.. code-block::

   $ python3
   Python 3.6.1 (default, Apr  4 2017, 09:40:21)
   [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>>


Python2 のインストール
===========================

**ターミナル**  で、次のコマンドを入力します。

.. code-block:: console

   $ brew install python2
   ==> Downloading https://homebrew.bintray.com/bottles/python-2.7.13_1.sierra.bottle.tar.gz
   ######################################################################## 100.0%
   ==> Pouring python-2.7.13_1.sierra.bottle.tar.gz
   ==> /usr/local/Cellar/python/2.7.13_1/bin/python2 -s setup.py --no-user-cfg install --force --verbose --single-version-ex
   …

インストールしたPythonは、``python`` コマンドや ``python2`` コマンドで実行できます。

.. code-block::

   $ python
    Python 2.7.13 (default, Apr  4 2017, 08:47:57)
    [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
