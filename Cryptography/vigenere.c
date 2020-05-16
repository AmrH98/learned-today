#Vigenère’s cipher improves upon Caesar’s cipher by encrypting messages using a sequence of keys (or, put 
#another way, a keyword). In other words, if p is some plaintext and k is a keyword (i.e., an alphbetical 
#string, whereby A represents 0, B represents 1, C represents 2, …​, and Z represents 25),
#then each letter,ci, in the ciphertext, c, is computed as:Note this cipher’s use of kj as opposed to 
#just k. And if k is shorter than p, then the letters in k must be reused cyclically as many times as it takes to encrypt p.
#In other words, if Vigenère himself wanted to say HELLO to someone confidentially, using a keyword of, 
#say, ABC, he would encrypt the H with a key of 0 (i.e., A), the E with a key of 1 (i.e., B), and the first L with a key
#of 2 (i.e., C), at which point he’d be out of letters in the keyword, and so he’d reuse (part of) it to encrypt the second
#L with a key of 0 (i.e., A) again, and the O with a key of 1 (i.e., B) again. And so he’d write HELLO as HFNLP.

#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string key=argv[1];
    //check if input us alpha or more than one
    if (argc!=2)
    {
    printf("Input error\n");
    return 1;
    }

    //check if all string is alphabatical
    int lenarg = strlen(key);
    for (int i=0; i<lenarg;i++)
    {
        if (isalpha(key[i]))
    {
    }
    else
    {
        printf("Input error");
        return 1;
    }
    }
    printf("plaintext:");
    //check char type and convert letter to rotation
    //get word text
    string w = get_string();
    int length = strlen(w);

    //print encrypted word
    printf("ciphertext:");
    //encrypt word
        int i=0;
    for (int a=0;a<length;a++)
    {
    //keep looping through the key
        i = i % lenarg;
        // check if the w is not alpha to not encrypt it
        if (ispunct(w[a]) || iscntrl(w[a]) || isblank(w[a]))
        {
            printf("%c", w[a]);
        }
        else
        {
            if (islower(w[a]) && islower(key[i]))
                printf("%c", (((w[a] - 97) + (key[i] - 97)) % 26) + 97);
            else if (isupper(w[a]) && islower(key[i]))
                printf("%c", (((w[a] - 65) + (key[i] - 97)) % 26) + 65);
            else if (islower(w[a]) && isupper(key[i]))
                printf("%c", (((w[a] - 97) + (key[i] - 65)) % 26) + 97);
            else if (isupper(w[a]) && isupper(key[i]))
                printf("%c", (((w[a] - 65) + (key[i] - 65)) % 26) + 65);
            i++;
        }
    }

    printf("\n");
    return 0;


}
