from fastapi import APIRouter

from api.schemas import QueryRequest

from retrieval.hybrid_search import search
from retrieval.reranker import rerank

from agent.generator import generate_answer
from agent.intent_router import classify_intent
from agent.lead_capture import detect_buying_intent

router = APIRouter()


@router.post("/chat")
def chat(req: QueryRequest):

    intent = classify_intent(req.query)

    docs = search(req.query)

    docs = rerank(docs)

    context = "\n".join(
        [d.payload["text"] for d in docs]
    )

    answer = generate_answer(
        req.query,
        context
    )

    return {
        "intent": intent,
        "answer": answer,
        "lead_capture": detect_buying_intent(
            req.query
        )
    }