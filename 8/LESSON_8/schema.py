import graphene
import graphql_jwt

from graph_app import schema
from graph_app_two import mutations


class Query(schema.Query, graphene.ObjectType):
    pass


class Mutation(mutations.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()


scheme = graphene.Schema(query=Query, mutation=Mutation)
