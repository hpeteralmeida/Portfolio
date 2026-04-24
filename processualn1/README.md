# 🌿 Sinta-Se | Perfumaria Exclusiva

![alt text](./images/paginainicial.png)

A **Sinta-Se** é uma plataforma de e-commerce conceitual dedicada à perfumaria de nicho. O projeto une um design minimalista e sofisticado com uma arquitetura de código moderna, focada em performance e escalabilidade através de renderização dinâmica de dados com JavaScript.

---

## 🎨 Identidade Visual e Design

O projeto foi construído sob uma paleta de cores terrosas e orgânicas, evocando a sofisticação dos ingredientes naturais e o luxo clássico.

### Paleta de Cores
* **Background do Site:** `#FAEDCD` (Um tom creme quente que proporciona uma leitura confortável e luxuosa).
* **Header & Elementos de Destaque:** `#7F4F24` (Marrom café profundo para autoridade e contraste).
* **Texto & Tipografia:** `#FEFAE0` (Off-white utilizado sobre fundos escuros para máxima legibilidade).

### Tipografia
* **Playfair Display:** Utilizada em títulos e logotipos para transmitir elegância e tradição.
* **Poppins / Montserrat:** Fontes sans-serif utilizadas para textos de apoio e corpo, garantindo uma interface limpa e moderna.

---

## 🤖 Processo Criativo com Inteligência Artificial

Este projeto é um estudo de caso sobre a simbiose entre o desenvolvimento humano e a Inteligência Artificial Generativa:

* **Imagens:** Toda a asset visual, incluindo os frascos de perfumes, paisagens e modelos, foi gerada via IA, buscando texturas realistas e iluminação cinematográfica.
* **Copywriting:** As descrições das fragrâncias, notas olfativas e narrativas de marca foram criadas utilizando modelos de linguagem avançados para garantir uma comunicação persuasiva e poética.

---

## 💻 Detalhes Técnicos e Arquitetura

O site foi desenvolvido focando em um código limpo (*Clean Code*) e na modularização de estilos e comportamentos.

### Tecnologias Utilizadas
* **HTML5 Semântico:** Estruturação focada em acessibilidade e SEO.
* **CSS3 Avançado:** * Uso de **CSS Grid** para layouts complexos (como o header simétrico e o grid do catálogo).
    * **Flexbox** para alinhamentos internos e fluidez.
    * **Responsive Design:** O site é totalmente adaptável para mobile, utilizando breakpoints estratégicos e o conceito de *Menu Hambúrguer* via CSS puro.
* **JavaScript Vanilla:** * **Páginas Dinâmicas:** Implementação de uma lógica de `URLSearchParams` que permite carregar múltiplos produtos usando um único arquivo `produto.html`.
    * **Data Object Management:** Os dados dos produtos são gerenciados através de um objeto centralizado, facilitando a manutenção e atualização da coleção.

### Destaques do Código
* **Search Interativa:** Barra de busca expansível no mobile que prioriza o espaço em tela.
* **Sistema de IDs:** Navegação inteligente entre catálogo e detalhes sem a necessidade de múltiplos arquivos HTML estáticos.
* **UX/UI:** Inclusão de elementos de prova social (estrelas de satisfação) e hierarquia visual clara.

---

## 📂 Estrutura de Pastas
```bash
/sinta-se
│
├── index.html          # Landing Page principal
├── /paginas
│   ├── catalogo.html   # Grade de produtos
│   ├── produto.html    # Template dinâmico de detalhes
│   └── cadastro.html   # Área de login/cadastro
│
├── /css
│   └── style.css       # Estilização global e responsividade
│
├── /js
│   └── script.js       # Lógica do catálogo e preenchimento de dados
│
└── /images             # Assets visuais do projeto