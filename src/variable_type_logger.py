import logging

# Configure a logger that can be captured in tests
logger = logging.getLogger(__name__)

def log_variable_type(variable):
    """
    Log the type of a given variable with an informative message.

    Args:
        variable: Any Python object whose type needs to be logged.

    Returns:
        str: The string representation of the variable's type.

    Examples:
        >>> log_variable_type(42)
        >>> log_variable_type("Hello")
        >>> log_variable_type([1, 2, 3])
    """
    if variable is None:
        logger.info("Variable type: NoneType")
        return "NoneType"
    
    var_type = type(variable).__name__
    var_repr = repr(variable)
    
    logger.info(f"Variable type: {var_type}, Value: {var_repr}")
    return var_type