import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    TRACKER_USERNAME:str=os.getenv('TRACKER_USERNAME')
    TRACKER_PASSWORD:str=os.getenv('TRACKER_PASSWORD')
