
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token


def delete_none(_dict):
    """Delete None values recursively from all of the dictionaries

    Parameters
    ----------
    _dict : dict
        dictionnaries containing None values

    Returns
    -------
    _dict : dict
        dictionnaries without any None values

    """
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    delete_none(v_i)

    return _dict


def decode_user(token: str):
    """Decode Google User ID Token.

    Parameters
    ----------
    token : str
        An end user ID token. The user’s email address is encoded in
        the end user ID token, formatted as a JSON web token

    Returns
    -------
    dict
        user id info

    """
    request = requests.Request()
    id_info = verify_oauth2_token(token, request)
    # TODO: Handle the valueerror below
    # ValueError: Token expired, 1659048959 < 1659050005
    return id_info


def decode_email(token: str):
    """Decode Google User ID Token.

    Parameters
    ----------
    token : str
        An end user ID token. The user’s email address is encoded in
        the end user ID token, formatted as a JSON web token

    Returns
    -------
    dict
        user id info

    """
    user = decode_user(token)
    return user.get("email", "")
