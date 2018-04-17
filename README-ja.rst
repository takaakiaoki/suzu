====
SUZU
====

version 0.4.0

April 17, 2018

Takaaki AOKI (aoki.takaaki.6v@kyoto-u.ac.jp)

`English <README.html>`_

.. contents::
  :local:

SUZU について
==============

SRIM (http://www.srim.org/) は高速粒子の飛跡並びに照射効果のシミュレーションソフトウェアとして最も有名なものです.
SRIM には TIN.exe というパラメータセットアップの為のGUIプログラムが有りますが, このプログラムは, 日本語, 中国語, 等々のマルチバイト環境でのwindows上では正しく動作しないことがあります.
SUZU (tin==錫)は TIN.exe と同等の機能を提供し, これらのWindows (そして他のOSプラットホーム)上で動作することを目指しています.

インストールと実行
===================

Windowsでは2通りのインストール方法があります. また後者は unix や mac にも適用出来ます.

オプション1: 実行ファイルのインストール (Windows用)
---------------------------------------------------------

1. .exe ファイルを取得

  http://sakura.nucleng.kyoto-u.ac.jp/~aoki/suzu/dist より
  suzu-(version)-win32.exe, または suzu-(version)-win-amd64.exe をダウンロードし,
  これらを実行します. 実行ファイルは c:\\Program Files\\suzu といったフォルダに展開され, またスタートメニューにエントリが追加されます.

2. 実行

  1.でセットアップしたフォルダ内の suzu.exe をダブルクリック, 実行します.

オプション2: Python のスクリプト, ライブラリとしてインストール
----------------------------------------------------------------

もう一つの方法は suzu を python のライブラリとしてインストールする方法です.

バージョン0.1.0以降の suzu は python 3.3.5 (またはそれ以上) で動作します.  http://www.python.org/ からpython 本体を入手インストールしてください.

PyPI (https://pypi.org/project/suzu/) に公開されているパッケージを pip によりインストールします.

.. code-block::

    pip install suzu


実行
++++++

- コマンドラインより 

  .. code-block:: 

    suzu 
   
  とタイプします.

- あるいは, suzu の実行ファイルを見つけ(例えば. C:\\Python33\\Script\\suzu.exe に見つかります.), これを実行します.


ソースコードの入手
==================

ソースコードは https://github.com/takaakiaoki/suzu で公開しています.

git (https://git-scm.com/) で管理しているので, 最新のソースコードが必要な場合,

.. code-block:: console

   git clone https://github.com/takaakiaoki/suzu.git

または

.. code-block:: console

   git clone git@github.com/takaakiaoki/suzu.git

で取得出来ます(あるいはご自身のレポジトリにForkしてください).

利用方法
===========

[Save (&Run Trim)]
-------------------

通常, 必要なパラメータを入力, 選択し [Save (& Run Trim)] ボタンを押します.

この時, ファイル名を 'TRIM.in' という名称とし, かつ TRIM.exe が存在する
(== SRIM がセットアップされた)フォルダに保存した場合, 
ファイルの保存に引き続き, TRIM.exe によるシミュレーションを実施してよいかの確認ダイアログが表示されます.

[Load .json]
------------

現行バージョン suzu では, 標準的なTRIM.exe への入力ファイル (TRIM.in) を読むことはできません. その代わり, suzu は上記の[Save (&Run Trim)] ボタンを押したときに, TRIM.in に加えて TRIM.in.json というファイルを保存します.
[Load .json] ボタンはこの .json データを選択, ロードします.

[Validate]
----------

[Validate] ボタンを押すと入力された内容のテストを行います. 問題が有れば, ダイアログを表示するとともに, 該当箇所を赤色で表示します. この操作は [Save (&Run Trim)] ボタンを押した際にも自動的に実施されます.

.. note::

  値の検査は自動的には実施されません. ユーザーは必要に応じて自発的に
  [Validate] ボタンにより, 変更されたパラメータの内容を確認する
  必要があります.

[Compound DB]
-------------

[Compount DB] ボタンは "target layer" の枠内にあります. このボタンを押すと,
SRIM で提供されている材料データベースにアクセスできます.

データベースの表示画面では, 最初にデータベースファイルを指定します.
At database dialog, indicate the path to compound.dat (usually, [SRIM INSTALL PATH]/DATA/Compound.dat). You may construct your own database.


Other Buttons
-------------

[Set Example] [Dump to Console] [Clear] buttons still remains for debugging.

More Information
================

Detail information especially for developers are found in dummy_tin/doc/* (python script package).


Bugs, issues, discussion for developers
=======================================

The author is pleased to here bug & issue reports and suggest & request for the software.
