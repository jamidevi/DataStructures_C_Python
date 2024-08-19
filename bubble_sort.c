#include<stdio.h>
int main()
{
    int n,arr[100],i,j,temp;
    //Reading the number of Elements 
    printf("Enter the Number of Elements in the Array:");
    scanf("%d",&n);
    //Reading the Array Elements 
    printf("Enter the Elements in to the Array:");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    //Performing the Bubble sorting
    for(i=1;i<n;i++){
        for(j=0;j<n-i;j++){
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
            
        }
    }
    // Printing the Sorted Array
    printf("*-*Sorted Array*-*\n");
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
    
}