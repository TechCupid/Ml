from sklearn import datasets;
from sklearn.model_selection import train_test_split as tts;
from sklearn.naive_bayes import GaussianNB;
from sklearn.metrics import accuracy_score,confusion_matrix;

iris=datasets.load_iris();
x=iris.data;
y=iris.target;
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2);
print("\nx-test\n",x_test);
print("\nx-train\n",x_train);
print("\ny-test\n",y_test);
print("\ny-train\n",y_train);

model=GaussianNB();
model.fit(x_train,y_train);
prediction=model.predict(x_test);
print("\nprediction\n",prediction);

print("\naccuracy\n",accuracy_score(y_test,prediction));
print("\nconfusion matrix\n",confusion_matrix(y_test,prediction));

