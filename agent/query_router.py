def classify_query(query):

    query = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    casual = [
        "thanks",
        "thank you",
        "bye",
        "goodbye"
    ]

    if query in greetings:
        return "greeting"

    if query in casual:
        return "casual"

    return "knowledge"