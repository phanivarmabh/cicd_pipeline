import pymssql
import pytest


@pytest.fixture(scope='module')
def adv_connection():
    conn = pymssql.connect(
        server='EPINHYDW03E2\\DQE',
        user='TestRobot',
        password='DataQuality@123',
        database='AdventureWorks2012'
    )
    yield conn
    conn.close()


@pytest.fixture()
def adv_cursor(adv_connection):
    cursor = adv_connection.cursor()
    yield cursor
    adv_connection.rollback()


@pytest.fixture(scope='module')
def trn_connection():
    conn = pymssql.connect(
        server='EPINHYDW03E2\\DQE',
        user='TestRobot',
        password='DataQuality@123',
        database='TRN'
    )
    yield conn
    conn.close()


@pytest.fixture()
def trn_cursor(trn_connection):
    cursor = trn_connection.cursor()
    yield cursor
    trn_connection.rollback()
