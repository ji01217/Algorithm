#include <stdio.h>

int main()
{
  int a[11][11]={};
  int i, j; 
  for (i=1;i<=10;i++){
    for (j=1;j<=10;j++){
      scanf("%d ", &a[i][j]);
    }
  }
  i = 2;
  j = 1;
  while(i>0){
    if (a[i][j+1]==0) {
      // 오른쪽 길이 있다면
      j++;
      a[i][j] = 9;
    } else if (a[i][j+1]==2) {
      // 오른쪽에 먹이가 있다면
      j++;
      a[i][j] = 9;
      break;
    } else if (a[i+1][j]==0) {
      // 아래에 길이 있다면
      i++;
      a[i][j] = 9;
    } else if (a[i+1][j]==2) {
      // 아래에 먹이가 있다면
      i++;
      a[i][j] = 9;
      break;
    } else {
      break;
    }
  }
  for(i=1;i<=10;i++){
    for(j=1;j<=10;j++){
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return 0;
}