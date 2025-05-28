"""
ServerConfigSchema

Contains a Schema class for managing config data for server configurations.
"""

# import standard libraries
import logging
from pathlib import Path
from typing import Any, Dict, List

# import 3rd-party libraries

# import OGD libraries
from ogd.common.schemas.configs.data_sources.MySQLSourceSchema import MySQLSchema
from ogd.common.utils.SemanticVersion import SemanticVersion
from ogd.apis.schemas.ServerConfigSchema import ServerConfigSchema

# import local files

class DataAPIConfigSchema(ServerConfigSchema):
    def __init__(self, name:str, all_elements:Dict[str, Any], logger:logging.Logger):
        self._state_dbs        : Dict[str, MySQLSchema]
        self._ogd_core         : Path
        self._google_client_id : str
        self._dbg_level        : int
        self._version          : int

        if "GOOGLE_CLIENT_ID" in all_elements.keys():
            self._google_client_id = DataAPIConfigSchema._parseGoogleID(google_id=all_elements["GOOGLE_CLIENT_ID"], logger=logger)
        else:
            self._google_client_id = "UNKNOWN ID"
            logger.warning(f"{name} config does not have a 'GOOGLE_CLIENT_ID' element; defaulting to google_client_id={self._google_client_id}", logging.WARN)

        _used = {"DB_CONFIG", "OGD_CORE_PATH", "GOOGLE_CLIENT_ID"}
        _leftovers = { key : val for key,val in all_elements.items() if key not in _used }
        super().__init__(name=name, debug_level=logging.INFO, version=SemanticVersion(0,0,0,"version-not-set"), other_elements=_leftovers)

    @property
    def GoogleClientID(self) -> str:
        return self._google_client_id

    @property
    def AsMarkdown(self) -> str:
        ret_val : str

        ret_val = f"{self.Name}"
        return ret_val

    @staticmethod
    def _parseGoogleID(google_id, logger:logging.Logger) -> str:
        ret_val : str
        if isinstance(google_id, str):
            ret_val = google_id
        else:
            ret_val = str(google_id)
            logger.warning(f"Google Client ID type was unexpected type {type(google_id)}, defaulting to google_client_id=str({ret_val}).", logging.WARN)
        return ret_val
