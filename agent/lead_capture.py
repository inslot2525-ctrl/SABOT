BUYING_SIGNALS = [
    "demo",
    "pricing",
    "purchase",
    "buy",
    "trial",
    "contact sales",
    "interested",
    "sign up"
]


def detect_buying_intent(
    query
):

    query = query.lower()

    return any(
        signal in query
        for signal in BUYING_SIGNALS
    )