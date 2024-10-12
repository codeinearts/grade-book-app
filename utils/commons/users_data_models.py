from pydantic import (
    BaseModel,
    StringConstraints,
    model_validator, 
    EmailStr

)
from werkzeug.security import generate_password_hash
from typing import Optional, Dict, Any, Annotated


class User(BaseModel):

    hashed_user_rut: str
    rut: str
    name: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    lastname: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    email: Optional[EmailStr] = None

    @model_validator(mode="before")
    @classmethod
    def data_mapping(cls, data: Dict[str, Any]) -> dict:
        """
        Mapea los campos de data antes
        de crear el objeto como objeto de la clase.
        """
        rut = data.get("rut")
        if not cls.validate_rut(rut):
            raise ValueError("RUT inválido")

        hashed_user_rut = generate_password_hash(str(rut), method='pbkdf2:sha256')

        return dict(
            hashed_user_rut=hashed_user_rut,
            rut=rut,
            name=data.get("name"),
            lastname=data.get("lastname"),
            email=data.get("email"),
        )

    @staticmethod
    def validate_rut(rut: str) -> bool:
        """
        Aquí puedes agregar las reglas de validación del RUT según el formato esperado.
        """
        # Implementa la lógica de validación según el formato de tu país.
        if len(rut) < 8 or len(rut) > 12:  # Ejemplo de validación de longitud
            return False
        # Agregar validaciones adicionales si es necesario (e.g., dígito verificador)
        return True
