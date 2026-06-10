"""
Simple way to disable all other loggers than a given one.
"""
import logging

def disable_other_loggers(only_enabled_name: str) -> None:
    for v in logging.Logger.manager.loggerDict.values():
        if isinstance(v, logging.Logger) and v.name != only_enabled_name:
            v.disabled = True
