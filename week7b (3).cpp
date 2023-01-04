#include<bits/stdc++.h>
#include<iostream>
#include<string.h>
#include <iomanip>
using namespace std;
class time1{
public:
    int min,sec;
    time1()
    {
        min=0;
        sec=0;
    }
    time1(int x,int y)
    {
        min=x;
        sec=y;
    }
    int returnMinutes()
    {
        return min;
    }
    int returnSeconds()
    {
        return sec;
    }
    
    int returnTotalSeconds()
    {
        int x=(min*60)+sec;
        return x;
    }
    void comparison(time1 x,time1 y)
    {
        if(x.min==y.min&&x.sec==y.sec)
        {
            cout<<"two times are equal\n";
        }
        else if(x.min>y.min)
        {
            cout<<"T1 is greater \n";
        }
        else
        {
            cout<<"T2 is greater \n";
        }
    }
    void subtraction(time1 x,time1 y)
    {
        int temp1=x.min-y.min;
        int temp2=x.sec-y.sec;
        if(temp1<0)
        {
            temp1=0;
            temp2=0;
        }
        if(temp2<0)
        {
            temp2=0;
        }
        cout<<temp1<<":"<<temp2<<endl;
    }
    void addition(time1 x,time1 y)
    {
        int temp1=x.min+y.min;
        int temp2=x.sec+y.sec;
        cout<<temp1<<":"<<temp2<<endl;
    }
};
int main()
{
    int t1m,t1s,t2m,t2s;
    cout<<"Enter time t1 in minutes and seconds:\n";
    cin>>t1m>>t1s;
    cout<<"Enter time t2 in minutes and seconds:\n";
    cin>>t2m>>t2s;
    time1 t1=time1(t1m,t1s);
    time1 t2=time1(t2m,t2s);
    time1 t;
    cout<<"Time t1 in minutes and seconds:"<<t1.returnMinutes()<<":"<<t1.returnSeconds()<<endl;
    cout<<"Time t1 in minutes:  "<<t1.returnMinutes()<<endl;
    cout<<"Time t1 in seconds:"<<t1.returnTotalSeconds()<<endl;
    cout<<"Time t2 in minutes and seconds:"<<t2.returnMinutes()<<":"<<t2.returnSeconds()<<endl;
    cout<<"Time t2 in minutes:  "<<t2.returnMinutes()<<endl;
    cout<<"Time t2 in seconds:"<<t2.returnTotalSeconds()<<endl;
    cout<<"Time comparison between t1 and t2:  ";
    t.comparison(t1,t2);
    cout<<"Time subtraction between t1 and t2  ";
    t.subtraction(t1,t2);
    cout<<"Time addition between t1 and t2  ";
    t.addition(t1,t2);
}













