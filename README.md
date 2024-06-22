# 🚧 Debugging `requests_html` 🚧

Este repositório foi criado para ajudar a identificar e corrigir um problema na biblioteca `requests_html`. Aqui você encontrará exemplos de código, instruções para reprodução do problema e diretrizes para contribuir com a solução.

## Objetivo

O objetivo deste projeto é:

- Reproduzir o problema encontrado na biblioteca `requests_html`.
- Analisar o comportamento e identificar a causa raiz do problema.
- Propor e testar possíveis soluções.
- Documentar o processo de depuração e as soluções encontradas.

## Estrutura do Repositório

- `files/`: Contém páginas HTML baixadas.
- `logs/`: Logs e arquivos de saída para ajudar na análise.
- `examples/`: Contém exemplos de código que demonstram o problema.
- `links.csv`: Links usados para reproduzir o erro.
- `README.md`: Este arquivo de documentação.

## Requisitos

Para reproduzir e depurar o problema, você precisará do seguinte (embora o erro já tenha sido reproduzido em diversas máquinas com diferentes versões de software):

- Python 3.8.10
- `requests_html` (0.10.0)

## Como Reproduzir o Problema

1. Clone este repositório:

    ```bash
    git clone https://github.com/carloseduardobanjar/debug-requests-html.git
    cd debug-requests-html
    ```

2. Caso deseje testar mais de uma vez, é recomendável baixar as páginas HTMLs para que não seja necessário fazer requisições diversas vezes, o que leva tempo.

    Para baixar as páginas HTML, execute a célula `Download HTML pages` no arquivo `examples/download_and_find.ipynb`. Em seguida, basta executar `examples/demo_problem.py`:

    ```bash
    python3 examples/demo_problem.py > logs/output.log 2>&1
    ```

3. Se você quiser testar apenas uma vez, descomente o trecho comentado em `examples/demo_problem.py` e comente o trecho que está em uso. Fazer dessa forma pode demorar mais, mas ambas as formas permitem reproduzir o erro.

4. Verifique os logs gerados no diretório `logs/` para mais detalhes sobre o comportamento do problema.

**Observação 1:** O problema geralmente é identificado quando o código parece ficar parado sem mostrar nenhum log de erro ou conclusão.

**Observação 2:** Não foi possível reproduzir o erro rodando a célula `Extract information from each downloaded HTML page` do Notebook Jupyter, apenas com o script `demo_problem.py`.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou entrar em contato.