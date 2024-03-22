#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import pytest
# from osb import URLClass  # Import your URLClass from your module
#
# @pytest.fixture
# def valid_data():
#     return {
#         'ID': 1,
#         'TOPIC_NAME': 'Topic 1',
#         'YEAR': '2022',
#         'LEVEL': 'Level I',
#         'INTRODUCTION_SUMMARY': 'Introduction summary',
#         'LEARNING_OUTCOMES': 'Learning outcomes',
#         'SUMMARY_PAGE_LINK': 'https://example.com/summary',
#         'PDF_FILE_LINK': 'https://example.com/pdf'
#     }
#
# @pytest.fixture
# def invalid_data():
#     return {
#         'ID': -1,
#         'TOPIC_NAME': '',
#         'YEAR': 'InvalidYear',
#         'LEVEL': 'Unknown',
#         'INTRODUCTION_SUMMARY': '',
#         'LEARNING_OUTCOMES': 'Learning outcomes',
#         'SUMMARY_PAGE_LINK': 'http://example.com/summary',
#         'PDF_FILE_LINK': 'ftp://example.com/pdf'
#     }
#
# def test_valid_data(valid_data):
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for valid data")
#
# def test_invalid_data(invalid_data):
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
# def test_null_year(valid_data):
#     valid_data['YEAR'] = None
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for null year")
#
# def test_null_level(valid_data):
#     valid_data['LEVEL'] = None
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for null level")
#
# def test_invalid_url(valid_data):
#     valid_data['SUMMARY_PAGE_LINK'] = 'invalidurl'
#     with pytest.raises(ValueError):
#         URLClass(**valid_data)


# In[3]:


# pwd


# In[ ]:


###Osborne New Code from here

# import pytest
# from osb import URLClass  # Import your URLClass from your module
#
# @pytest.fixture
# def valid_data():
#     return {
#         'ID': 1,
#         'TOPIC_NAME': 'Topic 1',
#         'YEAR': '2022',
#         'LEVEL': 'Level I',
#         'INTRODUCTION_SUMMARY': 'Introduction summary',
#         'LEARNING_OUTCOMES': 'Learning outcomes',
#         'SUMMARY_PAGE_LINK': 'https://example.com/summary',
#         'PDF_FILE_LINK': 'https://example.com/pdf'
#     }
#
# @pytest.fixture
# def invalid_data():
#     return {
#         'ID': -1,
#         'TOPIC_NAME': '',
#         'YEAR': 'InvalidYear',
#         'LEVEL': 'Unknown',
#         'INTRODUCTION_SUMMARY': '',
#         'LEARNING_OUTCOMES': 'Learning outcomes',
#         'SUMMARY_PAGE_LINK': 'http://example.com/summary',
#         'PDF_FILE_LINK': 'ftp://example.com/pdf'
#     }
#
#
# def test_valid_data(valid_data, invalid_data):
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for valid data")
#
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
# def test_invalid_data(valid_data, invalid_data):
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for valid data")
#
# def test_null_year(valid_data, invalid_data):
#     valid_data['YEAR'] = None
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for null year")
#
#     invalid_data['YEAR'] = None
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
# def test_null_level(valid_data, invalid_data):
#     valid_data['LEVEL'] = None
#     try:
#         URLClass(**valid_data)
#     except ValueError:
#         pytest.fail("Validation should pass for null level")
#
#     invalid_data['LEVEL'] = None
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
# def test_invalid_url(valid_data, invalid_data):
#     valid_data['SUMMARY_PAGE_LINK'] = 'invalidurl'
#     with pytest.raises(ValueError):
#         URLClass(**valid_data)
#
#     invalid_data['SUMMARY_PAGE_LINK'] = 'invalidurl'
#     with pytest.raises(ValueError):
#         URLClass(**invalid_data)
#
#


###########Ozzzzzzzzzzzzzzzzzz

import pytest
from Assignment3_Part1_1 import URLClass  # Import your URLClass from your module

@pytest.fixture
def valid_data():
    return {
        'ID': 1,
        'TOPIC_NAME': 'Topic 1',
        'YEAR': '2022',
        'LEVEL': 'Level I',
        'INTRODUCTION_SUMMARY': 'Introduction summary',
        'LEARNING_OUTCOMES': 'Learning outcomes',
        'SUMMARY_PAGE_LINK': 'https://example.com/summary',
        'PDF_FILE_LINK': 'https://example.com/pdf'
    }

@pytest.fixture
def invalid_data():
    return {
        'ID': -1,
        'TOPIC_NAME': '',
        'YEAR': 'InvalidYear',
        'LEVEL': 'Unknown',
        'INTRODUCTION_SUMMARY': '',
        'LEARNING_OUTCOMES': 'Learning outcomes',
        'SUMMARY_PAGE_LINK': 'http://example.com/summary',
        'PDF_FILE_LINK': 'ftp://example.com/pdf'
    }

# Existing test functions...

def test_invalid_level(valid_data, invalid_data):
    invalid_data['LEVEL'] = 'Unknown'  # Invalid level
    with pytest.raises(ValueError):
        URLClass(**invalid_data)

    valid_data['LEVEL'] = 'Level I'  # Valid level
    try:
        URLClass(**valid_data)
    except ValueError:
        pytest.fail("Validation should pass with a valid level")

def test_invalid_introduction_summary(valid_data, invalid_data):
    invalid_data['INTRODUCTION_SUMMARY'] = ''  # Invalid introduction summary
    with pytest.raises(ValueError):
        URLClass(**invalid_data)

    valid_data['INTRODUCTION_SUMMARY'] = 'Introduction summary'  # Valid introduction summary
    try:
        URLClass(**valid_data)
    except ValueError:
        pytest.fail("Validation should pass with a valid introduction summary")

def test_invalid_learning_outcomes(valid_data, invalid_data):
    invalid_data['LEARNING_OUTCOMES'] = ''  # Invalid learning outcomes
    with pytest.raises(ValueError):
        URLClass(**invalid_data)

    valid_data['LEARNING_OUTCOMES'] = 'Learning outcomes'  # Valid learning outcomes
    try:
        URLClass(**valid_data)
    except ValueError:
        pytest.fail("Validation should pass with valid learning outcomes")

def test_invalid_summary_page_link(valid_data, invalid_data):
    invalid_data['SUMMARY_PAGE_LINK'] = 'ftp://example.com/summary'  # Invalid URL
    with pytest.raises(ValueError):
        URLClass(**invalid_data)

    valid_data['SUMMARY_PAGE_LINK'] = 'https://example.com/summary'  # Valid URL
    try:
        URLClass(**valid_data)
    except ValueError:
        pytest.fail("Validation should pass with a valid summary page link")

def test_invalid_pdf_file_link(valid_data, invalid_data):
    invalid_data['PDF_FILE_LINK'] = 'invalidurl'  # Invalid URL
    with pytest.raises(ValueError):
        URLClass(**invalid_data)

    valid_data['PDF_FILE_LINK'] = 'https://example.com/pdf'  # Valid URL
    try:
        URLClass(**valid_data)
    except ValueError:
        pytest.fail("Validation should pass with a valid PDF file link")
