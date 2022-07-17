"""Some general utilities"""
from uuid import uuid4
from requests import post
from django.shortcuts import reverse


HTTPBIN='https://httpbin.org/get'


def create_return_to(request_id):
    """Create a return url to do tests and analyze information

    This function prevents you from create a website for testing.
    It allows you to develop quickly.

    Reference: httpbin.org
    """
    url = reverse('')
    r = post(url=url, data={"uuid": request_id})
    url = r.json()['url']
    return url


# def create_return_to(request_id):
#     """Create a return url to do tests and analyze information
#
#     This function prevents you from create a website for testing.
#     It allows you to develop quickly.
#
#     Reference: httpbin.org
#     """
#     r = get(HTTPBIN, {"uuid": uuid4().hex})
#     url = r.json()['url']
#     return url


def nonce_saver(payload):
    return True


def nonce_reader(nonce):
    return False
