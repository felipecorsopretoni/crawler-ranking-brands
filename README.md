# 🕷️ Crawler — Ranking The Brands

Crawler desenvolvido com **Scrapy** para coletar todas as marcas de A a Z do site [Ranking The Brands](https://www.rankingthebrands.com) e armazená-las no **MongoDB**.

---

## 📋 Sobre o Projeto

O projeto realiza a raspagem automática de marcas cadastradas no site Ranking The Brands, filtrando letra por letra (A–Z) e salvando os dados coletados em um banco de dados MongoDB.

---

## ✨ Funcionalidades

- 🔤 **Coleta A–Z** — percorre todas as letras do alfabeto automaticamente
- 🗄️ **Armazenamento no MongoDB** — salva nome, URL da marca e URL de origem
- 🧹 **Limpeza automática** — apaga os dados anteriores antes de cada coleta
- 🤖 **Respeito ao robots.txt** — coleta responsável com delay entre requisições

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

| Tecnologia | Uso |
|------------|-----|
| Python | Linguagem principal |
| Scrapy | Framework de crawling |
| PyMongo | Conexão com MongoDB |
| python-dotenv | Gerenciamento de variáveis de ambiente |

---

## 📁 Estrutura do Projeto

```
crawler-ranking-brands/
├── experimentos/
│   └── exp01-crawler-ranking-brands-ab.py  # Spider principal
├── marcas_ab.json                           # Exemplo de saída
├── requirements.txt                         # Dependências
├── .env                                     # Variáveis de ambiente (não versionado)
└── .gitignore
```

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
- Python 3.8+
- MongoDB rodando localmente ou URI de conexão

### 1. Clone o repositório
```bash
git clone https://github.com/felipecorsopretoni/crawler-ranking-brands.git
cd crawler-ranking-brands
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o `.env`
Crie um arquivo `.env` na raiz com:
```env
MONGO_URI=mongodb://localhost:27017
```

### 4. Execute o crawler
```bash
python -m scrapy runspider experimentos/exp01-crawler-ranking-brands-ab.py
```

---

## 🗄️ Estrutura dos Dados no MongoDB

Cada documento salvo na collection `brands` segue o formato:

```json
{
  "letter": "A",
  "brand_name": "Apple",
  "brand_url": "https://www.rankingthebrands.com/Brand-detail.aspx?brandID=1",
  "source_url": "https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=A"
}
```

---

## ⚠️ Boas Práticas Aplicadas

- `ROBOTSTXT_OBEY: True` — respeita as regras do site
- `DOWNLOAD_DELAY: 1.0` — intervalo de 1 segundo entre requisições
- `CONCURRENT_REQUESTS_PER_DOMAIN: 2` — limite de requisições simultâneas

---

## 👨‍💻 Autor

**Felipe Corso Pretoni**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/felipe-corso-pretoni)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/felipecorsopretoni)
