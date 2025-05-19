from pipelex.core.stuff_content import StructuredContent

from typing import Optional, Literal
from enum import StrEnum


class OperationTypeEnum(StrEnum):
    CapitalIncrease = "capital increase"
    ShareIssue = "share issue"
    ShareBuyback = "share buyback"
    ShareSplit = "share split"
    ShareMerger = "share merger"
    ShareTransfer = "share transfer"
    ShareRepurchase = "share repurchase"


class OperationType(StructuredContent):
    """Type of financial operation"""

    category: Optional[
        Literal[
            OperationTypeEnum.CapitalIncrease,
            OperationTypeEnum.ShareIssue,
            OperationTypeEnum.ShareBuyback,
            OperationTypeEnum.ShareSplit,
            OperationTypeEnum.ShareMerger,
            OperationTypeEnum.ShareTransfer,
            OperationTypeEnum.ShareRepurchase,
        ]
    ] = None
    explanation: Optional[str] = None


class CapitalIncreaseCaracteristics(StructuredContent):
    total_gross_amount: Optional[float] = None
    total_new_shares: Optional[int] = None
    subscription_ratio: Optional[float] = None
    subscription_period: Optional[str] = None
    dilution: Optional[float] = None
    discount: Optional[float] = None
