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

    docs = search(query)

    print("\nRETRIEVED DOCUMENTS")
    print("=" * 50)

    for doc in docs:

        print(
            f"\nSOURCE: {doc['source']}"
        )

        print(
            doc["text"][:300]
        )

    intent = classify_intent(
        query
    )

    context = "\n".join(
        [
            d["text"]
            for d in docs
        ]
    )

    print("\nCONTEXT SENT TO GEMINI")
    print("=" * 50)

    print(
        context[:1500]
    )

    answer = generate_answer(
        query,
        context
    )

    sources = list(
        set(
            [
                d["source"]
                for d in docs
            ]
        )
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

    print("\nINTENT")
    print(result["intent"])

    print("\nANSWER")
    print(result["answer"])

    print("\nSOURCES")
    print(result["sources"])

    print("\nLEAD CAPTURE")
    print(result["lead_capture"])