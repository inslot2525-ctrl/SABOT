def classify_intent(query):

    query = query.lower()

    if any(
        word in query
        for word in [
            "price",
            "pricing",
            "cost",
            "subscription",
            "plan"
        ]
    ):
        return "pricing"

    if any(
        word in query
        for word in [
            "competitor",
            "compare",
            "alternative",
            "vs"
        ]
    ):
        return "competitor"

    if any(
        word in query
        for word in [
            "problem",
            "issue",
            "concern",
            "risk"
        ]
    ):
        return "objection"

    if any(
        word in query
        for word in [
            "demo",
            "buy",
            "purchase",
            "interested",
            "contact sales"
        ]
    ):
        return "closing"

    return "feature"