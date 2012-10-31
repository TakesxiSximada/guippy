#-*- coding: utf-8 -*-
"""ユーティリティとなる関数やクラス

ここにあるものはパッケージに依存しないものです。
パッケージにすればいいのですが、量が少ないので
ここに定義しています。
"""
import os

class Enum(object):
    """C言語のenumのような使い方が出来る
    """

    DEFAULT_INCREMENT = lambda x: x+1

    def __init__(self, default=0, increment=None):
        self.cur = default # current value
        self.increment = increment\
            if increment is not None else lambda x: x+1
#self.DEFAULT_INCREMENT
    
    def next(self, value=None, increment=None):
        if value is not None:
            self.cur = value
            
        if increment is not None:
            self.increment = increment

        cur = self.cur
        self.cur = self.increment(self.cur)
        return cur

enum = lambda *args, **kwds: Enum(*args, **kwds).next

_MD = enum() # mkdir return code
class Mkdir(object):
    """ディレクトリ作成用ユーティリティ

    先頭のMは小文字でも良かったのですが、PEPに則り大文字にしました。
    小文字のユーティリティは別のところで準備することにしました。
    """

    SUCCESS = _MD() 
    FAIL = _MD()    

    @classmethod
    def p(cls, path):
        """ディレクトリ作成に失敗しても例外を発生させない
        
        既に作成されたディレクトリに対し作成関数をcallすると例外が発生します。
        それがウザいことがあるので例外を発生させないものを作成しました。
        
        pの名前は'mkdir -p'の-pからとっています。
        失敗したかはリターンコードで判別できます。
        SUCCESSが返った時は成功しています。
        FAILが返った時は何らかの例外が発生した事を意味します。
        """
        try:
            os.makedirs(path)
        except (IOError, OSError, WindowsError), err:
            return cls.FAIL
        else:
            return cls.SUCCESS
del _MD

## 'mkdir -p'に似た感じで使えるように小文字も準備しました
## こんな感じで使ってください。 'mkdir.p(PATH)'
## きっとソースが綺麗になります。
mkdir = Mkdir 
              
