import pandas as pd;
from sklearn.feature_extraction.text import (CountVectorizer,TfidfVectorizer,TfidfTransformer);

data={"apple bag virus","bag cat party","apple party"};

cv=CountVectorizer();
bow=cv.fit_transform(data);
print("\n Back of Words\n")
print(bow.toarray());
print("\nBack of Words Features\n")
print(cv.get_feature_names_out());
print(cv.vocabulary_);

tv=TfidfVectorizer();
bow=tv.fit_transform(data);
print("\nTfidf Vectors\n")
print(bow.toarray());
print("\nTfidf Vector Features\n")
print(tv.get_feature_names_out());
print(tv.vocabulary_);