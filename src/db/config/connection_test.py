import pytest
import os

from .connection import DBConnectionHandler

@pytest.mark.skipif(os.getenv('RUN_SENSITIVE_TEST') != 'true', reason="Sensitive test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()

    assert engine is not None