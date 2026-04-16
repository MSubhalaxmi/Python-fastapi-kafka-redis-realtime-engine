import graphene

class Vehicle(graphene.ObjectType):
    id = graphene.String()
    speed = graphene.Float()

class Query(graphene.ObjectType):
    vehicle = graphene.Field(Vehicle, id=graphene.String())

    def resolve_vehicle(root, info, id):
        return {"id": id, "speed": 72.5}

schema = graphene.Schema(query=Query)