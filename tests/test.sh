#!/bin/bash
set -e

coverage run manage.py test
coverage report -m
