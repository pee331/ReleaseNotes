# test_releasenotes.py
"""
Tests for ReleaseNotes module.
"""

import unittest
from releasenotes import ReleaseNotes

class TestReleaseNotes(unittest.TestCase):
    """Test cases for ReleaseNotes class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReleaseNotes()
        self.assertIsInstance(instance, ReleaseNotes)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReleaseNotes()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
