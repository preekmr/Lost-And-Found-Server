import sqlalchemy
from base import Base


class Items(Base):
    __tablename__ = 'items_primary'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=300))
    shape = sqlalchemy.Column(sqlalchemy.String(length=50))
    color = sqlalchemy.Column(sqlalchemy.String(length=50))
    owner = sqlalchemy.Column(sqlalchemy.String(length=300))
    date_found = sqlalchemy.Column(sqlalchemy.String(length=50))
    location_found = sqlalchemy.Column(sqlalchemy.String(length=300))
    is_collected = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    file_name = sqlalchemy.Column(sqlalchemy.String(length=300))
    date_collected = sqlalchemy.Column(sqlalchemy.String(length=50))
    collected_by = sqlalchemy.Column(sqlalchemy.String(length=300))

    def __repr__(self):
        return "%s" % self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "shape": self.shape,
            "color": self.color,
            "owner": self.owner,
            "date_found": self.date_found,
            "location_found": self.location_found,
            "is_collected": self.is_collected,
            "file_name": self.file_name,
            "date_collected": self.date_collected,
            "collected_by": self.collected_by
        }