import pytest
from pathlib import Path

from alterpdf import pdf_to_image

# test, uh test cases

def is_prime(num):
    if num == 1:
        return False

def test_is_prime():
    assert is_prime(1) == False


# test cases to actually test pdfs

# test whether the pdf_to_image module actually works
def test_pdf_to_image():
    assert '/'

def test_ocr_image_exists():
    pass

def image_made_to_pdf():
    pass
