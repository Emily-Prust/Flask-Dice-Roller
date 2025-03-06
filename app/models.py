from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.roll import roll


class Roll(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    note: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                            unique=True)
    amount: so.Mapped[int] = so.mapped_column()
    dice_number: so.Mapped[int] = so.mapped_column()
    roll_result: so.Mapped[str] = so.mapped_column(sa.String(999))

    def generate_roll(self, amount, dice_number):
        self.roll_result = roll(amount, dice_number)

    def __repr__(self):
        return f'<{self.note} : {self.amount} d{self.dice_number}(s) rolled. Result: {self.roll_result}.'
