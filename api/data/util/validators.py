import re
import uuid
import datetime as dt

from rest_framework import exceptions
from market.models import MarketSession


def __validate_datetime_str(dt_str):
    fmt_ = "%Y-%m-%dT%H:%M:%SZ"
    try:
        dt.datetime.strptime(dt_str, fmt_)
    except (TypeError, ValueError):
        raise exceptions.ValidationError(
            f"Query datetime parameters must use format {fmt_}"
        )


def validate_query_params(
        market_session_id=None,
        resource_id=None,
        resource_name=None,
        market_session_status=None,
        confirmed=None,
        start_date=None,
        end_date=None,
):
    if market_session_id is not None:
        try:
            int(market_session_id)
        except ValueError:
            raise exceptions.ValidationError(
                "Query param 'market_session' must be an integer."
            )
    if resource_id is not None:
        try:
            uuid.UUID(resource_id)
        except ValueError:
            raise exceptions.ValidationError(
                "Query param 'resource' must be a valid uuid."
            )
    if market_session_status is not None:
        lbl = [x.lower() for x in MarketSession.MarketStatus.labels]
        if market_session_status.lower() not in lbl:
            raise exceptions.ValidationError(
                f"Query param 'session_status' must be "
                f"one of the following {lbl}"
            )
    if confirmed is not None:
        if confirmed.lower() not in ['true', 'false']:
            raise exceptions.ValidationError(
                "Query param 'confirmed' must be a boolean (true/false)"
            )

    if start_date is not None:
        __validate_datetime_str(start_date)

    if end_date is not None:
        __validate_datetime_str(end_date)

    if resource_name is not None:
        matched = re.match("^[a-z0-9_-]*$", resource_name)
        is_match = bool(matched)
        if not is_match:
            raise exceptions.ValidationError(
                {
                    "resource_name": "Resource name cannot contain any "
                                     "upper-case characters, "
                                     "spaces or any special "
                                     "characters besides '-' or '_'."
                }
            )
