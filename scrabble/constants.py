from collections import Counter, namedtuple

"""
2 blank tiles (scoring 0 points)
1 point: E ×12, A ×9, I ×9, O ×8, N ×6, R ×6, T ×6, L ×4, S ×4, U ×4
2 points: D ×4, G ×3
3 points: B ×2, C ×2, M ×2, P ×2
4 points: F ×2, H ×2, V ×2, W ×2, Y ×2
5 points: K ×1
8 points: J ×1, X ×1
10 points: Q ×1, Z ×1
"""

Tile = namedtuple('TILE', 'char, freq, value')

TILES = (
    Tile(char='A', freq=9, value=1),
    Tile(char='B', freq=2, value=3),
    Tile(char='C', freq=2, value=3),
    Tile(char='D', freq=4, value=2),
    Tile(char='E', freq=12, value=1),
    Tile(char='F', freq=2, value=4),
    Tile(char='G', freq=3, value=2),
    Tile(char='H', freq=2, value=4),
    Tile(char='I', freq=9, value=1),
    Tile(char='J', freq=1, value=8),
    Tile(char='K', freq=1, value=5),
    Tile(char='L', freq=4, value=1),
    Tile(char='M', freq=2, value=3),
    Tile(char='N', freq=6, value=1),
    Tile(char='O', freq=8, value=1),
    Tile(char='P', freq=2, value=3),
    Tile(char='Q', freq=1, value=10),
    Tile(char='R', freq=6, value=1),
    Tile(char='S', freq=4, value=1),
    Tile(char='T', freq=6, value=1),
    Tile(char='U', freq=4, value=1),
    Tile(char='V', freq=2, value=4),
    Tile(char='W', freq=2, value=4),
    Tile(char='X', freq=1, value=8),
    Tile(char='Y', freq=2, value=4),
    Tile(char='Z', freq=1, value=10),
    Tile(char='*', freq=2, value=0),
)

LETTERS = tuple([t.char for t in TILES if t.char != '*'])
FREQ = Counter({t.char: t.freq for t in TILES})
SCORER = Counter({t.char: t.value for t in TILES})

# 27 tile types
assert len(set(TILES)) == 27
# 100 tiles in total
assert sum([t.freq for t in TILES]) == 100
# 187 points from tiles
assert sum([t.freq * t.value for t in TILES]) == 187
# 26 letters
assert len(set(LETTERS)) == 26




