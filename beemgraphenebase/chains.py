from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
default_prefix = "PEV"
known_chains = {
    "PEV": {
        "chain_id": "0" * int(256 / 4),
        "min_version": "0.0.1",
        "prefix": "PEV",
        "chain_assets": [
            {"asset": "PBD", "symbol": "PBD", "precision": 3, "id": 0},
            {"asset": "PEV", "symbol": "PEV", "precision": 3, "id": 1},
            {"asset": "VESTS", "symbol": "VESTS", "precision": 6, "id": 2}
        ],
    },
    "PEVTEST": {
        "chain_id": "18dcf0a285365fc58b71f18b3d3fec954aa0c141c44e4e5cb4cf777b9eab274e",
        "min_version": '0.0.1',
        "prefix": "TST",
        "chain_assets": [
            {"asset": "PBD", "symbol": "TBD", "precision": 3, "id": 0},
            {"asset": "PEV", "symbol": "TESTS", "precision": 3, "id": 1},
            {"asset": "VESTS", "symbol": "VESTS", "precision": 6, "id": 2}
        ],
    },
    "PEVAPPBASE": {
        "chain_id": "0" * int(256 / 4),
        "min_version": '0.1.0',
        "prefix": "PEV",
        "chain_assets": [
            {"asset": "@@000000013", "symbol": "SBD", "precision": 3, "id": 0},
            {"asset": "@@000000021", "symbol": "PEV", "precision": 3, "id": 1},
            {"asset": "@@000000037", "symbol": "VESTS", "precision": 6, "id": 2}
        ],
    },
}
