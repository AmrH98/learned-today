//  CC 273 DATA infixUCTURE 1 FinalProject Spring 2020

#include <iostream>
#include <string.h>
#include <stack>
#include <vector>
#include <cstdlib>
#include <math.h>
#include <fstream>
#include <sstream>

using namespace std;

bool checkPeriority(char a, char b) {
    int aWeight, bWeight = 2;
    if (a == '*' || a == '/')
        aWeight = 2;
    else
        aWeight = 1;
    return aWeight >= bWeight;
}

int check(char *val) {
    int i;
    for (i = 0; i < strlen(val); i++) {
        if (!((val[i] >= '0' && val[i] <= '9') || (val[i] == '.')))

            return 0;
    }
    return 1;
}

bool isAnOperator(char a) {
    if (a == '+' || a == '-' || a == '*' || a == '/') {
        return true;
    } else
        return false;
}

bool isNegative(char *x) {
    if (x[0] == '-' && isdigit(x[1]))
        return true;
    else
        return false;
}

string infixToPostfix(string infix) {
    string postfix;
    stack<char> stack;
    for (int i = 0; i < infix.length(); i++) {
        if (isdigit(infix[i]) || infix[i] == '.') {
            postfix += infix[i];
            if (isAnOperator(infix[i + 1]) || (infix[i + 1] == '(')) {
                postfix += " ";
            }
        } else if (infix[i] == '-' && isdigit(infix[i + 1]) && stack.empty()
                   && !isdigit(infix[i - 1])) {
            postfix += infix[i];
            postfix += infix[i + 1];
            if (!isdigit(infix[i + 2]))
                postfix += " ";
            i = i + 1;
        } else if (infix[i] == '*' && infix[i + 1] == '-' && isdigit(infix[i
                                                                           + 2])) {
            postfix += infix[i + 1];
            postfix += infix[i + 2];
            postfix += " ";
            postfix += '*';
            i = i + 2;
        } else if (infix[i] == '(') {
            stack.push(infix[i]);
        } else if (isAnOperator(infix[i])) {
            if (stack.empty() || stack.top() == '(') {
                stack.push(infix[i]);
            }

            else if (checkPeriority(infix[i], stack.top())) {
                stack.push(infix[i]);
            }

            else {
                postfix += " ";
                postfix += stack.top();
                postfix += " ";
                stack.pop();
                stack.push(infix[i]);
            }
        } else if (infix[i] == ')') {
            while (stack.top() != '(') {
                postfix += " ";
                postfix += stack.top();
                stack.pop();
            }
            if (stack.top() == '('){
                postfix += " ";
                stack.pop();
            }
        }
        if (infix[i] == ' ') {
            continue;
        }
    }
    while (!stack.empty()) {
        postfix += " ";
        if (stack.top() != '(')
            postfix += stack.top();
        stack.pop();
    }
    return postfix;
}

double evaluatePostfix(string postfix) {
    double op1, op2;
    stack<double> stack;
    char p[postfix.length()];
    strcpy(p, postfix.c_str());
    char *token = strtok(p, " ");
    while (token != NULL) {
        if (isdigit(*token) || isNegative(token)) {
            stack.push(atof(token));
        } else if (*token == '+') {
            op1 = stack.top();
            stack.pop();
            op2 = stack.top();
            stack.pop();
            stack.push(op1 + op2);
        } else if (*token == '-') {
            op1 = stack.top();
            stack.pop();
            op2 = stack.top();
            stack.pop();
            stack.push(op2 - op1);
        } else if (*token == '*') {
            op1 = stack.top();
            stack.pop();
            op2 = stack.top();
            stack.pop();
            stack.push(op1 * op2);
        } else if (*token == '/') {
            op1 = stack.top();
            stack.pop();
            op2 = stack.top();
            stack.pop();
            stack.push(op2 / op1);
        } else {
            cout << "WRONG OPERATORS! \n";
        }
        token = strtok(NULL, " ");
    }
    return stack.top();
}

bool isNumber(string s) {
//	for (int i = 0; i < s.length(); i++)
//		if (isdigit(s[i]) == false)
//			return false;
//
//	return true;
    return s.find_first_not_of( "0123456789." ) == string::npos;
}

