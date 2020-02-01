from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return "%s" % self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fullname": self.fullname,
            "nickname": self.nickname
        }