# BTC Discover

Um script para descobrir chaves privadas de carteiras Puzzle Bitcoin.

A idéia é gerar chaves privadas aleatórias e verificar se a chave privada corresponde a uma carteira Puzzle Bitcoin. Se for esse o caso, parabéns, você já pode abrir o champanhe!

## Executando

```bash
python main.py
```

## Alterando opções

Você pode alterar o range de valores aleatórios gerados para as chaves privadas no arquivo `main.py`. Basta editar as constantes `MIN` e `MAX`. E para os endereços das carteiras Puzzle, você pode alterar a lista `WALLETS`.
