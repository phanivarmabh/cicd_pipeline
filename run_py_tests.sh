#!/bin/bash
echo Deploy tests to staging env
python -m pytest -v -s test_trn_db.py