// buildTree.cc --- 
// 
// Filename: buildTree.cc
// Description: 
// 
// Author:    Yu Lu
// Email:     yulu@utexas.edu
// Github:    https://github.com/SuperYuLu 
// 
// Created: Wed Nov 21 21:41:21 2018 (-0600)
// Version: 
// Last-Updated: Thu Nov 22 14:34:52 2018 (-0600)
//           By: yulu
//     Update #: 128
// 
#include<iostream>
#define END -1024 // handle tree leaf end, since NULL is anbiguous

template <class T>
struct Node
{
  T root;
  Node* left;
  Node* right;
  Node(): root(0), left(nullptr), right(nullptr){};
  Node(T x): root(x), left(nullptr), right(nullptr){};
  void inorderTraversal();
};

template <class T>
void Node<T> :: inorderTraversal()
{
  if(root != END)
    {
      std::cout << this -> root << std::endl;
      if(left)
	left -> inorderTraversal();
      if(right)
	right -> inorderTraversal();
    }
}
    


template <class T>
Node<T>* newNode(T val, Node<T>* ptrLeft, Node<T>* ptrRight)
{
  
}

template <class T>
Node<T>* createBinaryTree(T a[], int i, int size)
{
  if (i >= size)
    return nullptr;
  else
    {
      Node<T>* t = new Node<T>;
      t -> root = a[i];
      t -> left = createBinaryTree(a, 2 * i + 1, size);
      t -> right = createBinaryTree(a, 2 * i + 2, size);
      return t;
    }
}


int main(){
  float x[] = {1,2.3,3, END, 4, 5};
  Node<float>* tree;
  tree = createBinaryTree(x, 0, 6);
  tree -> inorderTraversal();
}
