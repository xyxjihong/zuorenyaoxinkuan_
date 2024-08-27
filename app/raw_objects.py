import datetime as dt
from pydantic import BaseModel, conlist, constr
from typing import Optional, List


class Swaption(BaseModel):
    trade_date: dt.date
    expiry_date: dt.date
    start_date: dt.date
    end_date: dt.date
    currency: str
    strike: float
    notional: float

    @property
    def tail(self):
        return (self.end_date - self.start_date).days / 365

    @property
    def expiry(self):
        return (self.expiry_date - self.trade_date).days / 365


class StrategyRule(BaseModel):
    components: conlist(Swaption, min_items=2)  # A list of material names (at least 2)
    notional_ratio: Optional[float] = None
    strike_eql: Optional[bool] = None
    expiry_eql: Optional[bool] = None
    tail_eql: Optional[bool] = None
    ccy_eql: Optional[bool] = None


class Strategy(BaseModel):
    name: str
    rules: List[StrategyRule]  # Each recipe can have multiple rules




strategies = [
    StrategyRule(name='Straddle',
                 rules=[StrategyRule]
                 )
]



if __name__ == "__main__":
    d = {'trade_date': dt.date.today(),
         'expiry_date': dt.date(2024, 9, 27),
         'start_date': dt.date(2024, 9, 29),
         'end_date': dt.date(2025, 9, 29),
         'currency': 'EUR',
         'strike': 0.021,
         'notional': 100.00}
    print(Swaption(**d).expiry)
