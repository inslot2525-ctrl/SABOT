from retrieval.hybrid_search import search

from agent.intent_router import (
    classify_intent
)

from agent.generator import (
    generate_answer
)

from agent.lead_capture import (
    detect_buying_intent
)


def ask(query):

    intent = classify_intent(query)

    docs = search(query)

    context = "\n".join(
        [d["text"] for d in docs]
    )

    sources = list(
        set(
            [
                d["source"]
                for d in docs
            ]
        )
    )

    answer = generate_answer(
        query,
        context
    )

    return {
        "intent": intent,
        "answer": answer,
        "sources": sources,
        "lead_capture":
            detect_buying_intent(
                query
            )
    }


while True:

    query = input(
        "\nAsk Question: "
    )

    if query.lower() == "exit":
        break

    result = ask(query)

    print("\nIntent:")
    print(result["intent"])

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    print(result["sources"])

    print("\nLead Capture:")
    print(result["lead_capture"])