string substitute(vector<string> variables, vector<string> equations, string eq) {
    for(int i = 0; i < variables.size(); i++) {
        string var = variables.at(i);
        string value = equations.at(i);
        if(!isNumber(value)) {
            continue;
        }

        size_t pos = eq.find(var);
        if (pos == std::string::npos) {
            continue;
        }
        eq.replace(pos, var.length(), value);
    }

    return eq;
}


    struct node {  //node classifier

        int alpha;
        node *left;
        node *right;

        ~node() {
            delete left;
            delete right;
        }
    };
    node *root;

    void insert_alpha(node** tree, int a)       //insert integer a to bst
    {
        if (*tree) {
            if (a < (*tree)->alpha)
                insert_alpha(&(*tree)->left, a);
            else
                insert_alpha(&(*tree)->right, a);
        } else {
            *tree = new node;
            (*tree)->alpha = a;
            (*tree)->right = NULL;
            (*tree)->left = NULL;
        }
    }

//    void p_ordered(node *z) { // values
//        if (z == NULL)
//            return;
//        else {
//            p_ordered(z->left); //recurse through function to print left most items then right *ascending*
//            cout << z;
//            p_ordered(z->right);
//        }
//    }

    void insert_array(int arr[], int n, node** z) { //insert the array integer into the nodes label of BST
        for (int i = 0; i < n; i++) {
            insert_alpha(z, arr[i]);
        }
    }

//        void sort(int list[], int a) {
//
//            node *z;
//            root = NULL;
//            for (int g = 0; g < a; g++) {
//                insert(list[g], root);
//            }
//        }
    void insert_into(int arr[], node **tree, int *i) {      //insert the array node into tree traversal
        if (*tree) {
            if ((*tree)->left) insert_into(arr, &(*tree)->left, i);
            arr[(*i)++] = (*tree)->alpha;
            if ((*tree)->right) insert_into(arr, &(*tree)->right, i);
        }
    }

int main() {

    char filename[50] = "/Users/amr/Downloads/Project/bst/sourcefile.txt";
    ifstream ds1;
    ds1.open(filename);
    if (ds1.is_open()) {
    } else {
        // show message:
        std::cout << "Error opening file\n";
        return 0;
    }

    string line;
    vector<string> variables, equations;
    string var, eq;
    char bst_test;
    int list_test[6]; // edit to variable array size to following equation

    int i = 0;

    while (std::getline(ds1, line)) { //parameters source, string
        std::string delimiter = " = "; //parse string, len parsed
        size_t pos = line.find(delimiter);
        // parse variable from equation
        var = line.substr(0, pos);
//        cout << var << "\n";
        assert(var.size() == 1); //convert var type__string to type__char
        bst_test = var[0]; //inserted value
//        cout << int(bst_test);
        list_test[i] = int(bst_test);

        eq = line.substr(pos + 3, line.size());
        variables.push_back(var);
        equations.push_back(eq);
        i++;
    }

    node *maintree = NULL;
    insert_array(list_test, i, &maintree);    //insert elements into BST
    int index = 0;
    insert_into(list_test, &maintree, &index);  //modify array sorting chars
    delete maintree;

//    for (int y = 0; y < i; y++)
//        cout << char(list_test[y]) << "\n";
//    cout << '\n';

    cout << "WELCOME TO ANY NUMBERS INFIX TO POSTFIX EVALUATION: \n";
    cout << "----------------------------------------------------\n";
    for (int j = 0; j < i; j++) {
        string s = equations.at(j);
        string eq = substitute(variables, equations, s);
        string postfix = infixToPostfix(eq);
        double result = evaluatePostfix(postfix);

        char buffer[128];
        snprintf(buffer, sizeof(buffer), "%g", result);
        equations[j] = buffer;
        cout << "YOUR INFIX = " << s << "\n";
        cout << "YOUR EQ = " << eq << '\n';
        cout << "YOUR POSTFIX = " << postfix << '\n';
        cout << "YOUR RESULT = " << result << '\n';
        cout << "----------------------------------------------------\n";
    }

    cout << "RESULTS\n---------------\n";

    for (int j = 0; j < i; j++) {
        cout << variables.at(j) << " = " << equations.at(j) << "\n";
    }

    cout << "\n" << "BST \n---------------\n"; // adjust equation value to match variable
    for (int y = 0; y < i; y++)
        cout << char(list_test[y]) << " = "<< equations.at(y) <<"\n";
    cout << '\n';

    ds1.close();
    return 0;
}

