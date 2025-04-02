import json
import logging

def log_json(json_obj, log_level='info', logger=None):
    """
    Log a JSON object with proper formatting and indentation.

    Args:
        json_obj (dict or str): The JSON object to log. 
                                Can be a dictionary or a JSON-formatted string.
        log_level (str, optional): Logging level. 
                                   Defaults to 'info'. 
                                   Supports 'debug', 'info', 'warning', 'error', 'critical'.
        logger (logging.Logger, optional): Custom logger. 
                                           If None, uses the root logger.

    Returns:
        str: Formatted JSON string that was logged.

    Raises:
        TypeError: If json_obj is not a dict or valid JSON string.
        ValueError: If an invalid log level is provided.
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Validate and convert input to dictionary if it's a string
    if isinstance(json_obj, str):
        try:
            json_obj = json.loads(json_obj)
        except json.JSONDecodeError:
            raise TypeError("Input must be a valid JSON string or dictionary")
    
    # Validate input is a dictionary
    if not isinstance(json_obj, dict):
        raise TypeError("Input must be a dictionary or JSON-formatted string")

    # Validate log level
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level. Supported levels are: {', '.join(log_levels.keys())}")

    # Format JSON with indentation
    formatted_json = json.dumps(json_obj, indent=2)

    # Log the formatted JSON
    log_levels[log_level.lower()](formatted_json)

    return formatted_json