## Binary Search Tree
given sequence [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
forms a binary search tree (BST). 

Root node: 7
````
                    7
				5 		8
			1 		6		9
          0   3
			2   4

````

Summary

The diagram will visually represent a BST, built in order: 7 is root, 5 is left, 8 is right, etc.
Every child is correctly placed so left children are less and right children are greater than their parent.


- 7 (root)
- 5 (left of 7)
- 1 (left of 5)
- 0 (left of 1)
- 3 (right of 1)
- 2 (left of 3)
- 4 (right of 3)
- 6 (right of 5)
- 8 (right of 7)
- 9 (right of 8)



flowchart TB
    A(("7"))
    B(("5"))
    C(("8"))
    D(("1"))
    E(("6"))
    F(("9"))
    G(("0"))
    H(("3"))
    I(("4"))
    J(("2"))
    
    A --> B
    A --> C
    B --> D
    B --> E
    C --> F
    D --> G
    D --> H
    H --> J
    H --> I

````
---
config:
  layout: dagre
  look: handDrawn
  theme: mc
---
flowchart TB
    A(("7")) --> B(("5")) & C(("8"))
    B --> D(("1")) & E(("6"))
    C --> F(("9"))
    D --> G(("0")) & H(("3"))
    H --> J(("2")) & I(("4"))
````
<img width="302.8" height="448" alt="image" src="https://github.com/user-attachments/assets/6cbbe5cb-61da-4538-b0a2-c13e095586c0" />
