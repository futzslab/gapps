from gapps.cardservice import utilities as ut


def test_delete_none():
    my_dict = {'key': {'hey': None,
                       'ho': None}
               }

    assert ut.delete_none(my_dict) == {'key': {}}
    my_dict = {'hey': None, 'ho': None}
    assert not ut.delete_none(my_dict)
    my_dict = {'key': {'hey': None,
                       'ho': {'hey': None,
                              'ho': None}
                       }
               }

    assert ut.delete_none(my_dict) == {'key': {'ho': {}}}


def test_color_conversion():
    assert ut.hex2floats('#000000') == (0.0, 0.0, 0.0)

    val = ut.hex2floats('#123456')
    hexa = ut.floats2hex(val)

    assert hexa == '#123456'

    assert ut.hex2floats(10) == None
    assert ut.hex2floats('10') == None
