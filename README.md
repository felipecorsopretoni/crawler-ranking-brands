# Experimento 01 – Web Crawler com Scrapy

## 📌 Objetivo

Desenvolver um crawler utilizando o framework **Scrapy** para coletar marcas iniciadas pelas letras **A** e **B** no site:

https://www.rankingthebrands.com

---

## 🛠 Tecnologias Utilizadas

- Python 3.12
- Scrapy 2.14.1

---

## 📂 Estrutura do Projeto

```

crawler-ranking-brands/
│
├── experimentos/
│   └── exp01-crawler-ranking-brands-ab.py
├── README.md
└── requirements.txt

```

---

## ▶️ Como Executar

1️⃣ Instalar dependências:

```

pip install -r requirements.txt

```

ou

```

pip install scrapy

```

2️⃣ Executar a spider:

```

python -m scrapy runspider experimentos/exp01-crawler-ranking-brands-ab.py -O marcas_ab.json

```

---

## 📦 Saída

O crawler gera o arquivo:

```

marcas_ab.json

```

Cada item contém:

- `letter` → Letra filtrada (A ou B)
- `brand_name` → Nome da marca
- `brand_url` → Link da marca
- `source_url` → Página de origem

---

## ⚙️ Configurações do Crawler

- Respeita o arquivo `robots.txt`
- Delay de 1 segundo entre requisições
- Limite de 2 requisições simultâneas por domínio
- User-Agent personalizado

---

## 👨‍💻 Autor

Felipe Corso Pretoni
