#!/bin/bash
echo Deploy tests to staging
python -m pytest -v -s test_trn_db.py