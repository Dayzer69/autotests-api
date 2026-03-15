import pydantic
from pydantic import BaseModel, Field, HttpUrl, FilePath
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class GetFilesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение файла.
    """
    file: FileSchema



