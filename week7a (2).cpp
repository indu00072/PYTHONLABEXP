#include<bits/stdc++.h>
using namespace std;
class buliding{
public:
   int buildings;
   int getBuildings(){
       return buildings;
   }
};
class floors: public buliding{
    public:
        int floor1;
        int getfloors()
        {
            return floor1;
        }
};
class rooms:public floors{
    public:
        int rooms1;
        int getrooms()
        {
            return rooms1;
        }
};
class networkAccesspoints :public rooms{
    public:
        int nap;
        bool stsAP=true;;
        int getNAP()
        {
            return nap;
        }
        bool statusofAP(){
            return stsAP;
        }
        void onAP()
        {
            stsAP=(!stsAP);
        }
};
int main()
{
    int floor1,rooms1,nap,total,buildings;
    networkAccesspoints s;
    cout<<"Enter no of buildings:\n";
    cin>>buildings;
    s.buildings=buildings;
    cout<<"Enter no of floors:\n";
    cin>>floor1;
    s.floor1=floor1;
    cout<<"Enter no of Rooms:\n";
    cin>>rooms1;
    s.rooms1=rooms1;
    cout<<"Enter no of Access points in a room;\n";
    cin>>nap;
    s.nap=nap;
    cout<<"Total Buildings :"<<buildings<<endl;
    cout<<"Total Floors:"<<s.getfloors()<<endl;
    cout<<"Total Rooms:"<<s.getrooms()<<endl;
    cout<<"Total networkAccesspoints :"<<s.getNAP()<<endl;
    total=floor1*rooms1*nap*buildings;
    if(s.statusofAP()==1)
        cout<<"networkAccesspoints: ON status\n month turned ON"<<endl;
    else
        cout<<"networkAccesspoints: OFF status\n";
    s.onAP();
    cout<<"After changing the status of networkAccesspoints:\n";
    if(s.statusofAP()==1)
        cout<<"networkAccesspoints: ON status\n month turned ON"<<endl;
    else
        cout<<"networkAccesspoints: OFF status\n";
    cout<<"Total networkAccesspoints in Buildings:"<<total<<endl;
}




