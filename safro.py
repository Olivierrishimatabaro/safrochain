"""
Safrochain Project
==================

A minimal and professional Python module describing the Safrochain blockchain
ecosystem. This file can serve as a foundation for documentation, demos,
education, or future integrations.

Author: Olivier Rishi Matabaro
License: MIT
"""

from typing import List, Dict


class Safrochain:
    """
    Core representation of the Safrochain blockchain.
    """

    def __init__(
        self,
        name: str,
        sdk: str,
        consensus: str,
        interoperability: str,
        smart_contracts: str
    ) -> None:
        self.name = name
        self.sdk = sdk
        self.consensus = consensus
        self.interoperability = interoperability
        self.smart_contracts = smart_contracts

    def features(self) -> List[str]:
        """
        Returns the main features of Safrochain.
        """
        return [
            "Fast and low-cost transactions",
            "Interoperability across multiple blockchains",
            "Energy-efficient consensus mechanism",
            "Support for decentralized applications",
            "Community-driven governance"
        ]

    def metadata(self) -> Dict[str, str]:
        """
        Returns technical metadata of the blockchain.
        """
        return {
            "Name": self.name,
            "SDK": self.sdk,
            "Consensus": self.consensus,
            "Interoperability": self.interoperability,
            "Smart Contracts": self.smart_contracts,
        }
