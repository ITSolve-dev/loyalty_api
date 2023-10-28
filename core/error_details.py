from typing import Dict, Optional

from pydantic import BaseModel


class ErrorDetails(BaseModel):
    """
    Default Error model for API
    Type is key for string
    type: "general.errors.doesnt_exists"
    """
    type: str
    description: Optional[str] = None
    ctx: Optional[Dict] = None
