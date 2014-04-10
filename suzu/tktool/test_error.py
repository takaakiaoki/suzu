#!/usr/bin/env python

import unittest
import itertools

from . import error

class Test_walk_errorreason(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assertion(self, qs, ans):
        for q, a in itertools.zip_longest(error.walk_errorstruct(qs), ans):
            self.assertEqual(q, a)

    def test1(self):
        qs = 'elem'
        ans = [('', 'elem')]
        self.assertion(qs, ans)


    def test2(self):
        qs = ['elem0', 'elem1', 'elem2']
        ans = [('', 'elem0'), ('', 'elem1'), ('', 'elem2')]
        self.assertion(qs, ans)

    def test3(self):
        qs = ('a', 'elem0')
        ans = [('.a', 'elem0')]
        self.assertion(qs, ans)

    def test4(self):
        qs = [('a', 'elem0'), ('a', 'elem1'), ('b', 'elem2')]
        ans = [('.a', 'elem0'), ('.a', 'elem1'), ('.b', 'elem2')]
        self.assertion(qs, ans)

    def test5(self):
        qs = [('a', 'elem0'), 'elem1', ('a', 'elem2')]
        ans = [('.a', 'elem0'), ('', 'elem1'), ('.a', 'elem2')]
        
    def test6(self):
        qs = ('a', ('b', 'elem00'))
        ans = [('.a.b', 'elem00')]

    def test7(self):
        qs = ('a0', [('b0', 'elem00'), ('b1,', 'elem01')])
        ans = [('.a0.b0', 'elem00'), ('.a0.b1', 'elem01')]

    def test8(self):
        qs = [('a0', ('b0', 'elem00')), ('a1', ('b0,', 'elem10'))]
        ans = [('.a0.b0', 'elem00'), ('.a1.b0', 'elem10')]

if __name__ == '__main__':
    unittest.main()
