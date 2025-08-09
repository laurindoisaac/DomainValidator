# test_domainvalidator.py
"""
Tests for DomainValidator module.
"""

import unittest
from domainvalidator import DomainValidator

class TestDomainValidator(unittest.TestCase):
    """Test cases for DomainValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DomainValidator()
        self.assertIsInstance(instance, DomainValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DomainValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
