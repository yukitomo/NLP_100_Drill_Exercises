#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse
usage = u'%prog [-c] [-u MAIL_ADDRESS] [-p PASSWORD] sm??????'
version = u'%prog 0.0'
parser = optparse.OptionParser(usage=usage, version=version)
parser.add_option(
        '-u', '--user',
        action='store',
        type='string',
        help=u'ログインユーザー名（メールアドレス）',
        metavar='MAIL_ADDRESS',
        )
parser.add_option(
        '-p', '--password',
        action='store',
        type='string',
        help=u'ログインユーザー名に対応するパスワード',
        )
parser.add_option(
        '-c', '--comment',
        action='store_true',
        help=u'コメント XML を取得する',
        )
parser.set_defaults(
        user='xxxxxxxx@xxx.jp',
        password='',
        comment=False,
        )

options, args = parser.parse_args()

print args
print options