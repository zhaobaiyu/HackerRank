#include <stdio.h>
#include <stdlib.h>

int main(){
    int n; 
    int c; 
    int m; 
    scanf("%d %d %d",&n,&c,&m);
    int *p = malloc(sizeof(int) * n);
    for(int p_i = 0; p_i < n; p_i++){
       scanf("%d",&p[p_i]);
    }
    m = m * c;
    int ans = 1;
    for (int i = 0; i < n; ++i) {
        if (p[i] > m) {
            ans = 0;
            break;
        }
    }
    if (ans) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
