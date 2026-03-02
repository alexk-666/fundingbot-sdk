from __future__ import annotations

from abc import abstractmethod
from typing import Protocol


class SymbolConverter(Protocol):
    @abstractmethod
    def from_standard_to_native(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи.
        """
        pass

    @abstractmethod
    def quote_from_stable_coin_to_fiat_if_needed(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи.
        """
        pass

    @abstractmethod
    def quote_from_fiat_to_stable_coin_if_needed(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи.
        """
        pass


class DefaultSymbolConverter(SymbolConverter):
    def from_standard_to_native(self, symbol: str) -> str:
        return symbol

    def quote_from_stable_coin_to_fiat_if_needed(self, symbol: str) -> str:
        return symbol

    def quote_from_fiat_to_stable_coin_if_needed(self, symbol: str) -> str:
        return symbol
