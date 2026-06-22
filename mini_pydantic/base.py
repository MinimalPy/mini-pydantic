from .fields import Field
from .validators import validate

class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        annotations = namespace.get("__annotations__", {})

        fields = {}

        for field_name, annotation in annotations.items():
            fields[field_name] = Field(
                field_name,
                annotation,
            )

        namespace["__fields__"] = fields

        return super().__new__(
            mcls,
            name,
            bases,
            namespace,
        )

class BaseModel(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self.__fields__.items():
            if field_name not in kwargs:
                raise ValueError(
                    f"Missing field: {field_name}"
                )

            value = validate(
                kwargs[field_name],
                field.annotation,
            )

            setattr(
                self,
                field_name,
                value,
            )

    def model_dump(self):
        return {
            name: getattr(self, name)
            for name in self.__fields__
        }

    def __repr__(self):
        values = ", ".join(
            f"{name}={getattr(self, name)!r}"
            for name in self.__fields__
        )

        return f"{self.__class__.__name__}({values})"