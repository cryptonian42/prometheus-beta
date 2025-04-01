import pytest
import logging
import io
import logging

from src.variable_type_logger import log_variable_type

def test_log_variable_type_primitive_types():
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test integer
    result = log_variable_type(42)
    assert result == 'int'
    log_output = log_capture.getvalue()
    assert 'Variable type: int, Value: 42' in log_output

    # Reset log capture
    log_capture.truncate(0)
    log_capture.seek(0)

    # Test string
    result = log_variable_type("Hello")
    assert result == 'str'
    log_output = log_capture.getvalue()
    assert 'Variable type: str, Value: \'Hello\'' in log_output

    # Reset log capture
    log_capture.truncate(0)
    log_capture.seek(0)

    # Test float
    result = log_variable_type(3.14)
    assert result == 'float'
    log_output = log_capture.getvalue()
    assert 'Variable type: float, Value: 3.14' in log_output

def test_log_variable_type_complex_types():
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test list
    result = log_variable_type([1, 2, 3])
    assert result == 'list'
    log_output = log_capture.getvalue()
    assert 'Variable type: list, Value: [1, 2, 3]' in log_output

    # Reset log capture
    log_capture.truncate(0)
    log_capture.seek(0)

    # Test dictionary
    result = log_variable_type({'a': 1, 'b': 2})
    assert result == 'dict'
    log_output = log_capture.getvalue()
    assert 'Variable type: dict, Value: {\'a\': 1, \'b\': 2}' in log_output

def test_log_variable_type_none():
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test None
    result = log_variable_type(None)
    assert result == 'NoneType'
    log_output = log_capture.getvalue()
    assert 'Variable type: NoneType' in log_output