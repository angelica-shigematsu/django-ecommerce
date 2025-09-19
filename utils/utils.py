def cart_total_qtd(carrinho):
  return sum([item['quantidade'] for item in carrinho.values()])

def cart_totals(carrinho):
  return sum(
    [
      float(item.get('preco_quantitativo_promocional'))
      if item.get('preco_quantitativo_promocional')
      else float(item.get('preco_quantitativo'))
      for item
      in carrinho.values()
    ]
  )