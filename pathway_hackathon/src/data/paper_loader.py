import pypdf
from typing import Dict, List
import os
import json

class PaperLoader:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def read_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        with open(file_path, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text.strip()

    def load_reference_papers(self) -> List[Dict]:
        """Load and process reference papers"""
        reference_dir = os.path.join(self.data_dir, 'reference')
        reference_data = []

        with open(os.path.join(reference_dir, 'reference_metadata.json'), 'r') as f:
            metadata = json.load(f)
            for paper_id, info in metadata.items():
                paper_path = os.path.join(reference_dir, f"{paper_id}.pdf")
                if os.path.exists(paper_path):
                    content = self.read_pdf(paper_path)
                    reference_data.append({
                        'paper_id': paper_id,
                        'content': content,
                        'metadata': info
                    })

        return reference_data

    def load_test_papers(self) -> List[Dict]:
        """Load papers to be evaluated"""
        test_dir = os.path.join(self.data_dir, 'test')
        test_papers = []

        for filename in os.listdir(test_dir):
            if filename.endswith('.pdf'):
                paper_id = filename.split('.')[0]
                content = self.read_pdf(os.path.join(test_dir, filename))
                test_papers.append({
                    'paper_id': paper_id,
                    'content': content
                })

        return test_papers
