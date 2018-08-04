#include<stdio.h>
#include<malloc.h>
using namespace std;
typedef struct Node{
	int val;
	Node* next;
}Node;
Node* create(){
	Node* head = (Node*)malloc(sizeof(Node));
	head->next = NULL;
	head->val = 0;
	return head;
}
void add(Node* head, int x){
	Node* cnt = head;
	while (cnt->next != NULL){
		cnt = cnt->next;
	}
	cnt->next = (Node*)malloc(sizeof(Node));
	cnt = cnt->next;
	cnt->next = NULL;
	cnt->val = x;
}
bool reverse(int m, Node* head){
	//每m个翻转一次,不够m个不反转
	Node* a = head;
	Node* p = head->next;
	if (a->next == NULL)	return false;
	if (p->next == NULL)	return false;
	Node* b = p;
	Node* cnt = p->next;
	Node* n = cnt->next;
	Node* t = p;
	int j = 0;
	while (true){
		j = 0;
		t = p;
		while (t != NULL && j < m - 1){
			t = t->next;
			j++;
		}
		if (t == NULL){
			break;
		}
		//printf("%d", t->val);
		for (int i = 0; i < m - 1; i++){
			n = cnt->next;
			cnt->next = p;
			p = cnt;
			cnt = n;
		}
		a->next = p;
		b->next = cnt;
		p = cnt;
		if (cnt != NULL)	cnt = cnt->next;
		a = b;
		b = p;
	}
	return true;
}
void show(Node* head){
	Node* cnt = head;
	while (cnt->next != NULL){
		printf("%d", cnt->next->val);
		cnt = cnt->next;
	}
	printf("\n");
}
int main(){
	/*int i = 0;
	printf("%d", i);*/
	Node* head = create();
	for (int i = 0; i < 12; i++){
		add(head, i);
	}
	//printf("%d",head[3]);
	show(head);
	//reverse(2,head);
	//show(head);
	return 0;
}