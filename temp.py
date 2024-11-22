def celsius_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9
def test_should_celsius_to_fahreneheit():
    assert celsius_to_fahrenheit(100) == 212
def test_should_return_fahreneheit_to_celsius():
    assert fahrenheit_to_celsius(212) == 100