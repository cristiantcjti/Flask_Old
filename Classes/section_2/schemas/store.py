from ma import ma 
from models.store import StoreModel

class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreModel
        load_instance = True
        dump_only = ('id', )
        include_fk = True