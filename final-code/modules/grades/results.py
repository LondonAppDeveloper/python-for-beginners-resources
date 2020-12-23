"""
Functions for calculating results.
"""

A_THRESHOLD = 70
B_THRESHOLD = 60
C_THRESHOLD = 50
D_THRESHOLD = 40
E_THRESHOLD = 30


def get_grade(score):
    """Accepts a score and returns a letter version."""
    if score >= A_THRESHOLD:
        return 'A'
    elif score >= B_THRESHOLD:
        return 'B'
    elif score >= C_THRESHOLD:
        return 'C'
    elif score >= D_THRESHOLD:
        return 'D'
    elif score >= E_THRESHOLD:
        return 'E'

    return 'F'
