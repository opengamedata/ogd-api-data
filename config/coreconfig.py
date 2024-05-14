settings = {
    "BATCH_SIZE":1000,
    "LOG_FILE":False,
    "DEBUG_LEVEL":"DEBUG",
    "FAIL_FAST":False,
    "FILE_INDEXING" : 
    {
        "LOCAL_DIR"     : "./data/",
        "REMOTE_URL"    : "https://fieldday-web.ad.education.wisc.edu/opengamedata/",
        "TEMPLATES_URL" : "https://github.com/opengamedata/opengamedata-samples"
    },
    "GAME_SOURCES" :
    {
        "AQUALAB_BQ" : {
            "DB_TYPE"    : "FIREBASE",
            "PROJECT_ID" : "aqualab-57f88",
            "PROJECT_KEY": "./config/aqualab.json"
        },
        "MASHOPOLIS_BQ": {
            "DB_TYPE"    : "BIGQUERY",
            "PROJECT_ID" : "mashopolis-36754",
            "PROJECT_KEY": "./config/mashopolis.json"
        },
        "SHADOWSPECT_BQ": {
            "DB_TYPE"    : "FIREBASE",
            "PROJECT_ID" : "shadowspect-b8e63",
            "PROJECT_KEY": "./config/shadowspect.json"
        },
        "SHIPWRECKS_BQ": {
            "DB_TYPE"    : "FIREBASE",
            "PROJECT_ID" : "shipwrecks-8d142",
            "PROJECT_KEY": "./config/shipwrecks.json"
        },
        "OPENGAMEDATA_BQ" : {
            "DB_TYPE"    : "BIGQUERY",
            "PROJECT_ID" : "wcer-field-day-ogd-1798",
            "PROJECT_KEY": "./config/ogd.json"
        },
        "OPENGAMEDATA_MYSQL": {
            "DB_TYPE" : "MySQL",
            "DB_HOST" : "127.0.0.1",
            "DB_PORT" : 3306,
            "DB_USER" : "swansonl",
            "DB_PW"   : "Terrific16Tuesday",
            "SSH_HOST": "ogd-logger.fielddaylab.wisc.edu",
            "SSH_USER": "lwswanson2",
            "SSH_PASS": "GobbLer58@4D[3"
        },
        "OPENGAMEDATA_MYSQL_FEATURES": {
            "DB_TYPE" : "MySQL",
            "DB_HOST" : "127.0.0.1",
            "DB_PORT" : 3306,
            "DB_USER" : "username",
            "DB_PW"   : "password",
            "SSH_HOST": "hostname",
            "SSH_USER": "WCER AD User",
            "SSH_PASS": "WCER AD Password"
        },
        "LOGGER": {
            "DB_TYPE" : "MySQL",
            "DB_HOST" : "127.0.0.1",
            "DB_PORT" : 3306,
            "DB_USER" : "username",
            "DB_PW"   : "password",
            "SSH_HOST": "hostname",
            "SSH_USER": "WCER AD User",
            "SSH_PASS": "WCER AD Password"
        }
    },
    "GAME_SOURCE_MAP":
    {
        "AQUALAB":        { "source":"AQUALAB_BQ",    "database":"analytics_271167280",             "table":"events",        "schema":"FIREBASE" },
        "ALL_YOU_CAN_ET": { "source":"OPENGAMEDATA_BQ",    "database":"all_you_can_eat",     "table":"all_you_can_et_daily", "schema":"OPENGAMEDATA_BIGQUERY" },
        "BACTERIA":       { "source":"OPENGAMEDATA_BQ",    "database":"bacteria",            "table":"bacteria_daily",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "BALLOON":        { "source":"OPENGAMEDATA_BQ",    "database":"balloon",             "table":"balloon_daily",        "schema":"OPENGAMEDATA_BIGQUERY" },
        "CRYSTAL":        { "source":"OPENGAMEDATA_BQ",    "database":"crystal",             "table":"crystal_daily",        "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_CARBON":   { "source":"OPENGAMEDATA_BQ",    "database":"cycle_carbon",        "table":"cycle_carbon_daily",   "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_NITROGEN": { "source":"OPENGAMEDATA_BQ",    "database":"cycle_nitrogen",      "table":"cycle_nitrogen_daily", "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_WATER":    { "source":"OPENGAMEDATA_BQ",    "database":"cycle_water",         "table":"cycle_water_daily",    "schema":"OPENGAMEDATA_BIGQUERY" },
        "EARTHQUAKE":     { "source":"OPENGAMEDATA_BQ",    "database":"earthquake",          "table":"earthquake_daily",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "ICECUBE":        { "source":"OPENGAMEDATA_MYSQL", "database":"opengamedata",        "table":"ICECUBE",              "schema":"OPENGAMEDATA_MYSQL"    },
        "JOWILDER":       { "source":"OPENGAMEDATA_BQ",    "database":"jowilder",            "table":"jowilder_daily",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "JOURNALISM":     { "source":"OPENGAMEDATA_BQ",    "database":"journalism",          "table":"journalism_daily",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "PENGUINS":       { "source":"OPENGAMEDATA_BQ",    "database":"penguins",            "table":"penguins_daily",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "LAKELAND":       { "source":"OPENGAMEDATA_BQ",    "database":"lakeland",            "table":"lakeland_daily",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "MAGNET":         { "source":"OPENGAMEDATA_BQ",    "database":"magnet",              "table":"magnet_daily",         "schema":"OPENGAMEDATA_BIGQUERY" },
        "MASHOPOLIS":     { "source":"OPENGAMEDATA_BQ",    "database":"mashopolis",          "table":"mashopolis_daily",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "SHIPWRECKS":     { "source":"SHIPWRECKS_BQ",      "database":"analytics_269167605", "table":"events",               "schema":"FIREBASE"              },
        "SHADOWSPECT":    { "source":"SHADOWSPECT_BQ",     "database":"analytics_284091572", "table":"events",               "schema":"FIREBASE"              },
        "WAVES":          { "source":"OPENGAMEDATA_BQ",    "database":"waves",               "table":"waves_daily",          "schema":"OPENGAMEDATA_BIGQUERY" },
        "WIND":           { "source":"OPENGAMEDATA_BQ",    "database":"wind",                "table":"wind_daily",           "schema":"OPENGAMEDATA_BIGQUERY" },
    },
    "GAME_DESTINATION_MAP":
    {
        "AQUALAB":        { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"aqualab",        "schema":"OPENGAMEDATA_BIGQUERY" },
        "ALL_YOU_CAN_ET": { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"all_you_can_et", "schema":"OPENGAMEDATA_BIGQUERY" },
        "BACTERIA":       { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"bacteria",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "BALLOON":        { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"balloon",        "schema":"OPENGAMEDATA_BIGQUERY" },
        "CRYSTAL":        { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"crystal",        "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_CARBON":   { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"cycle_carbon",   "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_NITROGEN": { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"cycle_nitrogen", "schema":"OPENGAMEDATA_BIGQUERY" },
        "CYCLE_WATER":    { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"cycle_water",    "schema":"OPENGAMEDATA_BIGQUERY" },
        "EARTHQUAKE":     { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"earthquake",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "ICECUBE":        { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"ICECUBE",        "schema":"OPENGAMEDATA_MYSQL"    },
        "JOWILDER":       { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"jowilder",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "JOURNALISM":     { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"journalism",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "PENGUINS":       { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"penguins",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "LAKELAND":       { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"lakeland",       "schema":"OPENGAMEDATA_BIGQUERY" },
        "MAGNET":         { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"magnet",         "schema":"OPENGAMEDATA_BIGQUERY" },
        "MASHOPOLIS":     { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"mashopolis",     "schema":"OPENGAMEDATA_BIGQUERY" },
        "SHIPWRECKS":     { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"shipwrecks",     "schema":"FIREBASE"              },
        "SHADOWSPECT":    { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"shadowspect",    "schema":"FIREBASE"              },
        "WAVES":          { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"waves",          "schema":"OPENGAMEDATA_BIGQUERY" },
        "WIND":           { "destination":"OPENGAMEDATA_MYSQL_FEATURES", "database":"opengamedata", "table":"wind",           "schema":"OPENGAMEDATA_BIGQUERY" },
    },
}
