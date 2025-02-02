# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2020-2021 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from pkg_resources import parse_version
from sphinx.__init__ import __version__ as sphinx_version
from tests.lib import build_sphinx
from tests.lib import parse
from tests.lib import prepare_conf
import os
import unittest


class TestConfluenceSphinxAlignment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # skip alignment tests pre-sphinx 2.1 as 'default' hints do not exist
        if parse_version(sphinx_version) < parse_version('2.1'):
            raise unittest.SkipTest('default hints not supported in sphinx')

        cls.config = prepare_conf()
        test_dir = os.path.dirname(os.path.realpath(__file__))
        cls.dataset = os.path.join(test_dir, 'datasets', 'common')
        cls.filenames = [
            'alignment',
        ]

    def test_storage_sphinx_alignment_center(self):
        config = dict(self.config)
        config['confluence_default_alignment'] = 'center'

        out_dir = build_sphinx(self.dataset, config=config,
            filenames=self.filenames)

        with parse('alignment', out_dir) as data:
            image = data.find('ac:image')
            self.assertIsNotNone(image)
            self.assertTrue(image.has_attr('ac:align'))
            self.assertEqual(image['ac:align'], 'center')

    def test_storage_sphinx_alignment_default(self):
        out_dir = build_sphinx(self.dataset, config=self.config,
            filenames=self.filenames)

        with parse('alignment', out_dir) as data:
            image = data.find('ac:image')
            self.assertIsNotNone(image)
            self.assertTrue(image.has_attr('ac:align'))
            self.assertEqual(image['ac:align'], 'center')

    def test_storage_sphinx_alignment_left(self):
        config = dict(self.config)
        config['confluence_default_alignment'] = 'left'

        out_dir = build_sphinx(self.dataset, config=config,
            filenames=self.filenames)

        with parse('alignment', out_dir) as data:
            image = data.find('ac:image')
            self.assertIsNotNone(image)
            self.assertTrue(image.has_attr('ac:align'))
            self.assertEqual(image['ac:align'], 'left')

    def test_storage_sphinx_alignment_right(self):
        config = dict(self.config)
        config['confluence_default_alignment'] = 'right'

        out_dir = build_sphinx(self.dataset, config=config,
            filenames=self.filenames)

        with parse('alignment', out_dir) as data:
            image = data.find('ac:image')
            self.assertIsNotNone(image)
            self.assertTrue(image.has_attr('ac:align'))
            self.assertEqual(image['ac:align'], 'right')
