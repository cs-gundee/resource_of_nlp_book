# Шаардлагатай санг импортлох
import nltk
nltk.download('punkt')                        # Үгсийг салгах tokenizer
nltk.download('averaged_perceptron_tagger')   # Үгийн аймаг тодорхойлогч (POS tagger)
nltk.download('maxent_ne_chunker')            # Нэрлэсэн нэгжийн chunker
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')                        # NE танихад хэрэглэгдэх үгийн жагсаалт

from nltk import ne_chunk, word_tokenize, pos_tag

# Жишээ өгөгдөл
txt = "John is studying at Stanford University in California"

# NER гүйцэтгэх
tokens = word_tokenize(txt)
pos_tags = pos_tag(tokens)
tree = ne_chunk(pos_tags, binary=False)

print(tree)
