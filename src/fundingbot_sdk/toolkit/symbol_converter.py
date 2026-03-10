from __future__ import annotations

from abc import abstractmethod
from typing import Protocol


class SymbolConverter(Protocol):  # noqa: D101
    @abstractmethod
    def from_standard_to_native(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи."""

    @abstractmethod
    def quote_from_stable_coin_to_fiat_if_needed(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи."""

    @abstractmethod
    def quote_from_fiat_to_stable_coin_if_needed(self, symbol: str) -> str:
        """Конвертирует из стандартного формата символа в нативный формат биржи."""


class DefaultSymbolConverter(SymbolConverter):  # noqa: D101
    def from_standard_to_native(self, symbol: str) -> str:  # noqa: PLR6301, D102
        return symbol

    def quote_from_stable_coin_to_fiat_if_needed(self, symbol: str) -> str:  # noqa: PLR6301, D102
        return symbol

    def quote_from_fiat_to_stable_coin_if_needed(self, symbol: str) -> str:  # noqa: PLR6301, D102
        return symbol
