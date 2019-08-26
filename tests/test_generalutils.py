#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `generalutils` package."""

import os
import sys
import random
import unittest
import generalutils.guard as guard
from generalutils.constants import HttpStatusCode

class TestGeneralUtils(unittest.TestCase):
    
    def test_DirectoryExistsException(self):
        '''Test whether a certain directory exists'''

        self.assertTrue(guard.Filesystem.PathExist(os.getcwd()))

    def test_DirectoryDoesNotExistsException(self):
        '''Negative test to check whether a certain directory doesn't exists'''
        
        # Random not existing folder path
        path = f'D:/{random.randint(100,10000)}'

        # Expected exception
        exception = f"Path - '{path}' does not exist"

        # Check whether the correct assertion is raised
        with self.assertRaises(Exception) as context:
            guard.Filesystem.PathExist(path)

        self.assertTrue(exception in str(context.exception))

    def test_DirectoryExists(self):
        '''Test whether a certain directory exists'''

        self.assertTrue(guard.Filesystem.IsPath(os.getcwd()))

    def test_DirectoryDoesNotExists(self):
        '''Negative test to check whether a certain directory doesn't exists'''
        
        # Random not existing folder path
        path = f'D:/{random.randint(100,10000)}'

        self.assertFalse(guard.Filesystem.IsPath(path))
    
    def test_ObjectIsNotNoneOrEmpty(self):
        '''Test whether object is not none or empty'''

        word = "Not empty"

        self.assertTrue(guard.Collections.NotNoneOrEmpty(word))

    def test_ObjectIsEmpty(self):
        '''Negative test to check whether a object is empty'''

        # Empty string
        word = ''

        exception = f"Object - '{word}' is none or empty"

        with self.assertRaises(Exception) as context:
            guard.Collections.NotNoneOrEmpty(word)

        self.assertTrue(exception in str(context.exception))

    def test_ObjectIsNone(self):
        '''Negative test to check whether a object is none'''

        # None assigned object
        word = None

        exception = f"Object - '{word}' is none or empty"

        with self.assertRaises(Exception) as context:
            guard.Collections.NotNoneOrEmpty(word)

        self.assertTrue(exception in str(context.exception))
    
    def test_StatusCodesEqual(self):
        '''Test whether the status codes are returning correctly'''
        
        self.assertEqual(HttpStatusCode.Ok, 200)
        self.assertEqual(HttpStatusCode.Created, 201)
        self.assertEqual(HttpStatusCode.NoContent, 204)
        self.assertEqual(HttpStatusCode.BadRequest, 400)
        self.assertEqual(HttpStatusCode.Unauthorized, 401)
        self.assertEqual(HttpStatusCode.Forbidden, 403)
        self.assertEqual(HttpStatusCode.NotFound, 404)
        self.assertEqual(HttpStatusCode.MethodNotAllowed, 405)
        self.assertEqual(HttpStatusCode.TooManyRequests, 429)
        self.assertEqual(HttpStatusCode.InternalServerError, 500)
        self.assertEqual(HttpStatusCode.BadGateway, 502)
        self.assertEqual(HttpStatusCode.ServiceUnavailable, 503)
        self.assertEqual(HttpStatusCode.GatewayTimeout, 504)

    def test_StatusCodesNotEqual(self):
        '''Negative test to check whether status codes are not equal'''
        
        statusCode = 9999

        self.assertNotEqual(HttpStatusCode.Ok, statusCode)
        self.assertNotEqual(HttpStatusCode.Created, statusCode)
        self.assertNotEqual(HttpStatusCode.NoContent, statusCode)
        self.assertNotEqual(HttpStatusCode.BadRequest, statusCode)
        self.assertNotEqual(HttpStatusCode.Unauthorized, statusCode)
        self.assertNotEqual(HttpStatusCode.Forbidden, statusCode)
        self.assertNotEqual(HttpStatusCode.NotFound, statusCode)
        self.assertNotEqual(HttpStatusCode.MethodNotAllowed, statusCode)
        self.assertNotEqual(HttpStatusCode.TooManyRequests, statusCode)
        self.assertNotEqual(HttpStatusCode.InternalServerError, statusCode)
        self.assertNotEqual(HttpStatusCode.BadGateway, statusCode)
        self.assertNotEqual(HttpStatusCode.ServiceUnavailable, statusCode)
        self.assertNotEqual(HttpStatusCode.GatewayTimeout, statusCode)

    def test_ValidArgument(self):
        '''Test whether an argument is valid'''

        arg = ["this", "is", "a", "test"]

        self.assertTrue(guard.Argument.IsValid(arg))
    
    def test_InvalidArgument(self):
        '''Negative test to check whether an argument is invalid'''

        arg = None

        self.assertFalse(guard.Argument.IsValid(arg))

    def test_ValidCwdPathCwdNotEqualBase(self):
        '''Test whether the current working directory is within the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:\\This\\Is\\1\\2"))
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:\\This\\Is\\1"))
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:\\This\\Is"))
        else:
            base = "Z:/This/Is"
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:/This/Is/1/2"))
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:/This/Is/1"))
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:/This/Is"))

    def test_ValidCwdPathCwdEqualBase(self):
        '''Test whether the current working directory is equal to the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:\\This\\Is", True))
        else:
            base = "Z:/This/Is"
            self.assertTrue(guard.Filesystem.PathCwdExists(base, "Z:/This/Is", True))

    def test_InValidCwdPathCwdNotEqual(self):
        '''Negative test to check whether the current working directory is not within the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            cwd = "Z:\\This\\IsInvalid\\1\\2"
            exception = f"Current working directory: '{cwd}' is not within in the '{base}' path"
            
            with self.assertRaises(Exception) as context:
                guard.Filesystem.PathCwdExists(base, cwd)

            self.assertTrue(exception in str(context.exception))
            
        else:
            base = "Z:/This/Is"
            cwd = "Z:/This/IsInvalid/1/2"
            exception = f"Current working directory: '{cwd}' is not within in the '{base}' path"

            with self.assertRaises(Exception) as context:
                guard.Filesystem.PathCwdExists(base, cwd)

            self.assertTrue(exception in str(context.exception))

    def test_IsValidCwdPathCwdNotEqualBase(self):
        '''Test whether the current working directory is within the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:\\This\\Is\\1\\2"))
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:\\This\\Is\\1"))
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:\\This\\Is"))
        else:
            base = "Z:/This/Is"
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:/This/Is/1/2"))
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:/This/Is/1"))
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:/This/Is"))

    def test_IsValidCwdPathCwdEqualBase(self):
        '''Test whether the current working directory is equal to the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:\\This\\Is", True))
        else:
            base = "Z:/This/Is"

            self.assertTrue(guard.Filesystem.IsPathCwd(base, "Z:/This/Is", True))

    def test_IsInvalidValidCwdPathNotEqual(self):
        '''Negative test to check whether the current working directory is not within the base path'''

        if sys.platform == "win32":
            base = "Z:\\This\\Is"
            self.assertFalse(guard.Filesystem.IsPathCwd(base, "Z:\\This\\IsInvalid\\1\\2"))
        else:
            base = "Z:/This/Is"
            self.assertFalse(guard.Filesystem.IsPathCwd(base, "Z:/This/IsInvalid/1/2"))

if __name__ == '__main__':
	unittest.main()
