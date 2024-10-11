from pydantic import BaseModel, model_validator, constr, EmailStr
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional, ClassVar, Dict, Any, Tuple


class User(BaseModel):

    hashed_user_rut: str
    rut: str
    name: str
    lastname: str
    email: Optional[EmailStr] = None

    @model_validator(mode="before")
    @classmethod
    def data_mapping(cls, data: Dict[str, Any]) -> dict:
        """
        Mapea los campos de data antes
        de crear el objeto como objeto de la clase.
        """

        hashed_user_rut = generate_password_hash(str(data.get("rut")), method='pbkdf2:sha256')

        data = dict(
            hashed_user_rut=hashed_user_rut,
            rut=data.get("rut"),
            name=data.get("name"),
            lastname=data.get("lastname"),
            email=data.get("email"),
        )
        return data
