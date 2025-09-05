from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(question, context):
    if not question.strip() or not context.strip():
        return "Please ask a question with product info."

    try:
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't find an answer."
