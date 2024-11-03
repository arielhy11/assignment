WHITE_SPACE_OPTIONAL = r"\s?"  # Matches zero or one space
WHITE_SPACE_REQUIRED = r"\s"   # Matches exactly one space

TEMPERATURE_SUFFIX = rf"(?:{WHITE_SPACE_OPTIONAL}°{WHITE_SPACE_OPTIONAL}C|{WHITE_SPACE_OPTIONAL}C)"      # Matches: "°C", "° C", "C", " °C", " C"
VOLTAGE_SUFFIX = rf"{WHITE_SPACE_OPTIONAL}V"                    # Matches: "V", " V"

SIGNED_NUMBER = r'[+-]?\d+(?:\.\d+)?'                      # Matches "+105", "+ 105", "-40", "- 40", etc
UNSIGNED_NUMBER = r'\d+(?:\.\d+)?'                             # Matches: 42, 42.5

def getTemperaturePatterns() -> str:
    return f"({SIGNED_NUMBER}){WHITE_SPACE_OPTIONAL}{TEMPERATURE_SUFFIX}" \
           f"{WHITE_SPACE_REQUIRED}to{WHITE_SPACE_REQUIRED}{WHITE_SPACE_OPTIONAL}({SIGNED_NUMBER})" \
           f"{WHITE_SPACE_OPTIONAL}{TEMPERATURE_SUFFIX}"

def getVoltagePatterns() -> str:
    return f"({UNSIGNED_NUMBER}){WHITE_SPACE_OPTIONAL}{VOLTAGE_SUFFIX}{WHITE_SPACE_REQUIRED}to{WHITE_SPACE_REQUIRED}({UNSIGNED_NUMBER}){WHITE_SPACE_OPTIONAL}{VOLTAGE_SUFFIX}"
