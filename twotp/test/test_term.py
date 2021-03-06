# Copyright (c) 2007-2009 Thomas Herve <therve@free.fr>.
# See LICENSE for details.

"""
Test basic term functionalities.
"""

from twotp.term import Atom, AtomNotInCache, Reference
from twotp.test.util import TestCase



class TermTestCase(TestCase):
    """
    Test erlang to python term classes.
    """

    def tearDown(self):
        """
        Reset properties of term classes.
        """
        # Reset atom cache
        Atom._cache = {}


    def test_atomEquality(self):
        """
        Test equality of L{Atom}s.
        """
        self.assertEqual(Atom("foo"), Atom("foo"))
        self.assertNotIdentical(Atom("foo"), Atom("foo"))


    def test_cachedAtom(self):
        """
        Test L{Atom} cache functionality.
        """
        a = Atom("bar", 1)
        b = Atom(None, 1)
        self.assertEqual(a, b)


    def test_cachedAtomError(self):
        """
        Trying to retrieve an L{Atom} not in the cache should raise an error.
        """
        self.assertRaises(AtomNotInCache, Atom, None, 1)


    def test_referenceHash(self):
        """
        L{Reference} instances are hashable.
        """
        r = Reference(Atom("foo@bar"), [1, 0, 0], 0)
        self.assertIsInstance(hash(r), int)
