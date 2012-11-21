============================================
:mod:`guippy.window` --- ウィンドウの操作
============================================

.. module:: guippy.window
   :synopsis: ウィンドウの操作

.. sectionauthor:: Tak Esxima

:mod:`guippy.window` ではウィンドウを操作するための機能を用意しています。:

.. attribute:: TIMEOUT

   ウィンドウを取得するときに使用するタイムアウトです。10秒です。 

.. class:: Window
   ウィンドウを操作するためのクラスです。

:class:`Window` オブジェクト
============================
 ウィンドウを操作するためのクラスです。サイズの変更や、座標の取得をすることができます。


.. data:: hwnd

   ファイルハンドルの値です。 catchすると値が設定されます。

.. data:: cname

   ウィンドウのクラス名です。

.. data:: wname

   ウィンドウのキャプションです。

.. method:: get_window(cname=None, wname=None, timeout=TIMEOUT)

   ウィンドウハンドルを取得します。
   cnameとwnameは取得したいウィンドウのクラス名とキャプションを渡します。
   この引数は省略可能です。
   省略した場合、現在アクティブなウィンドウのウィンドウハンドルを取得します。
   これは静的メソッドです。クラスをインスタンス化しなくても使用できます。

.. method:: catch(self, cname=None, wname=None)

   ウィンドウを捕まえます。ウィンドウは捕まえなければ操作できません。
   cnameとwnameは取得したいウィンドウのクラス名とキャプションを渡します。

.. method:: active(self)

   ウィンドウをアクティブにします。

.. method:: move(self)

   ウィンドウを移動します。未サポートです。

.. method:: close(self)

   ウィンドウを閉じます。未サポートです。

.. method:: get_rect(self, normalize=True)

   上下左右の座標を取得します。この関数は `ctypes.wintypes.RECT` オブジェクトを返します。上下左右の値は `RECT.top` , `RECT.bottom` , `RECT.left` , `RECT.right` でアクセスします。normalizeはTrueかFalseを渡します。Trueの時は座標値は標準化します。Falseの時は座標値はそのまま渡されます。

.. method:: set_rect(self)

   ウィンドウのサイズを変更します。未サポートです。

.. method:: width(self)

   ウィンドウの横幅を取得します。未サポートです。

.. method:: height(self)

   ウィンドウの縦幅を取得します。未サポートです。

.. method:: restore(self)

   最大化や最小化されていたウィンドウのサイズを元に戻します。

.. method:: maximize(self)

   ウィンドウを最大化します。

.. method:: minimize(self)

   ウィンドウを最小化します。

.. method:: get_popup(self)

   ウィンドウのポップアップウィンドウを捕まえます。成功すると :class:`Window` クラスを返します。

.. method:: get_child(self)

   ウィンドウの子ウィンドウを捕まえます。成功すると :class:`Window` クラスを返します。
