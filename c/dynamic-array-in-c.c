#include <stdio.h>
#include <stdlib.h>

/*
 * This stores the total number of books in each shelf.
 */
//int* total_number_of_books;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
//int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    
    int** total_number_of_pages;
    int* total_number_of_books;

    total_number_of_pages = (int**) calloc(total_number_of_shelves, sizeof(int));
    total_number_of_books = (int*) calloc(total_number_of_shelves, sizeof(int));

    for(int i=0; i<total_number_of_shelves; i++){
        *(total_number_of_books+i) = 0;        
        *(total_number_of_pages+i) = NULL;
    }

    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        if (type_of_query == 1) {            
            /*
             * Process the query of first type here.
             */
            int x, y;
            scanf("%d %d", &x, &y);
            int number_of_books = *(total_number_of_books+x) + 1;
            *(total_number_of_books+x) = number_of_books;
            if(!(*(total_number_of_pages+x))){
                printf("\n[calloc]\n");
                *(total_number_of_pages+x) = (int*) calloc(1, sizeof(int));
            }else {
                printf("\n[realloc] number_of_books=%d\n", number_of_books);
                int new_size = number_of_books * sizeof(int);
                printf("\n[realloc] memory to be allocated=%d\n", number_of_books);
                int* ptr = (int*) realloc(*(total_number_of_pages+x), new_size);
                *(total_number_of_pages+x) = ptr;
            }
            *(*(total_number_of_pages+x) + number_of_books) = y;



        } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        printf("\nfree total_number_of_books... \n");
        free(total_number_of_books);
        printf("\nfree total_number_of_books... done. \n");
    }
    
    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            printf("\nfree total_number_of_pages+i... \n");
            free(*(total_number_of_pages + i));
            printf("\nfree total_number_of_pages+i... done.\n");
        }
    }
    
    if (total_number_of_pages) {
        printf("\nfree total_number_of_pages... \n");
        free(total_number_of_pages);
        printf("\nfree total_number_of_pages... done.\n");
    }
    
    return 0;
}