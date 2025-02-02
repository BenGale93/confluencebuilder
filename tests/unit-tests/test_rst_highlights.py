# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2020-2021 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from tests.lib import build_sphinx
from tests.lib import parse
from tests.lib import prepare_conf
import os
import unittest


class TestConfluenceRstHighlights(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = prepare_conf()
        test_dir = os.path.dirname(os.path.realpath(__file__))
        cls.dataset = os.path.join(test_dir, 'datasets', 'common')
        cls.filenames = [
            'highlights',
        ]

    def test_storage_rst_highlights(self):
        out_dir = build_sphinx(self.dataset, config=self.config,
            filenames=self.filenames)

        with parse('highlights', out_dir) as data:
            quote = data.find('blockquote')
            self.assertIsNotNone(quote)

            parts = list(quote.children)
            self.assertEqual(len(parts), 2)

            self.assertEqual(parts[0].text.strip(), 'quote')
            self.assertEqual(parts[1].strip(), '-- source')
