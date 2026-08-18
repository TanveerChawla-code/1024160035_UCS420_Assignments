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

category_counts = df.groupby("category").size()
print(category_counts)