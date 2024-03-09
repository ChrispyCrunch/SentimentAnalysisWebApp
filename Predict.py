from transformers import pipeline

class Predict:
    def __init__(self):
        self.classifier = pipeline(
            model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
            return_all_scores=True
        )

    def make_prediction(self, input):
        if not input:
            return None, None
    
        try:
            results = self.classifier(input)
            if results:
                top_result = max(results[0], key=lambda x: x['score'])
                return top_result['label'], top_result['score']
        except Exception as e:
            return None, e
    
        return None, None
    
    
        
