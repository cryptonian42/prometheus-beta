import pytest
import json
import logging
from io import StringIO
from src.json_logger import log_json

class TestJSONLogger:
    @pytest.fixture
    def capture_log(self):
        """Fixture to capture log output"""
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)
        root_logger.setLevel(logging.DEBUG)
        yield log_capture
        root_logger.removeHandler(handler)

    def test_log_dict(self, capture_log):
        """Test logging a dictionary"""
        test_dict = {"name": "John", "age": 30}
        log_json(test_dict)
        log_output = capture_log.getvalue()
        assert json.dumps(test_dict, indent=2) in log_output

    def test_log_json_string(self, capture_log):
        """Test logging a JSON string"""
        test_json = '{"name": "Jane", "city": "New York"}'
        log_json(test_json)
        log_output = capture_log.getvalue()
        assert '"name": "Jane"' in log_output
        assert '"city": "New York"' in log_output

    def test_log_levels(self, capture_log):
        """Test different log levels"""
        test_dict = {"key": "value"}
        
        for level in ['debug', 'info', 'warning', 'error', 'critical']:
            capture_log.truncate(0)
            capture_log.seek(0)
            log_json(test_dict, log_level=level)
            log_output = capture_log.getvalue()
            assert json.dumps(test_dict, indent=2) in log_output

    def test_invalid_json_type(self):
        """Test logging an invalid type raises TypeError"""
        with pytest.raises(TypeError):
            log_json(123)
        
        with pytest.raises(TypeError):
            log_json([1, 2, 3])

    def test_invalid_json_string(self):
        """Test invalid JSON string raises TypeError"""
        with pytest.raises(TypeError):
            log_json('Invalid JSON')

    def test_invalid_log_level(self):
        """Test invalid log level raises ValueError"""
        with pytest.raises(ValueError):
            log_json({"key": "value"}, log_level="invalid_level")

    def test_custom_logger(self):
        """Test using a custom logger"""
        custom_logger = logging.getLogger('custom')
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        custom_logger.addHandler(handler)
        custom_logger.setLevel(logging.INFO)

        test_dict = {"test": "data"}
        log_json(test_dict, logger=custom_logger)
        log_output = log_capture.getvalue()
        assert json.dumps(test_dict, indent=2) in log_output