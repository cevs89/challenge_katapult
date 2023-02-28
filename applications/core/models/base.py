import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base Models:
    Purpose:
        Se hace un modelo base para evitar escribir los mismos campos en todos los modelos,
        evitar repetir codigo en la mejor practica que podemos aplicar.
    Fields:
        uuid: podriamos usarlo como ID unico para operaciones donde no nos importe que vean el ID
        is_active: Todos los registro dentro de una DB deben manejar estados
        created_at: Fecha de creacion, solo se modifica su unica vez cuando se crea
        modified_at: Fecha de modificacion, se modificacion siempre que se actualice el modelo

    Comment:
        i thoung in some point made relations with User(),
        maybe if you want to find some records for a specific user.

        But it's doesn't a requirement in the file
    """

    uuid = models.UUIDField(
        default=uuid.uuid4,
        verbose_name="UUID",
        unique=True,
        editable=False,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    """ abstract allow extend the models and inmerse in others """

    class Meta:
        abstract = True
