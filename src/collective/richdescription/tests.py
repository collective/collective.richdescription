# -*- coding: utf-8 -*-
import doctest
import unittest

OPTIONFLAGS = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        doctest.DocTestSuite('collective.richdescription',
                             optionflags=OPTIONFLAGS,),
    ])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
