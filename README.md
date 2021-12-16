# MDC Projeto Final - Music Genre Classification

## Contribuidores

*   André Gonçalves [Linkedin](https://www.linkedin.com/in/andregon%C3%A7alves/)/[GitHub](https://github.com/AndreGoncalves013)
*   Danitiele Laranja [Linkedin](https://www.linkedin.com/in/danitiele-laranja-b1232839/)
*   Luísa Lelis [Linkedin](https://www.linkedin.com/in/lu%C3%ADsa-lelis/)
*   Victor Goraieb [Linkedin](https://www.linkedin.com/in/victor-goraieb/)
*   Vitor Silva [Linkedin](https://www.linkedin.com/in/vitoranastaciosilva/)

## Contexto

A última disciplina do curso de [Mineração de Dados Complexos da Unicamp](https://www.ic.unicamp.br/~mdc/) consiste em escolher um conjunto de dados selecionados pelos professores e monitores do curso para que os alunos realizem toda preparação dos dados e façam o uso de modelos de Machine Learning e Deep Learning para obter-se o melhor resultado com o tipo de problema escolhido.

O nosso grupo TD2M (Talk Data to Me) escolheu o problema de [Music Genre Classification](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification) por ser um problema que tem dados tabulares em csv, arquivos de imagem png e arquivos de áudio wav. Assim, poderíamos dividir os conjuntos de dados entre os integrantes do grupo para que testássemos diversos modelos com esses tipos de dados.

## Como executar os arquivos

1. **Download dos dados**
    1. Via git clone <br>
  Instale o [git](https://git-scm.com/downloads) na sua máquina e siga o [tutorial da criação da chave ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) para poder clonar os arquivos na sua máquina 
    2. Download do arquivo zip <br>
  Também a opção de fazer o download de todo o projeto em zip. Baixe o mesmo e extraia os seus arquivos no seu diretório de trabalho. 
  <br>
2. **Preparando os dados para modelagens**<br>
  Caso queira baixar os arquivos de dados diretamente do kaggle, siga o passo a passo abaixo:
    1.  Download dos arquivos do Kaggle<br>
  Execute o arquivo _download_data.ipynb_ para que seja feito o download dos dados de imagem, som e tabulares disponíveis no Kaggle em um diretório padrão que é usado pelos outros arquivos do projeto.
    2.  Convertendo arquivos de imagem de RGBA para RGB<br>
  Como os arquivos png baixados estão em formato RGBA, é necessário convertê-los para RGB para que possam ser usados nos modelos. Para isso, rode o código em _conversor_rgba_rgb.ipynb_ que criará uma nova pasta com as imagens png com padrão de canais de cores RGB.
    3.  Dividindo os dados em conjuntos de treino, validação e teste<br>
  Como parte da disciplina, é necessário que todos os grupos que escolheram o problema de Music Genre Classification precisassem alinhar quais exemplos de dados serão utlizados no conjunto de treino, validação e teste para que os resultados possam ser mais comparáveis entre os grupos. <br>
  Para isso, o código disponível em _data_split.ipynb_ faz a divisão dos dados salvando o nome dos arquivos que ficaram em cada um dos conjuntos de dados em csvs separados. Estes são depois utilizados na função _get_train_val_set_data_ em _utils.py_ para garantir que todos do grupo usassem os dados certos em seus modelos.
  <br>
3. **Executando os códigos dos modelos**<br>

