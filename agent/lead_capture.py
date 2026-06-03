BUYING_SIGNALS = [
    "interested",
    "book demo",
    "schedule demo",
    "contact sales",
    "purchase",
    "buy",
    "sign up",
    "trial",
    "pricing",
    "get started"
]


def detect_buying_intent(query):

    query = query.lower()

    for signal in BUYING_SIGNALS:

        if signal in query:
            return True

    return False