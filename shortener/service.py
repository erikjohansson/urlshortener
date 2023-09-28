import secrets


def shortcode():
    """
    Generates a shortcode using the secrets module.

    This function generates a random shortcode using the `token_urlsafe` function from the `secrets` module. It takes no parameters and returns a string of length 5.

    Returns:
        str: A randomly generated shortcode of length 5.
    """
    return secrets.token_urlsafe(nbytes=5)
