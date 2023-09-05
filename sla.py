from classes import *
p1 = Produtos("Notebook", 4500)
p2 = Produtos("Iphone", 8000)
p3 = Produtos("Tablet", 2500)
p4 = Produtos("Macbook", 8000)
p5 = Produtos("Xiaomi Redmi 9", 2000)
p6 = Produtos("Sansung A70", 1200)
p7 = Produtos("TV LG 50 polegadas", 2300)
p8 = Produtos("TV LG 70 polegadas", 4180)
p9 = Produtos("TV BOX", 650)

Carrinho_Andre = Carrinho_Compras()

Carrinho_Andre.inserir_produto(p1)
Carrinho_Andre.inserir_produto(p2)
Carrinho_Andre.inserir_produto(p3)
Carrinho_Andre.inserir_produto(p4)
Carrinho_Andre.inserir_produto(p5)
Carrinho_Andre.inserir_produto(p6)
Carrinho_Andre.inserir_produto(p7)
Carrinho_Andre.inserir_produto(p8)
Carrinho_Andre.inserir_produto(p9)



Carrinho_Andre.listar_produtos()

Carrinho_Andre.delProduto(1)
print("----------------------------------------------")
Carrinho_Andre.listar_produtos()