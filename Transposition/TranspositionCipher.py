from itertools import chain, cycle
from typing import Iterable


class TranspositionCipher:

    def encrypt(self, plain_text: str, rails: int) -> str:
        rail_indices = self._rail_indices(rails)
        return "".join(c for c, _ in sorted(zip(plain_text, rail_indices), key=lambda x: x[1]))

    def decrypt(self, cipher: str, rails: int) -> str:
        rail_indices = self._rail_indices(rails)
        rail_indices = sorted((e, i) for i, e in zip(range(len(cipher)), rail_indices))
        result = [None] * len(cipher)
        for c, (_, i) in zip(cipher, rail_indices):
            result[i] = c
        return "".join(result)

    def _rail_indices(self, rails: int) -> Iterable[int]:
        return cycle(chain(range(rails), range(rails - 2, 0, - 1)))
