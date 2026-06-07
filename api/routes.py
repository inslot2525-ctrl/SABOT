from fastapi import APIRouter

from api.schemas import (
    QueryRequest,
    QueryResponse
)

from retrieval.hybrid_search import (
    search
)

from agent.generator import (
    generate_answer
)

from agent.intent_router import (
    classify_intent
)

from agent.lead_capture import (
    detect_buying_intent
)

from agent.confidence import (
    calculate_confidence
)

router = APIRouter()


def classify_query(query: str):

    query = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    casual = [
        "thanks",
        "thank you",
        "ok",
        "okay",
        "bye",
        "goodbye"
    ]

    if query in greetings:
        return "greeting"

    if query in casual:
        return "casual"

    return "knowledge"


@router.post(
    "/chat",
    response_model=QueryResponse
)
def chat(
    request: QueryRequest
):

    query_type = classify_query(
        request.query
    )

    if query_type == "greeting":

        return QueryResponse(
            intent="conversation",
            answer="""
Hello! 👋

I can answer questions from the documents you upload.

Examples:

• What are the seller policies?

• What account restrictions exist?

• What are the review guidelines?

Upload documents and ask questions.
""",
            confidence=100,
            lead_capture=False,
            sources=[]
        )

    if query_type == "casual":

        return QueryResponse(
            intent="conversation",
            answer="You're welcome.",
            confidence=100,
            lead_capture=False,
            sources=[]
        )

    docs = search(
        request.query,
        top_k=5
    )

    if not docs:

        return QueryResponse(
            intent="information",
            answer="""
I could not find relevant information
in the uploaded documents.
""",
            confidence=0,
            lead_capture=False,
            sources=[]
        )

    # Relevance check

    if "distance" in docs[0]:

        best_distance = docs[0]["distance"]

        if best_distance > 1.2:

            return QueryResponse(
                intent="information",
                answer="""
I could not find relevant information
in the uploaded documents.

Please upload documents that contain
information related to your question.
""",
                confidence=0,
                lead_capture=False,
                sources=[]
            )

    intent = classify_intent(
        request.query
    )

    context = "\n\n".join(
        [
            doc["text"]
            for doc in docs
        ]
    )

    answer = generate_answer(
        request.query,
        context,
        intent
    )

    confidence = calculate_confidence(
        len(docs),
        5
    )

    sources = []

    seen = set()

    for doc in docs:

        source_name = doc.get(
            "source",
            "Unknown File"
        )

        if source_name not in seen:

            seen.add(
                source_name
            )

            sources.append(
                {
                    "file": source_name,
                    "snippet":
                    doc["text"][:250]
                }
            )

    lead_capture = detect_buying_intent(
        request.query
    )

    return QueryResponse(
        intent=intent,
        answer=answer,
        confidence=confidence,
        lead_capture=lead_capture,
        sources=sources
    )