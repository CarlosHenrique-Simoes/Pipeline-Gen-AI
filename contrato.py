from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChatGPT"
    produto3 = "ZapFlow com Llama 3.0"


class Vendas(BaseModel):
    """Modelo de dados para as vendas.

    Args:
        email (EmailStr): Email do comprador.
        data (datetime): Data da compra.
        valor (PositiveFloat): Valor da compra.
        quantidade (Positiveint): Quantidade de produtos.
        produto (ProdutoEnum): Categoria do produto.

    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

