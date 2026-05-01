"""Configuration management module"""
import os
import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path="config.yaml"):
        self.config_path = Path(config_path)
        self.data = {}
        if self.config_path.exists():
            with open(self.config_path) as f:
                self.data = yaml.safe_load(f)
    def get(self, key, default=None):
        keys = key.split(".")
        v = self.data
        for k in keys:
            if isinstance(v, dict):
                v = v.get(k)
            else:
                return default
        return v if v is not None else default
