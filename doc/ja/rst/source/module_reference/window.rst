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

.. data:: width

   ウィンドウの横幅を取得、設定します。代入することで、ウィンドウサイズの変更まで行います。

.. data:: height

   ウィンドウの縦幅を取得、設定します。代入することで、ウィンドウサイズの変更まで行います。
   
.. method:: __init__(self, cname=None, wname=None, hwnd=None)

   :class:`Window` を初期化します。 :data:`cname` にはターゲットとするウィンドウの
   クラス名を渡します。 :data:`wname` にはターゲットとするウィンドウのキャプションを
   渡します。 :data:`cname` と :data:`wname` は入力した場合、
   catch()するためのデフォルト値として使用します。省略可能です。
   Windowの制御はcatch()しなければなりません。

   :data:`hwnd` にはファイルハンドルを渡します。入力した場合、catch()しなくても
   ウィンドウを制御できます。なぜならcatch()とは :data:`hwnd` を取得する操作ですから。
   省略した場合、 ウィンドウを制御するためには、事前にcatch()しなければなりません。

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

.. method:: move(self, left, top):

   ウィンドウを移動します。leftにはウィンドウの左端の座標を指定します。
   topにはウィンドウの上端の座標を指定します。

.. method:: resize(self, width=None, height=None)

   ウィンドウのサイズを変更します。widthにはウィンドウの横幅を指定します。
   省略した場合、現在の値が使用されます。
   heightにはウィンドウの高さを指定します。省略した場合、現在の値が使用します。

.. method:: close(self)

   ウィンドウを閉じます。

.. method:: get_rect(self, normalize=True)

   上下左右の座標を取得します。この関数は `ctypes.wintypes.RECT` オブジェクトを返します。上下左右の値は `RECT.top` , `RECT.bottom` , `RECT.left` , `RECT.right` でアクセスします。normalizeはTrueかFalseを渡します。Trueの時は座標値は標準化します。Falseの時は座標値はそのまま渡されます。

.. method:: set_rect(self)

   ウィンドウのサイズを変更します。未サポートです。今後もサポートされる予定はありません。
   ウィンドウのサイズ変更には :method:`resize` を使用してください。

.. method:: get_cname(self)

   補足しているウィンドウのクラス名を取得します。
   クラス名が長すぎる場合、TooLongエラーが送出されます。
   クラス名の長さは最長で :data:`BUFFER_LEN` * 5 です。
   ウィンドウを補足していない場合の動作は未定義です。

.. method:: get_wname(self):

   補足しているウィンドウのキャプションを取得します。
   キャプションが長すぎる場合、TooLongエラーが送出されます。
   キャプションの長さは最長で :data:`BUFFER_LEN` * 5 です。
   ウィンドウを補足していない場合の動作は未定義です。

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
