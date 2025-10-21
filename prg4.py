import pandas as pd;
from sklearn import datasets;
from sklearn.model_selection import train_test_split as tts;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.metrics import confusion_matrix,classification_report;

iris=datasets.load_iris();
x=iris.data;
y=iris.target;
print("\nsepal-length","sepal-width","petal-length","petal-width\n",x);
print("\nsentosa","versicolor","virginica\n",y);

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2);
print("\nx-train\n",x_train);
print("\nx-test\n",x_test);
print("\nx-train\n",x_train);
print("\nx-test\n",x_test);

knn=KNeighborsClassifier(7).fit(x_train,y_train);
df = pd.DataFrame({"Actual": y_test.flatten(),"Predicted": knn.predict(x_test).flatten()})
print(df);

accuracy=knn.score(x_test,y_test);
print("\nAccuracy",accuracy);

print("\nconfusion_matrix\n",confusion_matrix(y_test,knn.predict(x_test)));
print("\nAccuracy Metrics\n",classification_report(y_test,knn.predict(x_test)));