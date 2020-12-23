"""
Module for exam predictions.
"""

def get_avg(score_history):
    """Takes a list of previous grades and returns average."""
    return sum(score_history) / len(score_history)


def predict_score(score_history, min_score=0):
    """Takes a list of previous percentage grades and returns the average."""
    score_avg = get_avg(score_history)
    if score_avg < min_score:
        return min_score
    
    return score_avg