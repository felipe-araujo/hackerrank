#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    int size_diff = strlen(a) - strlen(b);

    if(size_diff !=0) {
        return size_diff;
    }

    int i = 0;
    while(a[i] != '\0' && b[i]!= '\0' && a[i] == b[i]){
        i++;
    }
    if(a[i] == '\0' && b[i] != '\0'){
        return -1;
    }else if(a[i] != '\0' && b[i] == '\0'){
        return 1;
    }

    // equals up to i index
    return a[i] - b[i];
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return -lexicographic_sort(a, b);
}

int count_distinct_characters(const char* a){
    
    int distinct = 0;
    for(int i=0; i<strlen(a)-1; i++){
        int repeated_ahead = 0;
        for(int j=i+1; j<strlen(a); j++){
            if(a[i] == a[j]){
                repeated_ahead = 1;
            }
        }
        if(repeated_ahead == 0){
            distinct++;
        }
    }

    return distinct+1;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    return count_distinct_characters(a) - count_distinct_characters(b);
}

int sort_by_length(const char* a, const char* b) {
    return strlen(a) - strlen(b);
}

void safe_swap(char **arr, int i, int j){
    char* temp = (char*)calloc(strlen(arr[i]), sizeof(char));
    strcpy(temp, arr[i]);
    arr[i] = arr[j];
    arr[j] = temp;
}

void string_sort(char** arr, const int len, int (*cmp_func)(const char* a, const char* b)){
    //qsort(tr, n, sizeof(triangle), cmpfunc);
    // use insertion sort algo
    // printf("string sort");
    for(int i=1; i< len-1; i++){ 
        int cmp = cmp_func(arr[i], arr[i+1]);
        
        if(cmp>0){
            // printf("cmp=%d\n", cmp);
            int j = i-1;
            // printf("j=%d, arr[j]=%s, arr[j+1]=%s", j, arr[j], arr[j+1]);
            // printf("cmp res = %d\n", cmp_func(arr[j], arr[j+1]));
            // safe_swap(arr, j, j+1);
            while(j >=0 && cmp_func(arr[j], arr[j+1]) > 0){
                //printf("j=%d, arr[j]=%s, arr[j+1]=%s", j, arr[j], arr[j+1]);
                //printf("\nsafe_swap(arr, j, j+1);\n");
                safe_swap(arr, j, j+1);
                j--;
            }  
        }

       /** 
        if(cmp>0){
            char* temp = (char*)calloc(strlen(arr[i+1]), sizeof(char));
            strcpy(temp, arr[i+1]);
            int t = i ;
            for(int j=i; j>=0; j--){
                t = j;
                //strcpy(arr[j+1], arr[j]);
                safe_swap(arr, j+1, j);
                if(cmp_func(arr[j], temp) < 0){
                    //swap and finish
                    break;
                }
            }
            strcpy(arr[t], temp);

           
        }

         **/
    }
    
}

int test_lexicographic_sort(){
    char a[] = "abcDE";
    char b[] = "abcAT";
    printf("\n%d",lexicographic_sort(a, b));
    printf("\n%d",lexicographic_sort_reverse(a, b));
}

int test_count_distinct(){
    char a[] = "aabaacdeeededa";
    char b[] = "a";

    printf("\ndistinct chars in [%s]: %d", a, count_distinct_characters(a));
    printf("\ndistinct chars in [%s]: %d", b, count_distinct_characters(b));
}

void test_safe_swap(){
    char a[] = "aaaa";
    char b[] = "bbbb";
}

int main_test(){
    test_lexicographic_sort();
    test_count_distinct();
    printf("\n");
}

int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}