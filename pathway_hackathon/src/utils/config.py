import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Base paths
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / "data"
    
    # API configurations
    PATHWAY_API_KEY = os.getenv("PATHWAY_API_KEY")
    
    # Model configurations
    EMBEDDING_MODEL = "text-embedding-ada-002"
    COMPLETION_MODEL = "gpt-4"
 # Application settings
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.PATHWAY_API_KEY:
            raise ValueError("PATHWAY_API_KEY environment variable is required")
        
        if not cls.DATA_DIR.exists():
            raise ValueError(f"Data directory does not exist: {cls.DATA_DIR}")
