from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def reward_score(original, rewritten):
    emb1 = model.encode(original, convert_to_tensor=True)
    emb2 = model.encode(rewritten, convert_to_tensor=True)
    similarity = util.cos_sim(emb1, emb2).item()
    return round(similarity, 4)
