#include <stdio.h>

int main()
{
  int n, i, t;
  int a[24] = {};  // 0번부터 23번까지 모두 0으로 초기화
  scanf("%d", &n);
  for(i=1;i<=n;i++){
    scanf("%d ", &t);
    a[t] += 1;
  }
  for(i=1;i<=23;i++){
    printf("%d ", a[i]);
  } 
  return 0;
}