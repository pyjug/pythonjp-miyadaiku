Anaconda
-----------------------------------

:jinja:`{{ content.load('/install/about_anaconda.rst').html }}`


パッケージのダウンロード
+++++++++++++++++++++++++++++


https://www.continuum.io/downloads より、パッケージをダウンロードします。

:jinja:`{{ utils.enlarge_image(content.load('/install/anaconda-dl-linux.png')) }}`


最新パッケージとして、Python 3.x と Python 2.7.x がダウンロードできます。特別な理由がなければ、Python 3.x (上図では Python 3.6) をインストールします。


.. code-block::

   $ bash ./Anaconda3-4.4.0-Linux-x86_64.sh 
   
   Welcome to Anaconda3 4.4.0 (by Continuum Analytics, Inc.)
   
   In order to continue the installation process, please review the license
   agreement.
   Please, press ENTER to continue
   
   >>> 
   ===================================
   Anaconda End User License Agreement
   ===================================
   
   Copyright 2017, Continuum Analytics, Inc.
   
   All rights reserved under the 3-clause BSD License:
   
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
   
   …
   
   cryptography
   A Python library which exposes cryptographic recipes and primitives.
   
   Do you approve the license terms? [yes|no]
   yes
   
   Anaconda3 will now be installed into this location:
   /home/user1/anaconda3
   
     - Press ENTER to confirm the location
     - Press CTRL-C to abort the installation
     - Or specify a different location below
   
   [/home/user1/anaconda3] >>> 
   PREFIX=/home/user/anaconda3
   
   installing: python-3.6.1-2 ...
   installing: _license-1.1-py36_1 ...
   
   …
   
   Python 3.6.1 :: Continuum Analytics, Inc.
   creating default environment...
   installation finished.
   Do you wish the installer to prepend the Anaconda3 install location
   to PATH in your /home/user1/.bashrc ? [yes|no]
   [no] >>> yes

   Prepending PATH=/home/user1/anaconda3/bin to PATH in /home/user1/.bashrc
   A backup will be made to: /home/user1/.bashrc-anaconda3.bak
   
   
   For this change to become active, you have to open a new terminal.
   
   Thank you for installing Anaconda3!
   
   Share your notebooks and packages on Anaconda Cloud!
   Sign up for free: https://anaconda.org


