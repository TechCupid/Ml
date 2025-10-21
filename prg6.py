from pandas import DataFrame;
from sklearn.cluster import KMeans;
import matplotlib.pyplot as plt;

data={'x':[1,56,76,87,93],'y':[2,5,7,23,36]}


df=DataFrame(data,columns=['x','y']);
plt.title("Before Clustering");
plt.scatter(df['x'],df['y']);
plt.show();

a=int(input("How Many Clusters Do You need to implement?:"));
b=KMeans(a).fit(df);
centroids=b.cluster_centers_;
print(centroids);

plt.title("After Clustering");
plt.scatter(df['x'],df['y'],c=b.labels_);
plt.scatter(centroids[:,0],centroids[:,-1],c='red');
plt.show();
