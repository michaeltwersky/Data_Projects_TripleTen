def get_age_group(age):

    """
    Returns the age group based on age in years within the interval 0..150
    otherwise returns 'unknown'.
    """

    if 0 <= age <= 14:
        return 'children'
        # complete this function so that it passes the unit test
         return 'unknown'

def test_get_age_group():

    """unit test for get_age_group"""

    assert get_age_group(-1) == 'unknown'
    assert get_age_group(0) == 'children'
    assert get_age_group(14) == 'children'
    assert get_age_group(15) == 'youth'
    assert get_age_group(24) == 'youth'
    assert get_age_group(25) == 'adults'
    assert get_age_group(64) == 'adults'
    assert get_age_group(65) == 'seniors'
    assert get_age_group(80) == 'seniors'
    assert get_age_group(150) == 'unknown' 