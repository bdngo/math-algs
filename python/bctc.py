from random import randint


def bctc(rolls: int) -> float:
    """Calculates the win/loss ratio for the Vietnamese betting game 'Bầu Cua Tôm Cá.'"""
    wins = 0
    for _ in range(rolls):
        dice, bet = [randint(1, 6) for _ in range(3)], randint(1, 6)
        if dice.count(bet):
            wins += 1
    return wins / rolls * 100
