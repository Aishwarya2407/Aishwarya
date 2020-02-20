#include<stdio.h>
int main()
 {
    int day;
    int msg;
    float data;
    scanf("%d,%d,%f",&day,&msg,&data);
if (day==84)
{
    printf("last day");
    printf("remaining msg=%d/n",100-msg);
    printf("remaining data=%f/n",1.5-data);
}
else if(day<84)
{
    printf("remaining day=%d/n",84-day);
    printf("remaining msg=%d/n",100-msg);
    printf("remaining data=%f/n",1.5-data);
}
else
{
    printf("expired");
}
}


