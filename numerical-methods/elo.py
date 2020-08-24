def player_a(ra, rb):
    """Returns the probability of player A
    winning using the Elo rating system.
    """
    DIFF_WEIGHT = 400
    return 1 / (1 + 10**((rb - ra) / DIFF_WEIGHT))

def player_b(ra, rb):
    """Returns the complement of PLAYER_A."""
    return 1 - player_a(ra, rb)

def update_ranking(ranking, actual, expected):
    """Returns the updated ranking of a player."""
    K_FACTOR = 32
    return ranking + K_FACTOR * (actual - expected)
