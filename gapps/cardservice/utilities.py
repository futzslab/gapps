
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


def update_actions(_dict):
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
        if key in ['onClick']:
            _dict[key] = {'action': value}
        if key in ['openLink', 'openDynamicLinkAction']:
            d_temp = _dict.get('onClick', {})
            d_temp.update({key: value})
            _dict['onClick'] = d_temp
            del _dict[key]
        elif key == 'selection_item':
            del _dict[key]
            _dict["items"] = [{'text': text, 'value': val, 'selected': sel}
                              for text, val, sel in value]
        elif isinstance(value, dict):
            update_actions(value)
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    update_actions(v_i)

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


def hex2floats(h):
    """Take a hex rgb string and returns an RGB tuple.

    Parameters
    ----------
    h: str
        hex rgb string (e.g. #ffffff)

    Returns
    -------
    rgb: tuple(float, float, float)

    """
    if not h:
        return None
    return tuple(int(h[i:i + 2], 16) / 255. for i in (1, 3, 5))  # skip '#'


def floats2hex(rgb):
    """Takes an RGB tuple or list and returns a hex RGB string."""
    if not rgb:
        return None
    return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'


def get_form_value(form, key):
    """Return Form value."""
    if not isinstance(form, dict):
        return None
    if not isinstance(key, str):
        return None

    val = form.get(key, {}).get('stringInputs', {}).get('value', None)
    return val
