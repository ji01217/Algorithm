#include <stdio.h>

int main()
{
  int h, w, n, l, d, x, y;
  scanf("%d %d", &h, &w);
  int a[101][101]={};
  scanf("%d", &n);
  for (int i=1;i<=n;i++){
    scanf("%d %d %d %d", &l, &d, &x, &y);
    if(d==0){
      // 가로
      for(int j=1;j<=l;j++){
        a[x][y+j-1]=1;
      }
    } else{
      // 세로
      for(int j=1;j<=l;j++){
        a[x+j-1][y]=1;
      }
    }
  }
  for(int i=1;i<=h;i++){
    for(int j=1;j<=w;j++){
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return 0;
}