def celsius_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def test_should_celsius_to_fahreneheit():
    assert celsius_to_fahrenheit(100) == 212