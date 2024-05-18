from djongo import models as djongo_models
from shared.models.user import User as PydanticUser

class UserModel(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    username = djongo_models.CharField(max_length=255)
    email = djongo_models.EmailField(unique=True)

    class Meta:
        abstract = False

    def to_pydantic(self):
        return PydanticUser(
            _id=self._id,
            username=self.username,
            email=self.email
        )
