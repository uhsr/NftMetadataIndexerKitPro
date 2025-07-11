# test_nftmetadataindexerkitpro.py
"""
Tests for NftMetadataIndexerKitPro module.
"""

import unittest
from nftmetadataindexerkitpro import NftMetadataIndexerKitPro

class TestNftMetadataIndexerKitPro(unittest.TestCase):
    """Test cases for NftMetadataIndexerKitPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerKitPro()
        self.assertIsInstance(instance, NftMetadataIndexerKitPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerKitPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
