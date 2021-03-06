# -*- coding: utf-8 -*-
# Copyright 2015 Christoph Reiter
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

import os

from tests import TestCase, DATA_DIR
from quodlibet.formats.mp3 import MP3File


class TMP3File(TestCase):

    def setUp(self):
        self.song = MP3File(os.path.join(DATA_DIR, 'silence-44-s.mp3'))
        self.song2 = MP3File(os.path.join(DATA_DIR, 'test.mp2'))
        self.song3 = MP3File(os.path.join(DATA_DIR, 'lame.mp3'))

    def test_length(self):
        self.assertAlmostEqual(self.song("~#length"), 3.0, 1)
        self.assertAlmostEqual(self.song2("~#length"), 1.764, 3)
        self.assertAlmostEqual(self.song3("~#length"), 0.0616, 3)

    def test_bitrate(self):
        self.failUnlessEqual(self.song("~#bitrate"), 32)
        self.failUnlessEqual(self.song2("~#bitrate"), 32)
        self.failUnlessEqual(self.song3("~#bitrate"), 270)

    def test_format(self):
        self.assertEqual(self.song("~format"), "MP3")
        self.assertEqual(self.song2("~format"), "MP2")
        self.assertEqual(self.song3("~format"), "MP3")

    def test_codec(self):
        self.assertEqual(self.song("~codec"), "MP3")
        self.assertEqual(self.song2("~codec"), "MP2")
        self.assertEqual(self.song3("~codec"), "MP3")

    def test_encoding(self):
        self.assertEqual(self.song("~encoding"), "")
        self.assertEqual(self.song2("~encoding"), "")
        self.assertEqual(self.song3("~encoding"), "LAME 3.99.1+\nVBR")
