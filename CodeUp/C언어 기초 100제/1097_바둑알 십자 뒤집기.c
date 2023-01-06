#include <stdio.h>

int main()
{
  int n, i, j, x, y;
  int a[20][20]={};
  for(i=1;i<=19;i++){
    for(j=1;j<=19;j++){
      scanf("%d ", &a[i][j]);
    }
  }
  scanf("%d", &n);
  for(int b=1;b<=n;b++){
    scanf("%d %d", &x, &y);
    for(j=1;j<=19;j++){
      if(a[x][j]==0){
        a[x][j] = 1;
      }else{
        a[x][j] = 0;
      }
    }
    for(i=1;i<=19;i++){
      if(a[i][y]==0){
        a[i][y] = 1;
      }else{
        a[i][y] = 0;
      }
    }
  }
  for(i=1;i<=19;i++){
    for(j=1;j<=19;j++){
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return 0;
}