import unittest
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite


optionflags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.ELLIPSIS

def test_suite():
    from zope.testing.doctestunit import DocTestSuite
    return unittest.TestSuite((
	    FunctionalDocFileSuite("store.txt",
		    package="plone.openid.tests"),
            ))

