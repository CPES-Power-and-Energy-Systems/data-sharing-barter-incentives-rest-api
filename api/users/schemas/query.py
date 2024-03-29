from drf_yasg import openapi


################################
#  Query params templates
################################
def user_resources_query_params():
    return [
        openapi.Parameter("resource", openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER,
                          required=False,
                          description="Filter by resource identifier"),
        openapi.Parameter("resource_name", openapi.IN_QUERY,
                          type=openapi.TYPE_STRING,
                          required=False,
                          description="Filter by resource name"),
        openapi.Parameter("to_forecast", openapi.IN_QUERY,
                          type=openapi.TYPE_BOOLEAN,
                          required=False,
                          description="Return resources currently "
                                      "registered as 'to_forecast' "
                                      "in the market"),
    ]
