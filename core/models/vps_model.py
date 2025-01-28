from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid, Enum, text, String
from core.models import Base

import enum


class StatusChoices(enum.Enum):
    started = "started"
    blocked = "blocked"
    stopped = "stopped"


class Vps(Base):

    uid: Mapped[str] = mapped_column(Uuid)

    cpu: Mapped[int] = mapped_column(default=0, server_default=text("0"))

    ram: Mapped[int] = mapped_column(default=0, server_default=text("0"))

    hdd: Mapped[int] = mapped_column(default=0, server_default=text("0"))

    status: Mapped[str] = mapped_column(
        String(7),
        Enum(StatusChoices),
        default=StatusChoices.started.value,
        server_default=StatusChoices.started.value,
    )
