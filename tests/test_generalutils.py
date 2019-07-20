#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `generalutils` package."""

import os
import random
import unittest
import generalutils.guard as guard

class TestGeneralUtils(unittest.TestCase):
    
    def test_DirectoryExists(self):
        '''Test whether a certain directory exists'''

        self.assertTrue(guard.Filesystem.PathExist(os.getcwd()))

    def test_DirectoryDoesNotExists(self):
        '''Negative test to check whether a certain directory doesn't exists'''
        
        # Random not existing folder path
        path = f'D:/{random.randint(100,10000)}'

        # Expected exception
        exception = f"Path - '{path}' does not exist"

        # Check whether the correct assertion is raised
        with self.assertRaises(Exception) as context:
            guard.Filesystem.PathExist(path)

        self.assertTrue(exception in str(context.exception))
    
    def test_ObjectIsNotNoneOrEmpty(self):
        '''Test whether object is not none or empty'''

        word = "Not empty"

        self.assertTrue(guard.Collections.IsNotNoneOrEmpty(word))

    def test_ObjectIsEmpty(self):
        '''Negative test to check whether a object is empty'''

        # Empty string
        word = ''

        exception = f"object - '{word}' is none or empty"

        with self.assertRaises(Exception) as context:
            guard.Collections.IsNotNoneOrEmpty(word)

        self.assertTrue(exception in str(context.exception))

    def test_ObjectIsNone(self):
        '''Negative test to check whether a object is none'''

        # None assigned object
        word = None

        exception = f"object - '{word}' is none or empty"

        with self.assertRaises(Exception) as context:
            guard.Collections.IsNotNoneOrEmpty(word)

        self.assertTrue(exception in str(context.exception))
    
if __name__ == '__main__':
	unittest.main()
