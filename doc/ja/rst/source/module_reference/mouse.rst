============================================
:mod:`guippy.mouse` --- マウスの操作
============================================

.. module:: guippy.mouse
   :synopsis: マウスの操作

.. sectionauthor:: Tak Esxima

:mod:`guippy.mouse` はマウスを操作する機能を用意しています。

.. attribute:: LEFT

   マウスの左ボタン用の値です。

.. attribute:: MIDDLE

   マウスの中ボタン用の値です。

.. attribute:: RIGHT

   マウスの右ボタン用の値です。

.. attribute:: DEFAULT_ABSOLUTE

   マウスポインタの座標の指定方法のデフォルト値です。Trueに設定しています。Trueであれば絶対値での座標指定です。画面の左上が(0, 0)の座標値を利用します。Falseであれば、相対値でのザ行指定です。現在のマウスポインタの位置が(0, 0)の座標値を利用します。

.. attribute:: DEFAULT_NORMALIZE

   マウスポインタの座標を指定方法のデフォルト値です。Trueに設定しています。Trueであれば正規化した値を使用します。画面の座標値を0～0xFFFFで正規化した値を使用します。Falseであれば正規化していない座標値を使用します。その場合、座標値はシステムメトリクスから影響を受けます。

.. function:: _mouse_event(code, xx=0, yy=0, wheel=0, flag=0)

   :func:`api.mouse_event` にデフォルト値を与えるための関数です。

.. function:: call_mouse_event()

   :func:`_mouse_event` を呼び出すためのデコレータです。デコレートされたメソッドを実行し、戻り値を :func:`_mouse_event` に渡して実行します。従ってこのデコレータでデコレートされたメソッドは :func:`_mouse_event` に渡すための引数を返さなければなりません。

.. class:: Button

   マウスのボタンを操作するクラスです。

.. class:: Position

   マウスポインタを操作するためのクラスです。

.. class:: Mouse

   マウスの全てを操作するためのクラスです。 :class:`Button` と :class:`Position` を継承しています。

:class:`Button` クラス
============================
マウスのボタンを操作するクラスです。

.. method:: drag(cls, button=None)

   マウスをドラッグします。buttonには :attr:`LEFT` か :attr:`MIDDLE` か :attr:`RIGHT` を指定します。省略すると :attr:`LEFT` が使われます。このメソッドを呼ぶとドラッグしっ放しになります。しっ放しになったドラッグを戻すためには :func:`drop` を使用します。

.. method:: drop(cls, button=None)

   マウスをドロップします。 buttonには :attr:`LEFT` か :attr:`MIDDLE` か :attr:`RIGHT` を指定します。省略すると :attr:`LEFT` が使われます。このメソッドは  :func:`drag` を先に実行しないと無意味です。


.. method:: click(cls, button=None)

   マウスをクリックします。buttonには :attr:`LEFT` か :attr:`MIDDLE` か :attr:`RIGHT` を指定します。省略すると :attr:`LEFT` が使われます。

.. method:: wclick(cls, button=None)

   マウスをダブルクリックします。引数、戻り値は :func:`click` と同じです。

.. method:: wheel(cls, num=1)

   マウスの中ボタンを回します。回す量はnumで指定します。

:class:`Position` クラス
==============================

マウスポインタを動かすためのクラスです。

.. method:: jump(cls, xx, yy, normalize=DEFAULT_NORMALIZE, absolute=DEFAULT_ABSOLUTE)

   マウスポインタを動かします。xxとyyには座標値を渡します。normalizeは座標の正規化をするかどうかです。absoluteは指定した座標が絶対座標なのか相対座標なのかを指定します。

.. method:: now(normalize=DEFAULT_NORMALIZE)

   マウスポインタの現在の絶対座標を取得します。normalizeがTrueの場合、座標値は正規化されます。デフォルト値は :attr:`DEFAULT_NORMALIZE` です。

:class:`Mouse` クラス
=========================

マウスを操作する関数です。 :class:`Button` と :class:`Position` を継承しています。

.. method:: point(cls, *args, **kwds)

   マウスを移動した後でクリックします。引数は :func:`jump` と同じです。

