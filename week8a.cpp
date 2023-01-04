 #include<iostream>
 using namespace std;

 template <class T> T addArray(T a[], T n){
 	int sum=0;
 	for(int i=0;i<n;i++){
    	sum+=a[i];
	}
	return sum;
 }
 int main(){
    int a[10],n;
    cout<<"enter n: ";
    cin>>n;
    cout<<"enter elements of the array: ";
    for(int i=0;i<n;i++){
    	cin>>a[i];
	}
    int result=addArray<int>(a, n);
    cout<<"sum of elements in 1D ARRAY: "<<result<<endl;
 }
