#include <stdio.h>

int main()
{
  int n;
  scanf("%x", &n);
  for(int i=1;i<=n;i++){
    if(i%3>0){
      printf("%d ", i);
    } else {
      printf("X ");
    }
  }
  return 0;
}