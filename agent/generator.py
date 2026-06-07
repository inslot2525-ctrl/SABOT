import re


def clean_text(text):

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = text.replace(
        "",
        ""
    )

    text = text.replace(
        "•",
        ""
    )

    text = text.strip()

    return text


def extract_key_points(
    context,
    max_points=6
):

    context = clean_text(
        context
    )

    sentences = re.split(
        r"(?<=[.!?])\s+",
        context
    )

    points = []

    seen = set()

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        if len(sentence) > 250:
            continue

        key = sentence.lower()

        if key in seen:
            continue

        seen.add(key)

        points.append(sentence)

        if len(points) >= max_points:
            break

    return points


def generate_answer(
    query,
    context,
    intent="feature"
):

    if not context.strip():

        return (
            "I could not find relevant information "
            "in the uploaded documents."
        )

    points = extract_key_points(
        context
    )

    if len(points) == 0:

        return (
            "I could not find relevant information "
            "in the uploaded documents."
        )

    answer = "## Summary\n\n"

    for point in points:

        answer += f"• {point}\n\n"

    answer += "\n---\n"

    answer += (
        "Source: Retrieved from uploaded documents."
    )

    return answer