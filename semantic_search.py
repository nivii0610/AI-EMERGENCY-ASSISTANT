from sentence_transformers import SentenceTransformer


# Load the AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


def find_similar_emergency(user_input):

    emergency_types = [

        "FLOOD",

        "FIRE",

        "EARTHQUAKE",

        "HEATWAVE",

        "CYCLONE / STORM",

        "ROAD ACCIDENT",

        "MEDICAL"
    ]


    descriptions = [

        "flood water rising flooding water entering house",

        "fire smoke flames burning building",

        "earthquake ground shaking tremor building shaking",

        "heatwave extreme heat very hot temperature heat illness",

        "cyclone storm strong winds heavy rain",

        "road accident vehicle crash car crash motorcycle accident collision",

        "medical emergency person unconscious not breathing severe bleeding sick"
    ]


    # Convert user's speech into an AI embedding
    user_embedding = model.encode(user_input)


    # Convert emergency descriptions into embeddings
    emergency_embeddings = model.encode(
        descriptions
    )


    # Calculate similarity
    similarities = model.similarity(
        user_embedding,
        emergency_embeddings
    )[0]


    # Find the closest emergency
    best_index = similarities.argmax()


    return (
        emergency_types[best_index],
        float(similarities[best_index])
    )

