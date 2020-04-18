def miniMaxSum(arr):
    total = sum(arr)
    all_sums = []
    for i in arr:
        all_sums.append(total-i)
    print(min(all_sums), max(all_sums))

miniMaxSum([1,2,3,4,5])



//Importing various libraries
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//Function to calculate the number of letters in the input string
int count_letter(string inp_text)
{
    int letters = 0;
    for (int i = 0, n = strlen(inp_text); i < n; i++)
    {
        if (isalpha(inp_text[i]))
        {
            letters++;
        }
    }
    return letters;
}

//Function to calculate the number of words in the input string
int count_words(string inp_text_w)
{
    int words = 1;
    for (int i = 0, n = strlen(inp_text_w); i < n; i++)
    {
        if (isspace(inp_text_w[i]))
        {
            words++;
        }
    }
    return words;

}

//Function to calculate the number of sentences in the input string
int count_sentences(string inp_text_s)
{
    int sentences = 0;
    for (int i = 0, n = strlen(inp_text_s); i < n; i++)
    {
        if (inp_text_s[i] == '.' || inp_text_s[i] == '!' || inp_text_s[i] == '?')
        {
            sentences++;
        }
    }
    return sentences;
}

//Function to calculate the final index using the Coleman-Liau index formula
float calc_index(float le, float wo, float se)
{
    float L = (le * 100) / wo;
    float S = (se * 100) / wo;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    return (round(index));
}

//To check if the answer lies below or above the set limits and returning the answers accordingly
int get_answer(int ans)
{
    if (ans < 0)
    {
        return 1;
    }
    if (ans > 16)
    {
        return 16;
    }
    else
    {
        return ans;
    }
}

int main(void)
{
    string text = get_string("Text: "); // Prompting the human for typing in a string
    int tot_letters = count_letter(text); // Total letter stored in the variable, calculated using the function "count_letter"
    int tot_words = count_words(text); // Total words stored in the variable, calculated using the function "count_words"
    int tot_sentences = count_sentences(text);
     // Total sentences stored in the variable, calculated using the function "count_sentences"
    int answer = calc_index(tot_letters, tot_words, tot_sentences);
    if (get_answer(answer) == 16)
    {
        printf("Grade 16+\n");
    }
    else if (get_answer(answer) == 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", get_answer(answer));
    }

}



