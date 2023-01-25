typedef enum {
    TK_RESERVED, // 記号（"+" or "-"）
    TK_NUM,
    TK_EOF,
} TokenKind;

typedef struct Token Token;

struct Token {
    TokenKind kind;
    Token *next; //　次のToken型
    int val;
    char *str; // 引数の文字列
    int len; // トークンの長さ（ex. + -> 1, != -> 2）
};
