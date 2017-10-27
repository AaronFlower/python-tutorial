#include <iostream>

using namespace std;

void insertion_sort(int * a, int len)
{
	for(int i = 1; i < len; ++i) {
		int j = i;
		while (j > 0 && a[j] < a[j - 1]) {
			int tmp = a[j];
			a[j] = a[j - 1];
			a[j - 1] = tmp;
			j--;
		}
	}
}

void printData(int * data, int len)
{
	for(int i = 0; i < len; ++i) {
		cout<<data[i] << "\t";
	}
}

int main()
{
	int data[] = {3, 4, 1, 8, 99, 12, 31, 5};
	int len = sizeof(data) / sizeof(data[0]);
	cout<< "Before Sorting:";
	printData(data, len);
	insertion_sort(data, len);
	cout<< "\nAfter  Sorting:";
	printData(data, len);
	return 0;
}