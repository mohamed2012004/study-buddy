import torch
from transformers import AutoModelForSequenceClassification

halluc_model_standalone = AutoModelForSequenceClassification.from_pretrained(
    "vectara/hallucination_evaluation_model",
    trust_remote_code=True
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
halluc_model_standalone.to(device)
MODELS_LOADED = True

@torch.no_grad()
def check_hallucination(question: str, answer: str, model):
    """
    يقارن بين answer (الناتج أو الإجابة) و question (السؤال) 
    ويرجع إذا فيه هلوسة أو لا مع النسب
    """
    if model is None:
        return False, 0.0, 0.0, 0.0

    # الزوج (claim, evidence)
    pairs = [(answer, question)]

    # استدعاء الموديل
    outputs = model.predict(pairs)  # بيرجع احتمال هلوسة
    hallucination_prob = outputs[0].item()

    # العكس = مش هلوسة
    not_hallucination_prob = 1.0 - hallucination_prob

    # قرار
    is_hallucination = hallucination_prob > not_hallucination_prob

    # درجة الثقة
    confidence_score = hallucination_prob if is_hallucination else not_hallucination_prob

    return is_hallucination, confidence_score, hallucination_prob, not_hallucination_prob
