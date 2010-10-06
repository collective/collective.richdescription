import unittest
import doctest

OPTIONFLAGS = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        doctest.DocTestSuite('collective.richdescription.richdescription',
                             optionflags=OPTIONFLAGS,),
    ])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')