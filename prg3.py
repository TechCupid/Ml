import pandas as pd;
from sklearn.linear_model import LinearRegression;
from sklearn.model_selection import train_test_split as tts;
from matplotlib import pyplot as plt;
data=pd.read_csv(input("Give the path of the file"));
print(data);
x=data["Hours"].values.reshape(-1,1);
y=data["Score"].values.reshape(-1,1);

x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2);
print(x_train);
print(x_test);
print(y_train);
print(y_test);

reg=LinearRegression();
reg.fit(x_train,y_train);
y_pred=reg.predict(x_test);
x_pred=reg.predict(x_train);
z_pred=pd.DataFrame({"Actual":y_test.squeeze(),"predicted":y_pred.squeeze()});
print(z_pred);

plt.title("Hours VS Scores");
plt.xlabel("Hours");
plt.ylabel("Score");
plt.scatter(x_train,y_train,color="violet");
plt.plot(x_train,x_pred,color="green");
plt.show();
t=int(input("how many hours do you have?:"));
print("predicted score for",t,"  hours",(reg.coef_*t)+reg.intercept_);
