from pydantic import BaseModel


class SymbolIdDetails(BaseModel):
    isin: str
    short_isin: str
    short_name: str
    long_name: str
    english_name: str

    company_isin: str
    company_short_isin: str
    company_name: str

    market_code: str
    market_name: str

    group_code: str
    group_name: str

    subgroup_code: str
    subgroup_name: str
