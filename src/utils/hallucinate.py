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
    Compares between the question and the answer (result) 
    and returns whether there is hallucination or not, along with the percentages.
    """
    if model is None:
        return False, 0.0, 0.0, 0.0

    
    pairs = [(answer, question)]

    outputs = model.predict(pairs)  
    hallucination_prob = outputs[0].item()

    not_hallucination_prob = 1.0 - hallucination_prob

    
    is_hallucination = hallucination_prob > not_hallucination_prob

    confidence_score = hallucination_prob if is_hallucination else not_hallucination_prob

    return is_hallucination, confidence_score, hallucination_prob, not_hallucination_prob
