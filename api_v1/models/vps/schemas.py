from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, Field
from pydantic_core.core_schema import UuidSchema

from core.models.vps_model import StatusChoices


class VpsBaseSchemas(BaseModel):
    uuid: Annotated[str, UuidSchema] | None = None
    cpu: Annotated[int, Field(ge=0)] | None = None
    ram: Annotated[int, Field(ge=0)] | None = None
    hdd: Annotated[int, Field(ge=0)] | None = None
    status: Annotated[str, Optional["StatusChoices"]] | None = None


class VpsCreateSchemas(VpsBaseSchemas):
    cpu: Annotated[int, Field(ge=0)]
    ram: Annotated[int, Field(ge=0)]
    hdd: Annotated[int, Field(ge=0)]
    status: Annotated[str, Optional["StatusChoices"]]


class VpsUpdateSchemas(VpsBaseSchemas):
    status: Annotated[str, Optional["StatusChoices"]]


class VpsSchemas(VpsBaseSchemas):
    model_config = ConfigDict(from_attributes=True)

    id: int