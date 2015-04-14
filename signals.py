#!/usr/bin/env python
#coding=utf-8

__author__ = 'louis'

from blinker import Namespace

signals = Namespace()

comment_added = signals.signal("comment-added")
comment_deleted = signals.signal("comment-deleted")