
仮想環境
-----------------------------------

.. jinja::

   {{ content.load('/install/why_virtualenv.rst').html }}



Virtualenvは、:jinja:`{{ content.link_to('./pip.rst') }}` コマンドでインストールできます。

.. code-block::

   $ pip3 install virtualenv


Virtualenvのコマンド
=========================


.. jinja::

   {{ content.load('/install/virtualenv_unix.rst').html }}


Virtualenvwrapper
=========================

.. jinja::

   {{ content.load('/install/virtualenvwrapper.rst').html }}
