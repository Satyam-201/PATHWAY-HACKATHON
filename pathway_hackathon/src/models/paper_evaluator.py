import pathway as pw
from pathway.xpacks.llm import LLM
from pathway.stdlib.ml.index import PWPathwayIndex
from typing import Dict, List

class PaperEvaluator:
    def __init__(self, api_key: str):
        self.llm = LLM(api_key=api_key)
        self.vector_store = PWPathwayIndex()
        self.reference_embeddings = {}
        
    def evaluate_publishability(self, content: str) -> Dict:
        prompt = """
        Evaluate this research paper for publishability considering:
        1. Methodology and technical soundness
        2. Clarity and coherence
        3. Evidence quality
        4. Innovation
        
        Paper content: {content}
        
        Return JSON format:
{
            "is_publishable": boolean,
            "scores": {
                "methodology": int,
                "clarity": int,
                "evidence": int,
                "innovation": int
            },
            "reasoning": string
        }
        """
        
        response = self.llm.generate(prompt.format(content=content[:3000]))
        return json.loads(response)
    
    def select_conference(self, content: str, similar_papers: List[Dict]) -> Dict:
        prompt = """
        Recommend the most suitable conference (CVPR, NeurIPS, DAA, EMNLP, TMLR, KDD) for this paper.
Paper: {content}
        
        Similar papers:
        {similar_papers}
        
        Return JSON format:
        {
            "conference": string,
            "rationale": string,
            "confidence": float
        }
        """
        
        similar_papers_text = "\n".join([
            f"Conference: {p['conference']}\nExcerpt: {p['content'][:500]}..."
            for p in similar_papers[:3]
        ])
        
        response = self.llm.generate(prompt.format(
            content=content[:2000],
            similar_papers=similar_papers_text
        ))
        return json.loads(response)
