CFLAGS=-std=c11 -g -static  # -std=c11: Cの最新規格であるC11で書かれたソースコードということを伝える
SRCS=$(wildcard *.c)  # -g: デバグ情報を出力する
OBJS=$(SRCS:.c=.o)  # -static: スタティックリンクする

9cc: $(OBJS)
	$(CC) -o 9cc $(OBJS) $(LDFLAGS)

$(OBJS): 9cc.h  # すべての.oファイルが9cc.hに依存している

test: 9cc
	./test.sh

clean:
	rm -f 9cc *.o *~ tmp*

.PHONY: test clean