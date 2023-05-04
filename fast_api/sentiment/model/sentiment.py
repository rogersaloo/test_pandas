from transformers import pipeline
nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", tokenizer="distilbert-base-uncased-finetuned-sst-2-english")
test = nlp("Zapier is sooooo confusing to me")

def main():
    print(test)

if __name__ == '__main__':
    main()