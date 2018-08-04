#include<stdio.h>
#include<malloc.h>
typedef struct Node{
	int val;
	Node* next;
}Node;
Node* create(){
	Node* head = (Node*)malloc(sizeof(Node));
	head->val = 0;
	head->next = NULL;
	return head;
}
void Sequeue(Node* head,int val){
	Node* temp = head;
	while (temp->next != NULL){
		temp = temp->next;
	}
	temp->next = (Node*)malloc(sizeof(Node));
	temp = temp->next;
	temp->val = val;
	temp->next = NULL;
}
int Dequeue(Node* head){
	Node* temp = head->next;
	int val = temp->val;
	head->next = temp->next;
	free(temp);
	return val;
}
void slideWindow(Node* head, int nums[], int k,int length){
	Node* cnt = head;
	int temp = nums[0];
	int val = 0;
	int pos = 0;
	int temp1 = 0;
	//Res* greater = (Res*)malloc(sizeof(Res));
	for (int i = 0; i < k; i++){
		Sequeue(head, nums[i]);
		if (nums[i] >= temp){
			temp = nums[i];
			pos = i;
		}
	}
	printf("%d,%d\n", pos,temp);
	//Res* greater = (Res*)malloc(sizeof(Res));
	for (int i = 3; i < length; i++){
		val = Dequeue(head);
		pos--;
		Sequeue(head, nums[i]);
		if (nums[i] >= temp){
			
			pos = 2;
			printf("%d,%d\n", pos,nums[i]);
			temp = nums[i];
		}
		else{
			if (pos >= 0){
				printf("%d,%d\n", pos,temp);
			}
			else{
				pos = 0;
				cnt = head->next;
				temp1 = cnt->val;
				for (int j = 1; j < k; j++){
					cnt = cnt->next;
					if (cnt->val >= temp1){
						pos = j;
						temp1 = cnt->val;
					}
				}
				printf("%d,%d\n", pos,temp1);
				temp = temp1;
			}
		}
	}
}
int main(){
	Node* head = create();
	int nums[] = { 1, 2, 3, 1, 4, 5, 2, 3, 6 };
	int k = 3;
	slideWindow(head, nums, k,sizeof(nums)/sizeof(nums[0]));
	return 0;
}
