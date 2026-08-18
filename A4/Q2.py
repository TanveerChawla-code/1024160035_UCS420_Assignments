import pandas as pd
roll_number = "1024160035"
last_two_digits = [int(d) for d in roll_number[-2:]]
fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

categories = ["billing","account","general"]

personalized_entries = []
digit = last_two_digits[0]
category = categories[digit % 3]

personalized_entries.append({
    "question": "how can i check my payment status",
    "answer": "You can check your payment status from the Billing section.",
    "keywords": "payment status billing transaction",
    "category": category
})

digit = last_two_digits[1]
category = categories[digit % 3]

personalized_entries.append({
    "question": "how can i update my registered email",
    "answer": "You can update your registered email from your account settings.",
    "keywords": "email update account settings",
    "category": category
})

all_entries = fixed_entries + personalized_entries
df = pd.DataFrame(all_entries)


def score_query(query, df):
    query_words = query.lower().split()
    results = []
    for index, row in df.iterrows():
        keywords = row['keywords'].lower().split()
        text = row['question'].lower() + " " + row['keywords'].lower()
        text_words = set(text.split())
        matched_words = text_words.intersection(query_words)
        if len(query_words) > 0:
            confidence = len(matched_words) / len(query_words)
        else:
            confidence = 0


        if confidence > 0:
            results.append({
                "question": row['question'],
                "answer": row['answer'],
                "category": row['category'],
                "matched_keywords": ", ".join(matched_words),
                "confidence": round(confidence,2)
            })

        results = sorted(results, key=lambda x: x['confidence'], reverse=True)
    return pd.DataFrame(results)

query = "how can i pay the fee"
results_df = score_query(query, df)
print("\nQuery Results:")
print(results_df)