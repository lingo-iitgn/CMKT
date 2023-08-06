from cmkt.metrics import *

sent = "RAHUL jab dieting par hota hai toh green tea peeta hai."
metrics = CodeMixedMetrics(language="hineng")

# Total Available metrics
print("Total available metrics")
print(metrics.AvailableMetrics())

# Metrics calculation with only sentence
print("Metrics calculation with only sentence:")
print()
print("CMI: ",metrics.metrics(name="cmi", sentence=sent))
print()
print("M-Index: ",metrics.metrics(name="M-index", sentence=sent)) #name 
print()
print("I-Index: ",metrics.metrics(name="I-index", sentence=sent))
print()
print("burstiness: ",metrics.metrics(name="burstiness", sentence=sent))
print()

# Metrics calculation through custom language tags
# custom langauage tags for the above sentence, '1'--> lang1(Hindi token in this case), '0'-->lang2(english token in this case), '2'-->language independent tokens


sent = "RAHUL jab dieting par hota hai toh green tea peeta hai."
custom_language_tags = ['2','1','0','1','1','1','1','0','0','1','1','2']


print(" Metrics calculation through custom language tags")
print()
print("CMI: ",metrics.metrics(name="cmi", sentence=sent, langTags=custom_language_tags))
print()
print("M-Index: ",metrics.metrics(name="M-index", sentence=sent, langTags=custom_language_tags))
print()
print("I-Index: ",metrics.metrics(name="I-index", sentence=sent, langTags=custom_language_tags))
print()
print("burstiness: ",metrics.metrics(name="burstiness",sentence=sent, langTags=custom_language_tags ))
print()

